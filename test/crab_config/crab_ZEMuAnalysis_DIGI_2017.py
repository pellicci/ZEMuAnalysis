from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
 
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'ZEMuAnalysis_Pythia8_DIGI_2017_1064V1'
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.psetName = 'cmssw_config/ZEMuAnalysis_13TeV_pythia8_DIGIL1_2017_cfg.py'
config.JobType.pluginName = 'Analysis'
#config.JobType.numCores = 8

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDataset = '/ZEMuAnalysis_2017_1064V1/pellicci-ZEMuAnalysis_GENSIM_2017_1064V1-7fb467da351648e1e6651c2a869630cc/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Data.outputDatasetTag = 'ZEMuAnalysis_DIGI_2017_1064V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Legnaro'
