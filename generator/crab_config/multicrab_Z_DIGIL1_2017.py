from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/DIGIL1_2017'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'LFVAnalysis_13TeV_DIGIL1_2017_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 3000

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True

config.Data.outputDatasetTag = 'LFVAnalysis_DIGIL1_947V2'

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


    config.General.requestName = 'LFVAnalysis_ZEMu_DIGIL1_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_ZEMu_2017_934V2/pellicci-LFVAnalysis_ZEMu_GENSIM_2017_934V2-5aa9fe4d49310aff7870397291f14924/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZETau_DIGIL1_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_ZETau_2017_934V2/pellicci-LFVAnalysis_ZETau_GENSIM_2017_934V2-3317719afd59f4d8f39a7e620d1f844c/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZMuTau_DIGIL1_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_ZMuTau_2017_934V2/pellicci-LFVAnalysis_ZMuTau_GENSIM_2017_934V2-29019737357bb43a3045af16e2458d8b/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HEMu_DIGIL1_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_HEMu_2017_934V2/pellicci-LFVAnalysis_HEMu_GENSIM_2017_934V2-ad46334b1116a0a5f625b1630baccb6c/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HETau_DIGIL1_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_HETau_2017_934V2/pellicci-LFVAnalysis_HETau_GENSIM_2017_934V2-bc7c7b2b890c08161474567515a106f4/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HMuTau_DIGIL1_2017_947V2'
    config.Data.inputDataset = '/LFVAnalysis_HMuTau_2017_934V2/pellicci-LFVAnalysis_HMuTau_GENSIM_2017_934V2-6963f2b84e44766023407599d8205d4b/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
