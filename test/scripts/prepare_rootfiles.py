import ROOT
import os, sys
import subprocess
import argparse
from importlib import import_module

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

ROOT.PyConfig.IgnoreCommandLineOptions = True

class HLTElectronFilter(Module):
    def __init__(self):
	self.writeHistFile=True

    def beginJob(self,histFile=None,histDirName=None):
	Module.beginJob(self,histFile,histDirName)

    def analyze(self, event):

        HLT = Object(event, "HLT") 

        if (HLT.IsoMu24 or HLT.IsoMu27 or HLT.Mu50) :
            return False

        return True

class SignalFilter(Module):
    def __init__(self):
        self.writeHistFile=True

    def beginJob(self,histFile=None,histDirName=None):
        Module.beginJob(self,histFile,histDirName)

    def analyze(self, event):

        muons = Collection(event, "Muon")

        if (len(muons) != 1) :
            return False

        return True

#---------------------------------#
p = argparse.ArgumentParser(description='Select whether to download MC or data')
p.add_argument('isData_option', help='Type <<MC>> or <<data>>')
p.add_argument('year_option', help='Type <<2016>>, <<2017>> or <<2018>>')
args = p.parse_args()

# Switch from muon to electron channel
if args.isData_option == "MC":
    isData = False
if args.isData_option == "data":
    isData = True

year = args.year_option
#---------------------------------#

if not os.path.exists("rootfiles"):
    os.makedirs("rootfiles")
if not os.path.exists("rootfiles/latest_production"):
    os.makedirs("rootfiles/latest_production")
if not os.path.exists("rootfiles/latest_production/MC"):
    os.makedirs("rootfiles/latest_production/MC")
if not os.path.exists("rootfiles/latest_production/dataprocess"):
    os.makedirs("rootfiles/latest_production/dataprocess")

print "Processing ", args.isData_option, " for year ", year

if not isData :
    dir_input = "crab_projects/samples_MC_" + year + "/"
    dir_output_bkg = "rootfiles/latest_production/MC/backgrounds/"
    dir_output_sig = "rootfiles/latest_production/MC/signals/"  
else :
    dir_input = "crab_projects/samples_data_" + year + "/"
    dir_output_data = "rootfiles/latest_production/dataprocess/"

list_dirs = os.listdir(dir_input)

if not isData and not os.path.exists(dir_output_bkg):
    os.makedirs(dir_output_bkg)

if not isData and not os.path.exists(dir_output_sig):
    os.makedirs(dir_output_sig)

for dirname in list_dirs:

    print "Processing sample dir " + dirname

    n_jobs_command = "crab status -d " + dir_input + dirname + " | grep status: " + "| awk " + """'{split($0,array,"/") ; print array[2]}'""" + "| sed 's/.$//'"
    n_jobs = int(subprocess.check_output(n_jobs_command, shell=True))

    print "Number of jobs to be retrieved: ", n_jobs

    crab_command = "crab getoutput -d " + dir_input + dirname
    os.system(crab_command)
    
    samplename = dirname.split("crab_" + year + "_ZEMuAnalysis_")

    if "Signal" in dirname:
        hadd_command = "../scripts/haddnano.py " + dir_output_sig + "ZEMuAnalysis_" + samplename[1] + "_" + year + ".root " + dir_input + dirname + "/results/*.root"
    elif isData:
        hadd_command = "../scripts/haddnano.py " + dir_output_data + "ZEMuAnalysis_" + samplename[1] + "_" + year + ".root " + dir_input + dirname + "/results/*.root"
    else:
        hadd_command = "../scripts/haddnano.py " + dir_output_bkg + "ZEMuAnalysis_" + samplename[1] + "_" + year + ".root " + dir_input + dirname + "/results/*.root"

    os.system(hadd_command)

    if not "Signal" in dirname and not isData :
        p_Signal=PostProcessor(".",[dir_output_bkg + "ZEMuAnalysis_" + samplename[1] + "_" + year + ".root "],modules=[SignalFilter()],haddFileName=dir_output_bkg + "ZEMuAnalysis_" + samplename[1] + "_SigRegion_" + year + ".root ")
        p_Signal.run()


# Now treat and merge samples
if isData:
    hadd_command = "../scripts/haddnano.py " + dir_output_data + "ZEMuAnalysis_SingleMu_" + year + ".root " + dir_output_data + "ZEMuAnalysis_SingleMu_?_" + year + ".root"
    rm_command = "rm -rf " + dir_output_data + "ZEMuAnalysis_SingleMu_?_" + year + ".root"

    os.system(hadd_command)
    os.system(rm_command)

    hadd_command = "../scripts/haddnano.py " + dir_output_data + "ZEMuAnalysis_SingleEle_DoubleTrig_" + year + ".root " + dir_output_data + "ZEMuAnalysis_SingleEle_?_" + year + ".root"
    rm_command = "rm -rf " + dir_output_data + "ZEMuAnalysis_SingleEle_?_" + year + ".root"

    os.system(hadd_command)
    os.system(rm_command)

    p_HLT=PostProcessor(".",[dir_output_data + "ZEMuAnalysis_SingleEle_DoubleTrig_" + year + ".root "],modules=[HLTElectronFilter()],haddFileName=dir_output_data + "ZEMuAnalysis_SingleEle_" + year + ".root ")
    p_HLT.run()

    rm_command = "rm -rf " + dir_output_data + "ZEMuAnalysis_SingleEle_DoubleTrig_" + year + ".root "
    os.system(rm_command)

    p_Signal_mu=PostProcessor(".",[dir_output_data + "ZEMuAnalysis_SingleMu_" + year + ".root "],modules=[SignalFilter()],haddFileName=dir_output_data + "ZEMuAnalysis_SingleMu_SigRegion_" + year + ".root ")
    p_Signal_mu.run()

    p_Signal_ele=PostProcessor(".",[dir_output_data + "ZEMuAnalysis_SingleEle_" + year + ".root "],modules=[SignalFilter()],haddFileName=dir_output_data + "ZEMuAnalysis_SingleEle_SigRegion_" + year + ".root ")
    p_Signal_ele.run()

print "All done!"
