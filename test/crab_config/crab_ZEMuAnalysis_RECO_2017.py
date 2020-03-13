from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
 
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'ZEMuAnalysis_Pythia8_RECO_2017_1064V2'
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.psetName = 'cmssw_config/ZEMuAnalysis_13TeV_pythia8_RAW2DIGIRECO_2017_cfg.py'
config.JobType.pluginName = 'Analysis'

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDataset = '/ZEMuAnalysis_2017_1064V1/pellicci-ZEMuAnalysis_HLT_2017_9414V1-1cba7fad1227c919886864247a60b1e3/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Data.outputDatasetTag = 'ZEMuAnalysis_RECO_2017_1064V2'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
