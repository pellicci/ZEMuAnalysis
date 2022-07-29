from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/Embedded_NANOAOD_2017'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2017_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 25
config.Data.publication = True

config.section_('Site')
config.Site.storageSite = 'T2_IT_Legnaro'

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


    # config.Data.outputDatasetTag = 'EmbeddedElMu_NANOAOD_10222V1'

    # config.General.requestName = 'ElMu_NANOAOD_2017B_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017B/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElMu_NANOAOD_2017C_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017C/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElMu_NANOAOD_2017D_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017D/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElMu_NANOAOD_2017E_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017E/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElMu_NANOAOD_2017F_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017F/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.Data.outputDatasetTag = 'EmbeddedElTau_NANOAOD_10222V1'

    # config.General.requestName = 'ElTau_NANOAOD_2017B_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017B/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElTau_NANOAOD_2017C_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017C/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElTau_NANOAOD_2017D_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017D/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElTau_NANOAOD_2017E_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017E/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElTau_NANOAOD_2017F_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017F/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.Data.outputDatasetTag = 'EmbeddedMuTau_NANOAOD_10222V1'

    # config.General.requestName = 'MuTau_NANOAOD_2017B_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017B/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'MuTau_NANOAOD_2017C_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017C/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'MuTau_NANOAOD_2017D_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017D/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'MuTau_NANOAOD_2017E_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017E/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'MuTau_NANOAOD_2017F_949V1'
    # config.Data.inputDataset = '/EmbeddingRun2017F/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    config.Data.outputDatasetTag = 'EmbeddedMuMu_NANOAOD_10222V1'

    config.General.requestName = 'MuMu_NANOAOD_2017B_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017B/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2017C_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017C/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2017D_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017D/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2017E_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017E/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2017F_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017F/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.Data.outputDatasetTag = 'EmbeddedElEl_NANOAOD_10222V1'

    config.General.requestName = 'ElEl_NANOAOD_2017B_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017B/ElectronEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2017C_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017C/ElectronEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2017D_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017D/ElectronEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2017E_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017E/ElectronEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2017F_949V1'
    config.Data.inputDataset = '/EmbeddingRun2017F/ElectronEmbedding-inputDoubleMu_94X_miniAOD-v2/USER'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
    