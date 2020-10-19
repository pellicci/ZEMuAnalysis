from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/RECO_2017'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'LFVAnalysis_13TeV_RECO_2017_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 3000

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True

config.Data.outputDatasetTag = 'LFVAnalysis_RECO_947V1'

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


    config.General.requestName = 'LFVAnalysis_ZEMu_RECO_2017_947V1'
    config.Data.inputDataset = '/LFVAnalysis_ZEMu_2017_934V1/pellicci-LFVAnalysis_HLT_947V1-2db75fb0f9c961a26a4b88327c2a04d4/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZETau_RECO_2017_947V1'
    config.Data.inputDataset = '/LFVAnalysis_ZETau_2017_934V1/pellicci-LFVAnalysis_HLT_947V1-2db75fb0f9c961a26a4b88327c2a04d4/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZMuTau_RECO_2017_947V1'
    config.Data.inputDataset = '/LFVAnalysis_ZMuTau_2017_934V1/pellicci-LFVAnalysis_HLT_947V1-2db75fb0f9c961a26a4b88327c2a04d4/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HEMu_RECO_2017_947V1'
    config.Data.inputDataset = '/LFVAnalysis_HEMu_2017_934V1/pellicci-LFVAnalysis_HLT_947V1-2db75fb0f9c961a26a4b88327c2a04d4/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HETau_RECO_2017_947V1'
    config.Data.inputDataset = '/LFVAnalysis_HETau_2017_934V1/pellicci-LFVAnalysis_HLT_947V1-2db75fb0f9c961a26a4b88327c2a04d4/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HMuTau_RECO_2017_947V1'
    config.Data.inputDataset = '/LFVAnalysis_HMuTau_2017_934V1/pellicci-LFVAnalysis_HLT_947V1-2db75fb0f9c961a26a4b88327c2a04d4/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
