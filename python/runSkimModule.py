import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class exampleProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):

        """process event, return True (go to next module) or False (fail, go to next event)"""
        HLT = Object(event, "HLT")
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")

        if (len(electrons) + len(muons) != 2) :
            return False

        if len(muons) == 2 :
            if ( (muons[0].p4() + muons[1].p4()).M() < 30. or (muons[0].p4() + muons[1].p4()).M() > 150.) :
                return False
        elif len(electrons) == 2 :
            if ( (electrons[0].p4() + electrons[1].p4()).M() < 30. or (electrons[0].p4() + electrons[1].p4()).M() > 150.) :
                return False
        else :
            if ( (muons[0].p4() + electrons[0].p4()).M() < 30. or (muons[0].p4() + electrons[0].p4()).M() > 150.) :
                return False

        if (HLT.IsoMu27 or HLT.Mu50 or HLT.Ele32_WPTight_Gsf or HLT.Ele32_WPTight_Gsf_L1DoubleEG) :
            return True

        return False

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
leptonConstr = lambda : exampleProducer()
