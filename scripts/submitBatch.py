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

nEvtPerJob = 0.1 # faster jobs, # in unit of 1e6 , 5-10 are good settings. 

#################################################
#                                               #
#---------------  Running data   ---------------#
#                                               #
#################################################
# dataset, nEvtPerJobIn1e6, year, isData, suffix

# Single Electron
samplesDict['2016_ElMu'] = [ 
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
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EmbeddedElMuH_2016',inputDBS="phys03")
    ]

#samplesDict['2017_SingleElectron'] = [ 
#    bm.JobConfig( '/SingleElectron/Run2017B-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", True, 'LFVAnalysis_SingleElectronRun2017B_2017'),
#    bm.JobConfig( '/SingleElectron/Run2017C-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", True, 'LFVAnalysis_SingleElectronRun2017C_2017'),
#    bm.JobConfig( '/SingleElectron/Run2017D-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", True, 'LFVAnalysis_SingleElectronRun2017D_2017'),
#    bm.JobConfig( '/SingleElectron/Run2017E-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", True, 'LFVAnalysis_SingleElectronRun2017E_2017'),
#    bm.JobConfig( '/SingleElectron/Run2017F-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", True, 'LFVAnalysis_SingleElectronRun2017F_2017')]


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
