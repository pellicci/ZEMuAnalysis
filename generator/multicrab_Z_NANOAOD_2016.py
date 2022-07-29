from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/Embedded_NANOAOD_2016'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2016_cfg.py'
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


    config.Data.outputDatasetTag = 'EmbeddedElMu_NANOAOD_10222V2'

    config.General.requestName = 'ElMu_NANOAOD_2016B_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016B/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElMu_NANOAOD_2016C_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016C/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElMu_NANOAOD_2016D_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016D/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElMu_NANOAOD_2016E_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016E/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElMu_NANOAOD_2016F_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016F/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElMu_NANOAOD_2016G_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016G/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElMu_NANOAOD_2016H_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016H/ElMuFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.Data.outputDatasetTag = 'EmbeddedElTau_NANOAOD_10222V2'

    config.General.requestName = 'ElTau_NANOAOD_2016B_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016B/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElTau_NANOAOD_2016C_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016C/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElTau_NANOAOD_2016D_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016D/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElTau_NANOAOD_2016E_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016E/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElTau_NANOAOD_2016F_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016F/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElTau_NANOAOD_2016G_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016G/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElTau_NANOAOD_2016H_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016H/ElTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.Data.outputDatasetTag = 'EmbeddedMuTau_NANOAOD_10222V2'

    config.General.requestName = 'MuTau_NANOAOD_2016B_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016B/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuTau_NANOAOD_2016C_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016C/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuTau_NANOAOD_2016D_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016D/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuTau_NANOAOD_2016E_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016E/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuTau_NANOAOD_2016F_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016F/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuTau_NANOAOD_2016G_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016G/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuTau_NANOAOD_2016H_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016H/MuTauFinalState-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.Data.outputDatasetTag = 'EmbeddedMuMu_NANOAOD_10222V2'

    config.General.requestName = 'MuMu_NANOAOD_2016B_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016B/MuonEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2016C_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016C/MuonEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2016D_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016D/MuonEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2016E_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016E/MuonEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2016F_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016F/MuonEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2016G_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016G/MuonEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'MuMu_NANOAOD_2016H_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016H/MuonEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.Data.outputDatasetTag = 'EmbeddedElEl_NANOAOD_10222V2'

    config.General.requestName = 'ElEl_NANOAOD_2016B_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016B/ElectronEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2016C_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016C/ElectronEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2016D_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016D/ElectronEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2016E_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016E/ElectronEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2016F_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016F/ElectronEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2016G_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016G/ElectronEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'ElEl_NANOAOD_2016H_949V1'
    config.Data.inputDataset = '/EmbeddingRun2016H/ElectronEmbedding-inputDoubleMu_94X_Legacy_miniAOD-v5/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
