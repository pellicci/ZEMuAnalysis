from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
 
config.section_('General')
config.General.transferLogs = True
config.General.requestName = '2018_ZEMuAnalysis_Signal'
config.General.workArea = 'crab_projects/samples_MC_2018/'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_config/crab_script.sh'
config.JobType.inputFiles = ['crab_config/crab_script.py','../scripts/haddnano.py','cmssw_config/keep_and_drop.txt']
config.JobType.sendPythonFolder	 = True

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDataset = '/ZEMuAnalysis_10218V2/pellicci-ZEMuAnalysis_NANOAOD_10218V1-a7880b551d3b12f0ed185e04212304eb/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False

config.section_('Site')
config.Site.storageSite = 'T2_IT_Legnaro'
#config.Site.storageSite = 'T2_IT_Bari'
