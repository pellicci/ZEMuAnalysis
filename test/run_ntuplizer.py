#!/usr/bin/env python3
import os
import sys
import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from StandardModel.ZEMuAnalysis.preselector import Preselector
from StandardModel.ZEMuAnalysis.puWeightProducer import *

inputfile = []
if len(sys.argv) > 3 :
    inputfile = [sys.argv[3]]
else :
    inputfile = ['/afs/cern.ch/user/p/pellicci/cernbox/ZEMuAnalysis/Production/2024/signal/NANO/ZEMuAnalysis_NANO_2024.root']

print(inputfile)

isData_string = sys.argv[1]
isData = False
if isData_string == "data" :
    isData = True
    print("Running on a data sample")
else :
    print("Running on a MC sample")

myrunningEra = -1
tmp_runningEra = sys.argv[2]
if "2016" in tmp_runningEra :
    myrunningEra = 0
elif "2017" in tmp_runningEra :
    myrunningEra = 2
elif "2018" in tmp_runningEra :
    myrunningEra = 3
elif "2022" in tmp_runningEra :
    myrunningEra = 4
elif "2022EE" in tmp_runningEra :
    myrunningEra = 5
elif "2023" in tmp_runningEra :
    myrunningEra = 6
elif "2024" in tmp_runningEra :
    myrunningEra = 7

print("Running era is ", myrunningEra)

ROOT.PyConfig.IgnoreCommandLineOptions = True

localPath = os.environ['CMSSW_BASE']+"/src/StandardModel/ZEMuAnalysis/test/json/"

jsonFile = None
if isData :
    if myrunningEra == 0 :
        jsonFile = localPath + "Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt"
    elif myrunningEra == 2 :
        jsonFile = localPath + "Cert_294927-306462_13TeV_UL2017_Collisions17_Golden_JSON.txt"
    elif myrunningEra == 3 :
        jsonFile = localPath + "Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"
    elif myrunningEra == 5 :
        jsonFile = localPath + "Cert_Collisions2022_355100_362760_Golden.json"
    elif myrunningEra == 7 :
        jsonFile = localPath + "Cert_Collisions2024_378981_386951_Golden.json"


class exampleProducer(Module):
    def __init__(self, runningEra):
        self.runningEra = runningEra
        pass
    def beginJob(self):
        self.N_totevents = 0.
        pass
    def endJob(self):
        print("Total number of processed events = ", self.N_totevents)
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.histcount = ROOT.TH1F("histocount","Counter of passed events",10,-0.5,9.5)

        self.histcount.GetXaxis().SetBinLabel(1,"Initial eff")
        self.histcount.GetXaxis().SetBinLabel(2,"Trigger")
        self.histcount.GetXaxis().SetBinLabel(3,"Any muon")
        self.histcount.GetXaxis().SetBinLabel(4,"Any electron")
        self.histcount.GetXaxis().SetBinLabel(5,"Momentum cut")
        self.histcount.GetXaxis().SetBinLabel(6,"Quality leptons")
        self.histcount.GetXaxis().SetBinLabel(7,"Invariant mass")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        outputFile.cd()
        self.histcount.Write()
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        self.N_totevents += 1
        self.histcount.Fill(0)

        HLT = Object(event, "HLT")
        electrons = Collection(event, "Electron")
        photons = Collection(event, "Photon")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        PuppiMET = Object(event, "PuppiMET")

        if self.runningEra > 3 and not (HLT.IsoMu24 or HLT.Ele30_WPTight_Gsf) :
            return False

        self.histcount.Fill(1)

        N_muonscount = 0
        for muoncount in range(len(muons)) :
            if not muons[muoncount].isGlobal :
                continue
            N_muonscount = N_muonscount + 1
        if N_muonscount < 1 :
            return False
        self.histcount.Fill(2)

        N_elecount = 0
        for elecount in range(len(electrons)) :
            if not electrons[elecount].mvaIso_WP90 :
                continue
            N_elecount = N_elecount + 1
        if N_elecount < 1 :
            return False
        self.histcount.Fill(3)

        mu_4mom  = muons[0].p4()
        ele_4mom = electrons[0].p4()

        if (mu_4mom.Pt() < 10. or ele_4mom.Pt() < 10.) :
            return False
        self.histcount.Fill(4) 

        if (muons[0].mvaMuID_WP < 2 or not electrons[0].mvaIso_WP90) :
            return False
        self.histcount.Fill(5)

        Z_4mom = mu_4mom + ele_4mom

        if (Z_4mom.M() < 60. or Z_4mom.M() > 120.) :
            return False
        self.histcount.Fill(6)

        return True

main_Sequence = [Preselector(myrunningEra),exampleProducer(myrunningEra)]

if not isData :
    main_Sequence.extend([puWeight(myrunningEra)])

p=PostProcessor(".",inputfile,
                    modules=main_Sequence,
                    jsonInput=jsonFile, # path of json file for data
                    haddFileName="tree.root",
                    provenance=False,
                    outputbranchsel="keep_and_drop.txt")
p.run()

print("DONE")
