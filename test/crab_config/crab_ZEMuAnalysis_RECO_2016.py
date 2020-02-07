from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
 
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'ZEMuAnalysis_Pythia8_RECO_8028V1'
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.psetName = 'cmssw_config/ZEMuAnalysis_13TeV_pythia8_RAW2DIGIRECO_2016_cfg.py'
config.JobType.pluginName = 'Analysis'

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDataset = '/ZEMuAnalysis_2016_8028V1/pellicci-ZEMuAnalysis_HLT_8028V1-6868a286d3522be326f21d858c30a51e/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Data.outputDatasetTag = 'ZEMuAnalysis_RECO_8028V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
