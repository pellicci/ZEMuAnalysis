from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/DIGIL1HLT_2018'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'LFVAnalysis_13TeV_DIGIL1HLT_2018_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 3000

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True

config.Data.outputDatasetTag = 'LFVAnalysis_HLT_10218V2'

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


    config.General.requestName = 'LFVAnalysis_ZEMu_DIGIL1HLT_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_ZEMu_2018_10218V1/pellicci-LFVAnalysis_ZEMu_GENSIM_2018_10218V1-813243de1b8bdb0f63fa0fc76f0f3480/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZETau_DIGIL1HLT_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_ZETau_2018_10218V1/pellicci-LFVAnalysis_ZETau_GENSIM_2018_10218V1-1084b9426a9e1fd2ff92e790f75d1ed0/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZMuTau_DIGIL1HLT_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_ZMuTau_2018_10218V1/pellicci-LFVAnalysis_ZMuTau_GENSIM_2018_10218V1-7db86bc296190924332b060b12a3d274/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HEMu_DIGIL1HLT_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_HEMu_2018_10218V1/pellicci-LFVAnalysis_HEMu_GENSIM_2018_10218V1-3270637bf2355ca6f0dc88ef70b36450/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HETau_DIGIL1HLT_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_HETau_2018_10218V1/pellicci-LFVAnalysis_HETau_GENSIM_2018_10218V1-f5b1a4ddf86cc37e7cad3ae1036054fc/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HMuTau_DIGIL1HLT_2018_10218V1'
    config.Data.inputDataset = '/LFVAnalysis_HMuTau_2018_10218V1/pellicci-LFVAnalysis_HMuTau_GENSIM_2018_10218V1-eaaf173c804813bc74d6dd16415036e7/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
