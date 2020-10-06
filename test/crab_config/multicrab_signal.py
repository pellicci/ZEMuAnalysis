from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_config/crab_script.sh'
config.JobType.inputFiles = ['crab_config/crab_script.py','../scripts/haddnano.py','cmssw_config/keep_and_drop.txt']
config.JobType.sendPythonFolder	 = True

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.publication = False

config.section_('Site')
config.Site.storageSite = 'T2_IT_Legnaro'

if __name__ == '__main__':

    # config.JobType.scriptArgs = ['isData=MC','year=2016']
    # config.General.workArea = 'crab_projects/samples_MC_2016/'
    # config.General.requestName = '2016_ZEMuAnalysis_Signal'
    # config.Data.inputDataset = '/ZEMuAnalysis_2016_8028V1/pellicci-ZEMuAnalysis_NANOAOD_10218V1-b1c578360797952dfc156561d5f36519/USER'
    # crabCommand('submit', config = config)

    # config.JobType.scriptArgs = ['isData=MC','year=2017']
    # config.General.workArea = 'crab_projects/samples_MC_2017/'
    # config.General.requestName = '2017_ZEMuAnalysis_Signal'
    # config.Data.inputDataset = '/ZEMuAnalysis_2017_934V1/pellicci-ZEMuAnalysis_NANOAOD_2017_10218V2-df769e3b6a68f1e897c86e71b2345849/USER'
    # crabCommand('submit', config = config)

    config.JobType.scriptArgs = ['isData=MC','year=2018']
    config.General.workArea = 'crab_projects/samples_MC_2018/'
    config.General.requestName = '2018_ZEMuAnalysis_Signal'
    config.Data.inputDataset = '/ZEMuAnalysis_10218V2/pellicci-ZEMuAnalysis_NANOAOD_10218V1-a7880b551d3b12f0ed185e04212304eb/USER'
    crabCommand('submit', config = config)
