from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/DIGI2016'
config.General.requestName = 'LFVAnalysis_ZLL_DIGI_2016_8028V1'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['ZEMuAnalysis_pythia8_DIGIL1HLT_2016.root']
config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = 'LFVAnalysis_13TeV_DIGIL1HLT_2016_cfg.py'

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.inputDataset = '/LFVAnalysis_ZLL_2016_8028V1_22prodV1/pellicci-LFVAnalysis_ZLL_GENSIM_2016_8028V1_22prodV1-d4fbf6bb88ea36444a4fe79d15bdc21b/USER'
config.Data.outputDatasetTag = 'LFVAnalysis_ZLL_DIGI_2016_8028V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
