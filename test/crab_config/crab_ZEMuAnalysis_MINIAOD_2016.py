from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
 
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'ZEMuAnalysis_Pythia8_MINIAOD_9415V1'
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.psetName = 'cmssw_config/ZEMuAnalysis_13TeV_pythia8_MINIAOD_2016_cfg.py'
config.JobType.pluginName = 'Analysis'

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDataset = '/ZEMuAnalysis_2016_8028V1/pellicci-ZEMuAnalysis_RECO_8028V1-69ab4ab0f87b34f1d1a65fba636b0a8c/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Data.outputDatasetTag = 'ZEMuAnalysis_MINIAOD_9415V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
