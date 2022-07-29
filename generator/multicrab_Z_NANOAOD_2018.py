from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/Embedded_NANOAOD_2018'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'phys03'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 50
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


    config.Data.outputDatasetTag = 'EmbeddedElMu_NANOAOD_2018_10222V1'
    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018ABC_cfg.py'

    # config.General.requestName = 'ElMu_NANOAOD_2018A_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018A/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElMu_NANOAOD_2018B_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018B/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElMu_NANOAOD_2018C_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018C/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018D_cfg.py'

    config.General.requestName = 'ElMu_NANOAOD_2018D_10222V1'
    config.Data.inputDataset = '/EmbeddingRun2018D/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.Data.outputDatasetTag = 'EmbeddedElTau_NANOAOD_2018_10222V1'
    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018ABC_cfg.py'

    # config.General.requestName = 'ElTau_NANOAOD_2018A_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018A/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElTau_NANOAOD_2018B_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018B/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElTau_NANOAOD_2018C_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018C/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018D_cfg.py'

    config.General.requestName = 'ElTau_NANOAOD_2018D_10222V1'
    config.Data.inputDataset = '/EmbeddingRun2018D/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()


    config.Data.outputDatasetTag = 'EmbeddedMuTau_NANOAOD_2018_10222V1'
    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018ABC_cfg.py'

    # config.General.requestName = 'MuTau_NANOAOD_2018A_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018A/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'MuTau_NANOAOD_2018B_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018B/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'MuTau_NANOAOD_2018C_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018C/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018D_cfg.py'

    config.General.requestName = 'MuTau_NANOAOD_2018D_10222V1'
    config.Data.inputDataset = '/EmbeddingRun2018D/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()


    config.Data.outputDatasetTag = 'EmbeddedMuMu_NANOAOD_2018_10222V1'
    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018ABC_cfg.py'

    # config.General.requestName = 'MuMu_NANOAOD_2018A_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018A/MuonEmbedding-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'MuMu_NANOAOD_2018B_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018B/MuonEmbedding-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'MuMu_NANOAOD_2018C_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018C/MuonEmbedding-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018D_cfg.py'

    config.General.requestName = 'MuMu_NANOAOD_2018D_10222V1'
    config.Data.inputDataset = '/EmbeddingRun2018D/MuonEmbedding-inputDoubleMu_102X_miniAOD-v1/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()


    config.Data.outputDatasetTag = 'EmbeddedElEl_NANOAOD_2018_10222V1'
    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018ABC_cfg.py'

    config.General.requestName = 'ElEl_NANOAOD_2018A_10222V1'
    config.Data.inputDataset = '/EmbeddingRun2018A/ElectronEmbedding-inputDoubleMu_102X_miniAOD-v1/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    # config.General.requestName = 'ElEl_NANOAOD_2018B_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018B/ElectronEmbedding-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    # config.General.requestName = 'ElEl_NANOAOD_2018C_10222V1'
    # config.Data.inputDataset = '/EmbeddingRun2018C/ElectronEmbedding-inputDoubleMu_102X_miniAOD-v1/USER'

    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

    config.JobType.psetName = 'LFVAnalysis_13TeV_NANOAOD_Embedded_2018D_cfg.py'

    config.General.requestName = 'ElEl_NANOAOD_2018D_10222V1'
    config.Data.inputDataset = '/EmbeddingRun2018D/ElectronEmbedding-inputDoubleMu_102X_miniAOD-v1/USER'

    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
