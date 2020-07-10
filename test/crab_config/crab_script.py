#!/usr/bin/env python
import os
import sys

# Take input parameters
isData = False
if sys.argv[2].split('=')[1] == "data":
    isData = True

year = sys.argv[3].split('=')[1]

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from StandardModel.ZEMuAnalysis.runSkimModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *

#inputfile = ['/afs/cern.ch/user/p/pellicci/work/ZEMuAnalysis/CMSSW_10_2_18/src/StandardModel/ZEMuAnalysis/test/ZEMuAnalysis_pythia8_NANOAOD_2017.root']
#p=PostProcessor(".",inputfile,"",modules=[leptonConstr(1),puAutoWeight_2017()],provenance=True,fwkJobReport=True,outputbranchsel="cmssw_config/keep_and_drop.txt")

if isData :
    if year == "2016" :
        p=PostProcessor(".",inputFiles(),modules=[leptonConstr(0)],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
    elif year == "2017" :
        p=PostProcessor(".",inputFiles(),modules=[leptonConstr(1)],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
    elif year == "2018" :
        p=PostProcessor(".",inputFiles(),modules=[leptonConstr(2)],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
else :
    if year == "2016" :
        p=PostProcessor(".",inputFiles(),modules=[leptonConstr(0),puAutoWeight_2016()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
    elif year == "2017" :
        p=PostProcessor(".",inputFiles(),modules=[leptonConstr(1),puAutoWeight_2017()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
    elif year == "2018" :
        p=PostProcessor(".",inputFiles(),modules=[leptonConstr(2),puAutoWeight_2018()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")

p.run()

print "DONE"
