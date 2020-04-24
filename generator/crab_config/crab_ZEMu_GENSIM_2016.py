from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'LFVAnalysis_ZEMu_GENSIM_2016_8028V1'
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.psetName = 'LFVAnalysis_ZEMu_13TeV_pythia8_GENSIM_2016_cfg.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.outputFiles = ['ZEMuAnalysis_pythia8_GENSIM_2016.root']
#config.JobType.numCores = 8

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.outputPrimaryDataset = 'LFVAnalysis_ZEMu_2016_8028V1'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5
NJOBS = 8000 #Do not increase: maximum number of jobs per task is 10k
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'LFVAnalysis_ZEMu_GENSIM_2016_8028V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
