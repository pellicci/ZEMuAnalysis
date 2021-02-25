from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'LFVAnalysis_ZLL_GENSIM_2016_1064V1'
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.psetName = 'ZLLAnalysis-2016-LHEGEN_cfg.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.outputFiles = ['ZLLAnalysis-2016-LHEGEN.root']
config.JobType.inputFiles = ['Zjets_ll_LFV_tarball.tar.xz']
#config.JobType.numCores = 8

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.outputPrimaryDataset = 'LFVAnalysis_ZLL_2016_1064V1'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 30
NJOBS = 5000 #Do not increase: maximum number of jobs per task is 10k
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'LFVAnalysis_ZLL_GENSIM_2016_1064V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
