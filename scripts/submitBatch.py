#! /usr/bin/env python
import StandardModel.ZEMuAnalysis.BatchMaster as bm
import os, sys


# -----------------------------
# Specify parameters
# -----------------------------

executable = 'execBatch.sh'
analyzer   = 'run_ntuplizer.py'
stage_dir  = 'batch'
output_dir = '/eos/user/p/pellicci/ZEMuAnalysis/skimprocess/'

# -----------------------------
# Set job configurations.  
# -----------------------------
samplesDict = {}

nEvtPerJob = 5 # faster jobs, # in unit of 1e6 , 5-10 are good settings. 

#################################################
#                                               #
#---------------  Running data   ---------------#
#                                               #
#################################################
# dataset, nEvtPerJobIn1e6, year, isData, suffix

samplesDict['2024_MC'] = [
    bm.JobConfig( dataset='/DYto2Mu_Bin-MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=False, suffix='2024_DYJetsToMuMu50_120'),
    bm.JobConfig( dataset='/DYto2E_Bin-MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=False, suffix='2024_DYJetsToEE50_120'),
    bm.JobConfig( dataset='/DYto2Tau_Bin-MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=False, suffix='2024_DYJetsToTauTau50_120')
]

samplesDict['2024_Data'] = [
    bm.JobConfig( dataset='/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon0_C'),
    bm.JobConfig( dataset='/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon1_C'),
    bm.JobConfig( dataset='/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon0_D'),
    bm.JobConfig( dataset='/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon1_D'),
    bm.JobConfig( dataset='/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon0_E'),
    bm.JobConfig( dataset='/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon1_E'),
    bm.JobConfig( dataset='/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon0_F'),
    bm.JobConfig( dataset='/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon1_F'),
    bm.JobConfig( dataset='/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon0_G'),
    bm.JobConfig( dataset='/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon1_G'),
    bm.JobConfig( dataset='/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon0_H'),
    bm.JobConfig( dataset='/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon1_H'),
    bm.JobConfig( dataset='/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon0_I'),
    bm.JobConfig( dataset='/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_Muon1_I'),
    bm.JobConfig( dataset='/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma0_C'),
    bm.JobConfig( dataset='/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma1_C'),
    bm.JobConfig( dataset='/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma0_D'),
    bm.JobConfig( dataset='/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma1_D'),
    bm.JobConfig( dataset='/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma0_E'),
    bm.JobConfig( dataset='/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma1_E'),
    bm.JobConfig( dataset='/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma0_F'),
    bm.JobConfig( dataset='/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma1_F'),
    bm.JobConfig( dataset='/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma0_G'),
    bm.JobConfig( dataset='/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma1_G'),
    bm.JobConfig( dataset='/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma0_H'),
    bm.JobConfig( dataset='/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma1_H'),
    bm.JobConfig( dataset='/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma0_I'),
    bm.JobConfig( dataset='/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD',
            nEvtPerJobIn1e6=nEvtPerJob, year="2024", isData=True, suffix='2024_EGamma1_I')
]


# -----------------------------
# submit to batch
# -----------------------------
samplesToSubmit = samplesDict.keys()
samplesToSubmit = sorted(samplesToSubmit)
doYears = ["2024"]
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
    print("Created symbolic link to ~/nobackup/batch")

batchMaster.submit_to_batch(doSubmit=True)
