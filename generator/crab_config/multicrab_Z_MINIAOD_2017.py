from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/MINIAOD_2017'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'LFVAnalysis_13TeV_MINIAOD_2017_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 3000

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.publication = True

config.Data.outputDatasetTag = 'LFVAnalysis_MINIAOD_947V2'

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


    config.General.requestName = 'LFVAnalysis_ZEMu_MINIAOD_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_ZEMu_2017_934V2/pellicci-LFVAnalysis_RECO_947V2-fcfc615a65be9fb627e3afc83a7469ff/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZETau_MINIAOD_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_ZETau_2017_934V2/pellicci-LFVAnalysis_RECO_947V2-fcfc615a65be9fb627e3afc83a7469ff/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZMuTau_MINIAOD_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_ZMuTau_2017_934V2/pellicci-LFVAnalysis_RECO_947V2-fcfc615a65be9fb627e3afc83a7469ff/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HEMu_MINIAOD_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_HEMu_2017_934V2/pellicci-LFVAnalysis_RECO_947V2-fcfc615a65be9fb627e3afc83a7469ff/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HETau_MINIAOD_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_HETau_2017_934V2/pellicci-LFVAnalysis_RECO_947V2-fcfc615a65be9fb627e3afc83a7469ff/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HMuTau_MINIAOD_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_HMuTau_2017_934V2/pellicci-LFVAnalysis_RECO_947V2-fcfc615a65be9fb627e3afc83a7469ff/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
