#! /usr/bin/env python
import StandardModel.ZEMuAnalysis.BatchMaster as bm
import os, sys


# -----------------------------
# Specify parameters
# -----------------------------

executable = 'execBatch.sh'
analyzer   = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2016_cfg.py'
stage_dir  = 'batch'
output_dir = '/eos/user/p/pellicci/ZEMuAnalysis/EmbeddedSamples/'

# -----------------------------
# Set job configurations.  
# -----------------------------
samplesDict = {}

nEvtPerJob = 0.05 # faster jobs, # in unit of 1e6 , 5-10 are good settings. 

#################################################
#                                               #
#---------------  Running data   ---------------#
#                                               #
#################################################
# dataset, nEvtPerJobIn1e6, year, isData, suffix

"""
    bm.JobConfig( dataset='/EmbeddingRun2016B/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElMuB_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016C/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElMuC_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016D/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElMuD_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016E/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElMuE_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016F/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElMuF_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016G/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElMuG_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016H/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElMuH_2016',inputDBS="phys03"),

"""

samplesDict['2016'] = [ 
    bm.JobConfig( dataset='/EmbeddingRun2016B/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElTauB_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016C/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElTauC_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016D/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElTauD_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016E/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElTauE_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016F/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElTauF_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016G/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElTauG_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016H/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElTauH_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016B/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedMuTauB_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016C/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedMuTauC_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016D/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedMuTauD_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016E/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedMuTauE_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016F/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedMuTauF_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016G/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedMuTauG_2016',inputDBS="phys03"),
    bm.JobConfig( dataset='/EmbeddingRun2016H/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedMuTauH_2016',inputDBS="phys03")
    ]

# -----------------------------
# submit to batch
# -----------------------------
samplesToSubmit = samplesDict.keys()
samplesToSubmit.sort()
doYears = ["2016", "2017", "2018"]
configs = []

for s in samplesToSubmit :
    if s[:4] in doYears :
        configs += samplesDict[s]

batchMaster = bm.BatchMaster(
    analyzer    = analyzer,
    config_list = configs, 
    stage_dir   = stage_dir,
    output_dir  = output_dir,
    executable  = executable,
)

#ensure there's a symbolic link 'batch' to put the tarball in
if not os.path.exists("batch") :
    os.symlink("/afs/cern.ch/user/p/pellicci/nobackup/batch", "batch")
    print "Created symbolic link to ~/nobackup/batch"

batchMaster.submit_to_batch(doSubmit=True)
