from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = Configuration()
 
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs=True
config.General.requestName = 'ZEMuAnalysis_Signal'
config.General.workArea = 'crab_projects/Signal'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_config/crab_script.sh'
config.JobType.inputFiles = ['crab_config/crab_script.py','../scripts/haddnano.py','cmssw_config/keep_and_drop.txt']
config.JobType.sendPythonFolder	 = True

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDataset = '/ZEMuAnalysis_GENSIM_10218/pellicci-ZEMuAnalysis_NANOAOD_10218V2-a7880b551d3b12f0ed185e04212304eb/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'Automatic'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'
