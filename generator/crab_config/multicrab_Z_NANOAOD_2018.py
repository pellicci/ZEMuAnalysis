from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/NANOAOD_2018'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_2018_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.publication = True

config.Data.outputDatasetTag = 'LFVAnalysis_NANOAOD_10218V1'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Bari'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    from multiprocessing import Process

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    config.General.requestName = 'LFVAnalysis_ZEMu_NANOAOD_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_ZEMu_2018_10218V1/pellicci-LFVAnalysis_MINIAOD_10218V1-54b8060d079e1ece71392c3e505d3426/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZETau_NANOAOD_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_ZETau_2018_10218V1/pellicci-LFVAnalysis_MINIAOD_10218V1-54b8060d079e1ece71392c3e505d3426/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZMuTau_NANOAOD_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_ZMuTau_2018_10218V1/pellicci-LFVAnalysis_MINIAOD_10218V1-54b8060d079e1ece71392c3e505d3426/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HEMu_NANOAOD_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_HEMu_2018_10218V1/pellicci-LFVAnalysis_MINIAOD_10218V1-54b8060d079e1ece71392c3e505d3426/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HETau_NANOAOD_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_HETau_2018_10218V1/pellicci-LFVAnalysis_MINIAOD_10218V1-54b8060d079e1ece71392c3e505d3426/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HMuTau_NANOAOD_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_HMuTau_2018_10218V1/pellicci-LFVAnalysis_MINIAOD_10218V1-54b8060d079e1ece71392c3e505d3426/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
