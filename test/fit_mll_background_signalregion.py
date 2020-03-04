import ROOT
import argparse

#Suppress the opening of many Canvas's
ROOT.gROOT.SetBatch(True) 

#Get all the inputs
fBkg = ROOT.TFile("trees/ZEMuAnalysis_Background_2018.root")
signaltree = fBkg.Get("signaltree")

M_ll = ROOT.RooRealVar("M_ll","M_ll",70.,110.)
mcweight = ROOT.RooRealVar("mcweight","mcweight",1.,-100.,100.)
dataset = ROOT.RooDataSet("dataset","dataset",ROOT.RooArgSet(M_ll,mcweight),ROOT.RooFit.Import(signaltree),ROOT.RooFit.WeightVar(mcweight))

fInput_mumu = ROOT.TFile("histos/latest_production/ZEMuHistos_Data_SameSign_Muon_2018.root")
histo_mu = fInput_mumu.Get("htemp")

fInput_elel = ROOT.TFile("histos/latest_production/ZEMuHistos_Data_SameSign_Electron_2018.root")
histo_el = fInput_elel.Get("htemp")

N_mumu = histo_mu.GetEntries()
N_ee = histo_el.GetEntries()

print "Number of events in the fit is ", dataset.sumEntries()
print "The number of mumu events is ", N_mumu
print "The number of ee events is ", N_ee

#Get the signal PDF
fWSSignal = ROOT.TFile("workspaces/morphed_signal_2018.root")
ws_signal = fWSSignal.Get("ws")

sigPDF = ws_signal.pdf("morph_pdf")

#Background PDF
a_bkg = ROOT.RooRealVar("a_bkg","a_bkg",3.28640,-10.,10.)
b_bkg = ROOT.RooRealVar("b_bkg","b_bkg",-0.290163,-10.,10.)
c_bkg = ROOT.RooRealVar("c_bkg","c_bkg",0.558070,-10.,10.)
d_bkg = ROOT.RooRealVar("d_bkg","d_bkg",0.264009,-10.,10.)

bkgPDF = ROOT.RooBernstein("bkgPDF","Background PDF",M_ll,ROOT.RooArgList(a_bkg,b_bkg,c_bkg,d_bkg))

#Compose the total PDF

br_emu = ROOT.RooRealVar("br_emu","br_emu",0.00000001,-0.000001,1.)
br_ll = ROOT.RooRealVar("br_ll","br_ll",0.033632)
N_mumu_var = ROOT.RooRealVar("N_mumu_var","N_mumu_var",N_mumu)
N_ee_var = ROOT.RooRealVar("N_ee_var","N_ee_var",N_ee)

N_sig = ROOT.RooFormulaVar("N_sig","@0*sqrt((@1*@2)/(@3*@3))",ROOT.RooArgList(br_emu,N_ee_var,N_mumu_var,br_ll))
N_bkg = ROOT.RooRealVar("N_bkg","N_bkg",500.,0.,100000.)

totPDF = ROOT.RooAddPdf("totPDF","totPDF",ROOT.RooArgList(sigPDF,bkgPDF),ROOT.RooArgList(N_sig,N_bkg))

#br_emu.setConstant(1)

#Fit, plot, etc
totPDF.fitTo(dataset,ROOT.RooFit.Extended(1))

xframe = M_ll.frame()
dataset.plotOn(xframe)
totPDF.plotOn(xframe)

c1 = ROOT.TCanvas()
xframe.Draw()
c1.SaveAs("plots/latest_production/2016_2017_2018/fit_bkgonly.pdf")

#Save the fit result
fOut = ROOT.TFile("workspaces/fit_Mll_Backgroundonly_2018.root","RECREATE")
fOut.cd()

bkg_data = bkgPDF.generate(ROOT.RooArgSet(M_ll),N_bkg.getVal())

ws = ROOT.RooWorkspace("ws")
getattr(ws,'import')(totPDF)
getattr(ws,'import')(bkg_data)

ws.Print()

ws.Write()
fOut.Close()

del ws