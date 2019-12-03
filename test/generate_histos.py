import ROOT
import math
import argparse
from Simplified_Workflow_Handler import Simplified_Workflow_Handler

############################################################################
#                                                                          #
#----------------------- Some bools to be initialized ---------------------#
#                                                                          #
############################################################################
p = argparse.ArgumentParser(description='Select whether to fill the histograms after pre-selection or selection')
p.add_argument('runningEra_option', help='Type <<0>> for 2016, <<1>> for 2017, <<2>> for 2018, <<3>> for combination 2016+2017')
p.add_argument('inputfile_option', help='Provide input file name')
p.add_argument('outputfile_option', help='Provide output file name')
args = p.parse_args()

runningEra = int(args.runningEra_option)
input_filename = args.inputfile_option
output_filename = args.outputfile_option

reducedLoop = True #Only process part of the MC root files (for speeding up)


#-------------------------#
myWF = Simplified_Workflow_Handler(runningEra)

############################################################################
#                                                                          #
#-------------------------- Integrated luminosity -------------------------#
#                                                                          #
############################################################################
#Normalize to this luminsity, in fb-1
if runningEra == 0:
    luminosity_norm = 35.86
if runningEra == 1:
    luminosity_norm = 41.529
    #luminosity_norm = 27.13 #lumi for Ele32_WPTight only
if runningEra == 2:
    luminosity_norm = 59.69

############################################################################
#                                                                          #
#-------------------- Get files and normalization map  --------------------#
#                                                                          #
############################################################################

# Get the files and the names of the samples
sample_name = input_filename.split("_")[2]

#Understand if this is data or MC
isData = False
if "Data" in sample_name:
    isData = True

# Get the normalization
Norm_Map = myWF.get_normalizations_map(runningEra)

############################################################################
#                                                                          #
#------------------------------ Create histos -----------------------------#
#                                                                          #
############################################################################

#Here's the list of histos to plot
h_PUdistrib = ROOT.TH1F("pile up", "pile up",75,0,75)
h_PUdistrib.Sumw2()

##Get the handlers for all the histos and graphics
h_base  = dict()

list_histos = ["h_Mmumu", "h_Mee","h_Mmue", "h_lep1pt", "h_lep2pt", "h_lep1eta", "h_lep2eta", "h_lep1phi", "h_lep2phi", "h_njets25", "h_nbjets25","h_met_sumEt","h_met_pt","h_jetptmax","h_ntau"]

h_base[list_histos[0]]  = ROOT.TH1F(list_histos[0], "M_{#mu#mu}", 60, 50., 120.)
h_base[list_histos[1]]  = ROOT.TH1F(list_histos[1], "M_{ee}", 60, 50., 120.)
h_base[list_histos[2]]  = ROOT.TH1F(list_histos[2], "M_{#mu e}", 50, 50., 120.)
h_base[list_histos[3]]  = ROOT.TH1F(list_histos[3], "p_{T} of the 1st lepton", 50, 20., 100.)
h_base[list_histos[4]]  = ROOT.TH1F(list_histos[4], "p_{T} of the 2nd lepton", 50, 20., 100.)
h_base[list_histos[5]]  = ROOT.TH1F(list_histos[5], "#eta of the 1st lepton", 50, -2.6, 2.6)
h_base[list_histos[6]]  = ROOT.TH1F(list_histos[6], "#eta of the 2nd lepton", 50, -2.6, 2.6)
h_base[list_histos[7]]  = ROOT.TH1F(list_histos[7], "#phi of the 1st lepton", 30, -3.15, 3.15)
h_base[list_histos[8]]  = ROOT.TH1F(list_histos[8], "#phi of the 2nd lepton", 30, -3.15, 3.15)
h_base[list_histos[9]]  = ROOT.TH1F(list_histos[9], "N_{jets} above 25 GeV", 10, 0, 10.)
h_base[list_histos[10]] = ROOT.TH1F(list_histos[10], "N_{bjets} above 25 GeV", 4, 0, 4.)
h_base[list_histos[11]] = ROOT.TH1F(list_histos[11], "MET sumEt puppi", 100, 0., 1000.)
h_base[list_histos[12]] = ROOT.TH1F(list_histos[12], "MET pt puppi", 30, 0., 60.)
h_base[list_histos[13]] = ROOT.TH1F(list_histos[13], "p_{T} of the hardest jet", 50, 25., 150.)
h_base[list_histos[14]] = ROOT.TH1F(list_histos[14], "N_{#tau}", 10, 0., 10.)

##Loop on events
if not isData:
    norm_factor = Norm_Map[sample_name]*luminosity_norm
    print "Norm_Map[", sample_name, "]: ", Norm_Map[sample_name]
    
root_file = ROOT.TFile(input_filename)
mytree = root_file.Get("Events")
print "Processing Sample ", sample_name

Nevts_per_sample   = 0. # Count the number of events in input per each sample processed
Nevts_selected     = 0. # Count the number of events survived per each sample processed
Nevts_expected     = 0. # Number of expected events from weights

nentries = mytree.GetEntriesFast()

print "This sample has ", mytree.GetEntriesFast(), " events"

for jentry in xrange(nentries):
    ientry = mytree.LoadTree( jentry )
    if ientry < 0:
        break
    nb = mytree.GetEntry(jentry )
    if nb <= 0:
        continue

    if nentries > 1000000 and reducedLoop and not isData :
        if jentry > nentries/40.:
            break

    Nevts_per_sample = Nevts_per_sample + 1

    if (Nevts_per_sample/20000.).is_integer() :
        print "Processed ", Nevts_per_sample, " events..."

    nPV = mytree.PV_npvs

    if mytree.nMuon == 2 :

        if not mytree.Muon_tightId[0] :
            continue
        if not mytree.Muon_tightId[1] :
            continue

        if mytree.Muon_pfRelIso03_all[0] > 0.2 : #medium
            continue
        if mytree.Muon_pfRelIso03_all[1] > 0.2 : #medium
            continue

        lep1_pt = mytree.Muon_pt[0]
        lep1_eta = mytree.Muon_eta[0]
        lep1_phi = mytree.Muon_phi[0]
        lep1_mass = mytree.Muon_mass[0]

        lep2_pt = mytree.Muon_pt[1]
        lep2_eta = mytree.Muon_eta[1]
        lep2_phi = mytree.Muon_phi[1]
        lep2_mass = mytree.Muon_mass[1]
    elif mytree.nElectron == 2 :

        lep1_pt = mytree.Electron_pt[0]
        lep1_eta = mytree.Electron_eta[0]
        lep1_phi = mytree.Electron_phi[0]
        lep1_mass = mytree.Electron_mass[0]

        lep2_pt = mytree.Electron_pt[1]
        lep2_eta = mytree.Electron_eta[1]
        lep2_phi = mytree.Electron_phi[1]
        lep2_mass = mytree.Electron_mass[1]
    else :

        if not mytree.Muon_tightId[0] :
            continue
        if mytree.Muon_pfRelIso03_all[0] > 0.2 : #medium
            continue

        lep1_pt = mytree.Muon_pt[0]
        lep1_eta = mytree.Muon_eta[0]
        lep1_phi = mytree.Muon_phi[0]
        lep1_mass = mytree.Muon_mass[0]

        lep2_pt = mytree.Electron_pt[0]
        lep2_eta = mytree.Electron_eta[0]
        lep2_phi = mytree.Electron_phi[0]
        lep2_mass = mytree.Electron_mass[0]

    lep1_FourMom = ROOT.TLorentzVector()
    lep1_FourMom.SetPtEtaPhiM(lep1_pt,lep1_eta,lep1_phi,lep1_mass)
    lep2_FourMom = ROOT.TLorentzVector()
    lep2_FourMom.SetPtEtaPhiM(lep2_pt,lep2_eta,lep2_phi,lep2_mass)

    Zcand_FourMom = lep1_FourMom + lep2_FourMom

    if Zcand_FourMom.M() < 50. :  #FIXWITHNEXTPROD
        continue

    met_sumEt_puppi = mytree.PuppiMET_sumEt
    met_pt_puppi = mytree.PuppiMET_pt

    njets_25 = 0
    nbjets_25 = 0
    jetptmax = -1.
    for jetcount in xrange(mytree.nJet) :
        if mytree.Jet_pt[jetcount] > jetptmax :
            jetptmax = mytree.Jet_pt[jetcount]
        if mytree.Jet_pt[jetcount] > 25. :
            njets_25 = njets_25 + 1
            if mytree.Jet_btagDeepB[jetcount] > 0.4184 :   #medium
                nbjets_25 = nbjets_25 + 1
    
    ntau = 0
    for taucount in xrange(mytree.nTau) :
        if mytree.Tau_pt[taucount] > 20. and mytree.Tau_idMVAoldDM2017v2[taucount] > 15:
            ntau = ntau + 1

    Nevts_selected = Nevts_selected + 1

    ############################################################################
    #                                                                          #
    #--------------------- Determine the total event weight -------------------#
    #                                                                          #
    ############################################################################

    #Lepton scale factors
    if mytree.nMuon == 2 and not isData: # Get muon scale factors, which are different for two groups of datasets, and weight them for the respective integrated lumi 

        isSingleMuTrigger_LOW = mytree.HLT_IsoMu24
        if runningEra == 1:
            isSingleMuTrigger_LOW = mytree.HLT_IsoMu27

        lep1_weight = myWF.get_muon_scale(lep1_pt,lep1_eta,isSingleMuTrigger_LOW,runningEra)
        lep2_weight = myWF.get_muon_scale(lep2_pt,lep2_eta,isSingleMuTrigger_LOW,runningEra)

    ############## ELECTRON SFs ##############
    elif mytree.nElectron == 2 and not isData:
        lep1_weight = myWF.get_ele_scale(lep1_pt, lep1_eta + mytree.Electron_deltaEtaSC[0],runningEra)
        lep2_weight = myWF.get_ele_scale(lep2_pt, lep2_eta + mytree.Electron_deltaEtaSC[1],runningEra)
    elif mytree.nMuon == 1 and not isData:
        isSingleMuTrigger_LOW = mytree.HLT_IsoMu24
        if runningEra == 1:
            isSingleMuTrigger_LOW = mytree.HLT_IsoMu27

        lep1_weight = myWF.get_muon_scale(lep1_pt,lep1_eta,isSingleMuTrigger_LOW,runningEra)
        lep2_weight = myWF.get_ele_scale(lep2_pt, lep2_eta + mytree.Electron_deltaEtaSC[0],runningEra)

    ############### Multiply weights and SFs for MC. Set weight to 1 for data ###############

    if not isData:
        MC_Weight = mytree.genWeight
        PU_Weight = mytree.puWeight # Add Pile Up weight

        Event_Weight = norm_factor*MC_Weight*PU_Weight/math.fabs(MC_Weight) # Just take the sign of the gen weight
        Event_Weight = Event_Weight*lep1_weight*lep2_weight

        if nentries > 1000000 and reducedLoop :
            Event_Weight = Event_Weight*40.
    else:
        Event_Weight = 1.


    # Remove QCD events with abnormal weight
    if "QCD" in sample_name and Event_Weight >= 2000:
        print "QCD event removed!!!"
        continue

    if mytree.nMuon == 1 :
        Nevts_expected += Event_Weight # Increment the number of events survived in the analyzed sample
   
    ############################################################################
    #                                                                          #
    #------------------------------- Fill histos ------------------------------#
    #                                                                          #
    ############################################################################
    if mytree.nMuon == 2 :
        h_base["h_Mmumu"].Fill(Zcand_FourMom.M(),Event_Weight)
    elif mytree.nElectron == 2 :
        h_base["h_Mee"].Fill(Zcand_FourMom.M(),Event_Weight)
    else :
        h_base["h_Mmue"].Fill(Zcand_FourMom.M(),Event_Weight)

        h_base["h_lep1pt"].Fill(lep1_pt,Event_Weight)
        h_base["h_lep1eta"].Fill(lep1_eta,Event_Weight)
        h_base["h_lep1phi"].Fill(lep1_phi,Event_Weight)
        h_base["h_lep2pt"].Fill(lep2_pt,Event_Weight)
        h_base["h_lep2eta"].Fill(lep2_eta,Event_Weight)
        h_base["h_lep2phi"].Fill(lep2_phi,Event_Weight)

        h_base["h_njets25"].Fill(njets_25,Event_Weight)
        h_base["h_nbjets25"].Fill(nbjets_25,Event_Weight)
        h_base["h_jetptmax"].Fill(jetptmax,Event_Weight)

        h_base["h_met_sumEt"].Fill(met_sumEt_puppi,Event_Weight)
        h_base["h_met_pt"].Fill(met_pt_puppi,Event_Weight)

        h_base["h_ntau"].Fill(ntau,Event_Weight)

        h_PUdistrib.Fill(nPV,Event_Weight)      

fOut = ROOT.TFile(output_filename,"RECREATE")
fOut.cd()
for hist_name in list_histos:
    h_base[hist_name].Write()
fOut.Close()

print "Number of expected events for ", luminosity_norm, " in fb-1, for sample " , sample_name
print "Number of events processed = ", Nevts_per_sample
print "Number of events selected = ", Nevts_selected
print "Number of events expected = ", Nevts_expected
print "###################"
print "###################"
