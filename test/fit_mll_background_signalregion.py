import ROOT
import argparse

#Suppress the opening of many Canvas's
ROOT.gROOT.SetBatch(True) 

#Get all the inputs
fBkg = ROOT.TFile("trees/ZEMuAnalysis_Background_Combined.root")
signaltree = fBkg.Get("signaltree")

M_ll = ROOT.RooRealVar("M_ll","M_ll",75.,110.,"GeV")
mcweight = ROOT.RooRealVar("mcweight","mcweight",1.,-100.,100.)
dataset = ROOT.RooDataSet("dataset","dataset",ROOT.RooArgSet(M_ll,mcweight),ROOT.RooFit.Import(signaltree),ROOT.RooFit.WeightVar(mcweight))

#fInput_mumu = ROOT.TFile("histos/latest_production/ZEMuHistos_Data_SameSign_Muon_2018.root")
#histo_mu = fInput_mumu.Get("htemp")
#fInput_elel = ROOT.TFile("histos/latest_production/ZEMuHistos_Data_SameSign_Electron_2018.root")
#histo_el = fInput_elel.Get("htemp")

N_mumu = 29409600.
N_ee = 12157600.

print "Number of events in the fit is ", dataset.sumEntries()
print "The number of mumu events is ", N_mumu
print "The number of ee events is ", N_ee

#Get the signal PDF
fWSSignal = ROOT.TFile("workspaces/morphed_signal_Combined.root")
ws_signal = fWSSignal.Get("ws")

sigPDF = ws_signal.pdf("morph_pdf_binned")

#Background PDF
a_bkg = ROOT.RooRealVar("a_bkg","a_bkg",3.28640,-10.,10.)
b_bkg = ROOT.RooRealVar("b_bkg","b_bkg",-0.290163,-10.,10.)
c_bkg = ROOT.RooRealVar("c_bkg","c_bkg",0.558070,-10.,10.)
d_bkg = ROOT.RooRealVar("d_bkg","d_bkg",0.264009,-10.,10.)

bkgPDF = ROOT.RooBernstein("bkgPDF","Background PDF",M_ll,ROOT.RooArgList(a_bkg,b_bkg,c_bkg,d_bkg))

#Alternate background function
tau_bkg = ROOT.RooRealVar("tau_bkg","tau_bkg",-0.0583634,-5000.,0.)
bkgPDF_exp = ROOT.RooExponential("bkgPDF_exp","bkgPDF_exp",M_ll,tau_bkg)

#Compose the total PDF

br_emu = ROOT.RooRealVar("br_emu","br_emu",0.,-0.00001,0.1)
br_ll = ROOT.RooRealVar("br_ll","br_ll",0.033632)
N_mumu_var = ROOT.RooRealVar("N_mumu_var","N_mumu_var",N_mumu)
N_ee_var = ROOT.RooRealVar("N_ee_var","N_ee_var",N_ee)

br_emu.setConstant(1)

#Add lognormal systematics
eff_nominal   = ROOT.RooRealVar("eff_nominal","eff_nominal",1.)
eff_kappa     = ROOT.RooRealVar("eff_kappa","eff_kappa",1.03)
beta_eff      = ROOT.RooRealVar("beta_eff","beta_eff",0.,-5.,5.)
eff           = ROOT.RooFormulaVar("eff","@0 * pow(@1,@2)",ROOT.RooArgList(eff_nominal,eff_kappa,beta_eff))
global_eff    = ROOT.RooRealVar("global_eff","global_eff",0.,-5.,5.)
one           = ROOT.RooRealVar("one","one",1.)
constrain_eff = ROOT.RooGaussian("constrain_eff","constrain_eff",global_eff,beta_eff,one)
global_eff.setConstant(1)

N_sig = ROOT.RooFormulaVar("N_sig","@0*@4*sqrt((@1*@2)/(@3*@3))",ROOT.RooArgList(br_emu,N_ee_var,N_mumu_var,br_ll,eff))
N_bkg = ROOT.RooRealVar("N_bkg","N_bkg",500.,0.,100000.)

totPDF = ROOT.RooAddPdf("totPDF","totPDF",ROOT.RooArgList(sigPDF,bkgPDF),ROOT.RooArgList(N_sig,N_bkg))

totPDF_constr = ROOT.RooProdPdf("totPDF_constr","totPDF_constr",ROOT.RooArgList(totPDF,constrain_eff))

bkgPDF_exp.fitTo(dataset)

#Fit, plot, etc
totPDF_constr.fitTo(dataset,ROOT.RooFit.Extended(1))

xframe = M_ll.frame()
dataset.plotOn(xframe)
totPDF_constr.plotOn(xframe)
bkgPDF_exp.plotOn(xframe,ROOT.RooFit.LineColor(ROOT.kRed),ROOT.RooFit.LineStyle(ROOT.kDashed))

c1 = ROOT.TCanvas()
xframe.Draw()
c1.SaveAs("plots/latest_production/2016_2017_2018/fit_bkgonly.pdf")

#Save the fit result
fOut = ROOT.TFile("workspaces/fit_Mll_Backgroundonly_Combined.root","RECREATE")
fOut.cd()

bkg_data = bkgPDF.generate(ROOT.RooArgSet(M_ll),N_bkg.getVal())

ws = ROOT.RooWorkspace("ws")
getattr(ws,'import')(totPDF_constr)
getattr(ws,'import')(bkgPDF_exp)
getattr(ws,'import')(bkg_data)

ws.Print()

ws.Write()
fOut.Close()

del ws