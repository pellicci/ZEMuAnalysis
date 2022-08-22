from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/GEN2016'
config.General.requestName = 'LFVAnalysis_ZLL_GENSIM_2016_8028V1'

config.section_('JobType')
config.JobType.pluginName = 'PrivateMC'
config.JobType.outputFiles = ['ZEMuAnalysis_pythia8_GENSIM.root']
config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = 'LFVAnalysis_ZLL_13TeV_GENSIM_2016_cfg.py'

config.section_('Data')
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 30
NJOBS = 8000 #Do not increase: maximum number of jobs per task is 10k
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'LFVAnalysis_ZLL_GENSIM_2016_8028V1_22prodV1'
config.Data.outputPrimaryDataset = 'LFVAnalysis_ZLL_2016_8028V1_22prodV1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'

