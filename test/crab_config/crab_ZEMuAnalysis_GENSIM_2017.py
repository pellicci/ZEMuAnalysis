from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'ZEMuAnalysis_Pythia8_GENSIM_2017_1064V3'
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.psetName = 'cmssw_config/ZEMuAnalysis_13TeV_pythia8_GENSIM_2017_cfg.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.outputFiles = ['ZEMuAnalysis_pythia8_GENSIM_2017.root']
config.JobType.numCores = 8

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.outputPrimaryDataset = 'ZEMuAnalysis_2017_1064V3'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2
NJOBS = 9000 #Do not increase: maximum number of jobs per task is 10k, use 8k usually
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'ZEMuAnalysis_GENSIM_2017_1064V3'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
