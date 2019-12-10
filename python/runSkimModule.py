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
        jets = Collection(event, "Jet")
        PuppiMET = Object(event, "PuppiMET")

        if PuppiMET.pt > 45. :
            return False

        if not (HLT.IsoMu24 or HLT.IsoMu27 or HLT.Mu50 or HLT.Ele32_WPTight_Gsf or HLT.Ele32_WPTight_Gsf_L1DoubleEG) :
            return False

        if (len(electrons) + len(muons) != 2) :
            return False

        if len(muons) == 2 :
            lep_mass = (muons[0].p4() + muons[1].p4()).M() 
            if (lep_mass < 70. or lep_mass > 120.) :
                return False
            if ( muons[0].charge * muons[1].charge > 0 ) :
                return False
            if not muons[0].tightId :
                return False
            if not muons[1].tightId :
                return False
            if muons[0].pfRelIso03_all > 0.2 or muons[1].pfRelIso03_all > 0.2 : #medium
                return False
            if muons[0].pt < 25. or muons[1].pt < 25. :
                return False

        elif len(electrons) == 2 :
            lep_mass = (electrons[0].p4() + electrons[1].p4()).M()
            if (lep_mass < 70. or lep_mass > 120.) :
                return False
            if ( electrons[0].charge * electrons[1].charge > 0 ) :
                return False
            if not electrons[0].mvaFall17V2Iso_WP80 :
                return False
            if not electrons[1].mvaFall17V2Iso_WP80 :
                return False
            if electrons[0].pt < 25. or electrons[1].pt < 25. :
                return False
        else :
            lep_mass = (muons[0].p4() + electrons[0].p4()).M()
            if (lep_mass < 70. or lep_mass > 120.) :
                return False
            if ( muons[0].charge * electrons[0].charge > 0 ) :
                return False
            if not muons[0].tightId :
                return False
            if muons[0].pfRelIso03_all > 0.2 : #medium
                return False
            if not electrons[0].mvaFall17V2Iso_WP80 :
                return False
            if muons[0].pt < 25. or electrons[0].pt < 25. :
                return False

        nbjets_25 = 0
        jetptmax = -1.
        for jetcount in xrange(len(jets)) :
            pt_of_jet = jets[jetcount].pt
            if pt_of_jet > jetptmax :
                jetptmax = pt_of_jet
            if pt_of_jet > 25. and jets[jetcount].btagDeepB > 0.4184 :   #medium
                nbjets_25 = nbjets_25 + 1
        if nbjets_25 > 0 or jetptmax > 100.:
            return False

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
leptonConstr = lambda : exampleProducer()
