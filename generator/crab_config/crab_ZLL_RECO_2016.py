from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/RECO2016'
config.General.requestName = 'LFVAnalysis_ZLL_RECO_2016_8028V1'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['ZEMuAnalysis_pythia8_RECO_2016.root']
config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = 'LFVAnalysis_13TeV_RECO_2016_cfg.py'

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.publication = True
config.Data.inputDataset = '/LFVAnalysis_ZLL_2016_8028V1_22prodV1/pellicci-LFVAnalysis_ZLL_DIGI_2016_8028V1-6868a286d3522be326f21d858c30a51e/USER'
config.Data.outputDatasetTag = 'LFVAnalysis_ZLL_RECO_2016_8028V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
