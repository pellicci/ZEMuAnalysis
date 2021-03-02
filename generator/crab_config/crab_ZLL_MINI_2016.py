from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'LFVAnalysis_ZLL_MINI_2016_10612V1'
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.psetName = 'ZLLAnalysis-2016-MINI_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['ZLLAnalysis-2016-MINI.root']
#config.JobType.numCores = 8

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/LFVAnalysis_ZLL_2016_1064V3/pellicci-LFVAnalysis_ZLL_RECO_2016_10612V1-16bbdce99b36d01efc024a410036b013/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.outputDatasetTag = 'LFVAnalysis_ZLL_MINI_2016_10612V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
