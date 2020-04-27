from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/DIGIL1HLT_2016'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'LFVAnalysis_13TeV_DIGIL1HLT_2016_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True

config.Data.outputDatasetTag = 'ZEMuAnalysis_HLT_8028V1'

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


    config.General.requestName = 'LFVAnalysis_ZEMu_DIGIL1HLT_2016_8028V1'
    config.Data.inputDataset = '/LFVAnalysis_ZEMu_2016_8028V1/pellicci-LFVAnalysis_ZEMu_GENSIM_2016_8028V1-de842a36922f7de48bef356ab80dc4aa/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZETau_DIGIL1HLT_2016_8028V1'
    config.Data.inputDataset = '/LFVAnalysis_ZETau_2016_8028V1/pellicci-LFVAnalysis_ZETau_GENSIM_2016_8028V1-00ee0753a3450cec6bb22d521e095a94/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_ZMuTau_DIGIL1HLT_2016_8028V1'
    config.Data.inputDataset = '/LFVAnalysis_ZMuTau_2016_8028V1/pellicci-LFVAnalysis_ZMuTau_GENSIM_2016_8028V1-e5cdd0ccd49d8f6094ea0012b6d726ae/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HEMu_DIGIL1HLT_2016_8028V1'
    config.Data.inputDataset = '/LFVAnalysis_HEMu_2016_8028V1/pellicci-LFVAnalysis_HEMu_GENSIM_2016_8028V1-c106a6fc2888a2c1f55c186c040a2a29/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HETau_DIGIL1HLT_2016_8028V1'
    config.Data.inputDataset = '/LFVAnalysis_HETau_2016_8028V1/pellicci-LFVAnalysis_HETau_GENSIM_2016_8028V1-5a1878009a2efa64bedf5a2b8dc29e8c/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'LFVAnalysis_HMuTau_DIGIL1HLT_2016_8028V1'
    config.Data.inputDataset = '/LFVAnalysis_HMuTau_2016_8028V1/pellicci-LFVAnalysis_HMuTau_GENSIM_2016_8028V1-a479edf73fdccb469a399e9b151b6cce/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
