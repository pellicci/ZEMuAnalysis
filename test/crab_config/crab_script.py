#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from StandardModel.ZEMuAnalysis.runSkimModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *

#inputfile = ['/afs/cern.ch/user/p/pellicci/cernbox/ROOT/ZEMuAnalysis/NANOAOD/191120_10218V1/ZEMuAnalysis_pythia8_NANOAOD_2018_1.root']
#p=PostProcessor(".",inputfile,"",modules=[leptonConstr(),puAutoWeight_2018()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")

p=PostProcessor(".",inputFiles(),modules=[leptonConstr(),puAutoWeight_2018()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
#p=PostProcessor(".",inputFiles(),modules=[leptonConstr()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
p.run()

print "DONE"
