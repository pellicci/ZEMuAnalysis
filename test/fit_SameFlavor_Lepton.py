import ROOT
import argparse

#Suppress the opening of many Canvas's
ROOT.gROOT.SetBatch(True) 

#---------------------------------#
p = argparse.ArgumentParser(description='Select the year')
p.add_argument('year_option', help='Type <<2016>>, <<2017>> or <<2018>>')
args = p.parse_args()

year = args.year_option

fInput = ROOT.TFile("histos/latest_production/ZEMuHistos_Data_SameSign_Muon_" + year + ".root")
histo = fInput.Get("htemp")

#Define the observable
M_ll = ROOT.RooRealVar("M_ll","#mu#mu invariant mass",110,70.,110.,"GeV")

data = ROOT.RooDataHist("data","data",ROOT.RooArgList(M_ll),histo)

print "Number of events to fit ", data.numEntries()

mean = ROOT.RooRealVar("mean","mean",90.,85.,95.)
width = ROOT.RooRealVar("width","width",2.5,0.1,5.)
sigma = ROOT.RooRealVar("sigma","sigma",2.,0.1,5.)
alpha = ROOT.RooRealVar("alpha","alpha",1.,0.1,10.)
enne = ROOT.RooRealVar("enne","enne",2.,0.1,10.)

mean2 = ROOT.RooRealVar("mean2","mean2",85.,70.,95.)
sigma2 = ROOT.RooRealVar("sigma2","sigma2",2.,0.1,10.)

sigpdf1 = ROOT.RooCBShape("sigpdf1","sigpdf1",M_ll,mean,sigma,alpha,enne)
sigpdf2 = ROOT.RooVoigtian("sigpdf2","sigpdf2",M_ll,mean,sigma2,width)

fracsig = ROOT.RooRealVar("fracsig","fracsig",0.9,0.,1.)

sigpdf = ROOT.RooAddPdf("sigpdf","sigpdf",sigpdf1,sigpdf2,fracsig)

a_bkg = ROOT.RooRealVar("a_bkg","a_bkg",0.1,-10.,10.)
b_bkg = ROOT.RooRealVar("b_bkg","b_bkg",-0.1,-10.,10.)
c_bkg = ROOT.RooRealVar("c_bkg","c_bkg",0.,-5.,5.)

bkgpdf = ROOT.RooBernstein("bkgpdf","Background PDF",M_ll,ROOT.RooArgList(a_bkg,b_bkg))

frac = ROOT.RooRealVar("frac","Signal fraction",0.99,0.,1.)

totpdf = ROOT.RooAddPdf("totpdf","Total PDF",sigpdf,bkgpdf,frac)

sigpdf.fitTo(data)

xframe = M_ll.frame()
data.plotOn(xframe)
sigpdf.plotOn(xframe)

c1 = ROOT.TCanvas()
xframe.Draw()
c1.SaveAs("plots/latest_production/" + year + "/fit_mll_SameSign_Muon.pdf")

fOut = ROOT.TFile("workspaces/fit_Mll_SameSign_Muon_" + year + ".root","RECREATE")
fOut.cd()

ws = ROOT.RooWorkspace("ws")
getattr(ws,'import')(sigpdf)
getattr(ws,'import')(data)

ws.Write()
fOut.Close()

del ws
