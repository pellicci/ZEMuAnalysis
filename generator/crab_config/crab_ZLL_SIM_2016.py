from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'LFVAnalysis_ZLL_SIM_2016_10612V1'
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.psetName = 'ZLLAnalysis-2016-SIM_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['ZLLAnalysis-2016-SIM.root']
#config.JobType.numCores = 8

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/LFVAnalysis_ZLL_2016_1064V3/pellicci-LFVAnalysis_ZLL_GENSIM_2016_1064V3-08dff76b1be5a0e459f30c611dc90d10/USER'
config.Data.splitting = 'Automatic'
#config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.outputDatasetTag = 'LFVAnalysis_ZLL_SIM_2016_10612V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
