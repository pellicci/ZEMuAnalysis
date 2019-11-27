from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = Configuration()

runningEra = 2 # 0 = 2016, 1 = 2017, 2 = 2018

config.section_('General')
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_config/crab_script.sh'
config.JobType.inputFiles = ['crab_config/crab_script.py','../scripts/haddnano.py','cmssw_config/keep_and_drop.txt']
config.JobType.sendPythonFolder	 = True

config.JobType.allowUndistributedCMSSW = True

if runningEra == 0:
    config.General.workArea = 'crab_projects/samples_MC_2016/'
if runningEra == 1:
    config.General.workArea = 'crab_projects/samples_MC_2017/'
if runningEra == 2:
    config.General.workArea = 'crab_projects/samples_MC_2018/'

config.section_('Data')
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False

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

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    #################################################
    #                                               #
    #--------------- Running 2016 MC ---------------#
    #                                               #
    #################################################

    if runningEra == 0:
        config.General.requestName = '2016_ZEMuAnalysis_ttbarToHadronic'
        # config.Data.inputDataset = '/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2016_ZEMuAnalysis_ttbarToSemiLeptonic'
        # config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_ttbarlnu'
        # config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_SingleToptW'
        # config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_SingleAntiToptW'
        # config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2016_ZEMuAnalysis_WJetsToLNu_1'
        # config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_WJetsToLNu_2'
        # config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_DY10to50_1' 
        # config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_DY10to50_2'
        # config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_DY50'
        # config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT100to200'
        # config.Data.inputDataset = '/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT200to300_1'
        # config.Data.inputDataset = '/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT200to300_2'
        # config.Data.inputDataset = '/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join() 
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT300to500_1'
        # config.Data.inputDataset = '/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT300to500_2'
        # config.Data.inputDataset = '/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT500to700_1'
        # config.Data.inputDataset = '/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT500to700_2'
        # config.Data.inputDataset = '/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT700to1000_1'
        # config.Data.inputDataset = '/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT700to1000_2'
        # config.Data.inputDataset = '/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT1000to1500_1'
        # config.Data.inputDataset = '/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT1000to1500_2'
        # config.Data.inputDataset = '/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT1500to2000_1'
        # config.Data.inputDataset = '/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT1500to2000_2'
        # config.Data.inputDataset = '/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT2000toInf_1'
        # config.Data.inputDataset = '/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_QCDHT2000toInf_2'
        # config.Data.inputDataset = '/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_ZZ'
        # config.Data.inputDataset = '/ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_WW'
        # config.Data.inputDataset = '/WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_WZ_1'
        # config.Data.inputDataset = '/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2016_ZEMuAnalysis_WZ_2' 
        # config.Data.inputDataset = '/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

    #################################################
    #                                               #
    #--------------- Running 2017 MC ---------------#
    #                                               #
    #################################################

    if runningEra == 1:

        config.General.requestName = '2017_ZEMuAnalysis_ttbarToHadronic'
        # config.Data.inputDataset = '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2017_ZEMuAnalysis_ttbarToSemiLeptonic'
        # config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2017_ZEMuAnalysis_ttbarlnu'
        # config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2017_ZEMuAnalysis_SingleToptW'
        # config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2017_ZEMuAnalysis_SingleAntiToptW'
        # config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2017_ZEMuAnalysis_DY10to50'
        # config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2017_ZEMuAnalysis_DY50_1'
        # config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2017_ZEMuAnalysis_DY50_2'
        # config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2017_ZEMuAnalysis_QCDHT100to200'
        # config.Data.inputDataset = '/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2017_ZEMuAnalysis_QCDHT200to300'
        # config.Data.inputDataset = '/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join() 
        
        # config.General.requestName = '2017_ZEMuAnalysis_QCDHT300to500'
        # config.Data.inputDataset = '/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2017_ZEMuAnalysis_QCDHT500to700'
        # config.Data.inputDataset = '/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2017_ZEMuAnalysis_QCDHT700to1000'
        # config.Data.inputDataset = '/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2017_ZEMuAnalysis_QCDHT1000to1500'
        # config.Data.inputDataset = '/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2017_ZEMuAnalysis_QCDHT1500to2000'
        # config.Data.inputDataset = '/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

        # config.General.requestName = '2017_ZEMuAnalysis_QCDHT2000toInf'
        # config.Data.inputDataset = '/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2017_ZEMuAnalysis_WW'
        # config.Data.inputDataset = '/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()
        
        # config.General.requestName = '2017_ZEMuAnalysis_WZ' # Non sembra esserci un campione con le giuste condizioni di PU
        # config.Data.inputDataset = '/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' 
        # p = Process(target=submit, args=(config,))
        # p.start()
        # p.join()

    #################################################
    #                                               #
    #--------------- Running 2018 MC ---------------#
    #                                               #
    #################################################


    if runningEra == 2:

        config.General.requestName = '2018_ZEMuAnalysis_ttbarToHadronic'
        config.Data.inputDataset = '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v3/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_ttbarToSemiLeptonic'
        config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_ttbarlnu'
        config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_ttbarZlnu'
        config.Data.inputDataset = '/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_SingleToptW'
        config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2018_ZEMuAnalysis_SingleAntiToptW'
        config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2018_ZEMuAnalysis_DY10to50_1'
        config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_DY10to50_2'
        config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2018_ZEMuAnalysis_DY50_1'
        config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_DY50_2'
        config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_QCDHT100to200'
        config.Data.inputDataset = '/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2018_ZEMuAnalysis_QCDHT200to300'
        config.Data.inputDataset = '/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join() 
        
        config.General.requestName = '2018_ZEMuAnalysis_QCDHT300to500'
        config.Data.inputDataset = '/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2018_ZEMuAnalysis_QCDHT500to700'
        config.Data.inputDataset = '/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_QCDHT700to1000'
        config.Data.inputDataset = '/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_QCDHT1000to1500'
        config.Data.inputDataset = '/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_QCDHT1500to2000'
        config.Data.inputDataset = '/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_WW'
        config.Data.inputDataset = '/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2018_ZEMuAnalysis_WZ'
        config.Data.inputDataset = '/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_ZZ'
        config.Data.inputDataset = '/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
