from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/SIM2016'
config.General.requestName = 'LFVAnalysis_ZLL_SIM_2016_8028V1'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['ZEMuAnalysis_pythia8_SIM_2016.root']
config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = 'LFVAnalysis_13TeV_SIM_2016_cfg.py'

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.inputDataset = '/LFVAnalysis_ZLL_2016_949V1_22prodV2/pellicci-LFVAnalysis_ZLL_GEN_2016_949V1_22prodV1-b0985b40a2be5133ec04035ed2cc5477/USER'
config.Data.outputDatasetTag = 'LFVAnalysis_ZLL_SIM_2016_8028V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
