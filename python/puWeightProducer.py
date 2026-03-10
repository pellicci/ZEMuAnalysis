
"""
Compute PU weight using correctionlib, and store in new branches
See example in test/example_puWeight.py for usage.
"""
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from correctionlib import CorrectionSet

import ROOT

ROOT.PyConfig.IgnoreCommandLineOptions = True

class puWeightProducer(Module):
    def __init__(self, json, key, name="puWeight", doSysVar=True) :
        """Add weights.
        Parameters:
            json: full path of json file
            key: key for the table in the file
            name: name of variable to be added 
            doSysVar: add up/dn variations
        """
        self.name = name
        self.nameUp = name+"Up"
        self.nameDn = name+"Dn"
        self.doSysVar = doSysVar

        self.evaluator = CorrectionSet.from_file(json)[key]
    
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch(self.name, "F")
        if self.doSysVar:
            self.out.branch(self.nameUp, "F")
            self.out.branch(self.nameDn, "F")
    
    def analyze(self, event):        
        self.out.fillBranch(self.name, self.evaluator.evaluate(event.Pileup_nTrueInt, "nominal"))
        if self.doSysVar:
            self.out.fillBranch(self.nameUp, self.evaluator.evaluate(event.Pileup_nTrueInt, "up"))
            self.out.fillBranch(self.nameDn, self.evaluator.evaluate(event.Pileup_nTrueInt, "down"))

        return True
    

def puWeight(myRunningEra):
    print("***puWeight: era", myRunningEra)

    if myRunningEra == 0 :
        json = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/LUM/2016postVFP_UL/puWeights.json.gz"
        key = "Collisions16_UltraLegacy_goldenJSON"

    elif myRunningEra == 2 :
        json = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/LUM/2017_UL/puWeights.json.gz"
        key = "Collisions17_UltraLegacy_goldenJSON"

    elif myRunningEra == 3 :
        json = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/LUM/2018_UL/puWeights.json.gz"
        key = "Collisions18_UltraLegacy_goldenJSON"

    elif myRunningEra == 4 : 
        json = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/LUM/2022_Summer22/puWeights.json.gz" # md5sum: 4ace5f732cc3fe8ba2ed816b6f76d60a
        key = "Collisions2022_355100_357900_eraBCD_GoldenJson"

    elif myRunningEra == 5 : 
        json = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/LUM/2022_Summer22EE/puWeights.json.gz" # md5sum: d959ba71b4f10fbe8517bff06f5bd11f  
        key = "Collisions2022_359022_362760_eraEFG_GoldenJson"

    elif myRunningEra == 7 : 
        json = "/cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/2025-12-02/puWeights_BCDEFGHI.json.gz"
        key = "Collisions24_BCDEFGHI_goldenJSON"

    else:
        raise ValueError(f"Era {era} not supported yet")

    return puWeightProducer(json, key)
