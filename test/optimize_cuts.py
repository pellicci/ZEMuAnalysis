import numpy as np
import math
import ROOT

#Supress the opening of many Canvas's
ROOT.gROOT.SetBatch(True) 

#Get the trees
fSignal = ROOT.TFile("trees/ZEMuAnalysis_Signal_2018.root")
tree_signal = fSignal.Get("signaltree")

fBackground = ROOT.TFile("trees/ZEMuAnalysis_Background_2018.root")
tree_background = fBackground.Get("signaltree")

#Number of steps for optimization and var limits
N_cuts = 20
var_min = 33.
var_max = 45.

#Initialize the counters
N_sig_pass = [0.0 for x in xrange(N_cuts)]
N_bkg_pass = [0.0 for x in xrange(N_cuts)]

#Loop over signal and count the events passing the cut
nentries_sig = tree_signal.GetEntriesFast()
print "Signal sample has ", tree_signal.GetEntriesFast(), " events"

for jentry in xrange(nentries_sig):
    ientry = tree_signal.LoadTree( jentry )
    if ientry < 0:
        break
    nb = tree_signal.GetEntry(jentry )
    if nb <= 0:
        continue
    
    if tree_signal.M_ll < 85. or tree_signal.M_ll > 95. :
        continue

    if tree_signal.jetptmax > 65.:
        continue 

    if tree_signal.met > 27.:
        continue 

    var1 = tree_signal.lep2pt
    weight = tree_signal.mcweight

    for i in xrange(N_cuts) :
        cut_val = var_min + i*(var_max - var_min)/N_cuts

        if var1 > cut_val :
            N_sig_pass[i] += weight

#Loop over background and count the events passing the cut
nentries_bkg = tree_background.GetEntriesFast()
print "Background sample has ", tree_background.GetEntriesFast(), " events"

for jentry in xrange(nentries_bkg):
    ientry = tree_background.LoadTree( jentry )
    if ientry < 0:
        break
    nb = tree_background.GetEntry(jentry )
    if nb <= 0:
        continue

    if tree_background.M_ll < 85. or tree_background.M_ll > 95. :
        continue

    if tree_background.jetptmax > 65. :
        continue
    
    if tree_background.met > 27. :
        continue

    var1 = tree_background.lep2pt
    weight = tree_background.mcweight

    for i in xrange(N_cuts) :
        cut_val = var_min + i*(var_max - var_min)/N_cuts

        if var1 > cut_val :
            N_bkg_pass[i] += weight

#Now calculate the significance
cut_xaxis = []
significance = []
signif_error = []
for i in xrange(N_cuts) :
    cut_xaxis.append(var_min + i*(var_max - var_min)/N_cuts)
    significance.append(N_sig_pass[i]/math.sqrt(N_bkg_pass[i]))

max_signif = max(significance)
iter_max = significance.index(max_signif)

print "The maximum value for the significance corresponds to a cut of ", var_min + iter_max*(var_max-var_min)/N_cuts


#Now do the graph
xvalue_array = np.array(cut_xaxis)
yvalue_array = np.array(significance)

sign_graph = ROOT.TGraph(N_cuts,xvalue_array,yvalue_array)

c1 = ROOT.TCanvas("c1","c1",800,500)
c1.cd()
sign_graph.SetMarkerStyle(20)
sign_graph.Draw("AP")

c1.SaveAs("cut_significance.pdf")


upperlimit = []
for i in xrange(N_cuts) :
    ws = ROOT.RooWorkspace()

    sig = ROOT.RooRealVar("sig","sig",1.,0.,200.)
    sig_eff = ROOT.RooRealVar("sig_eff","sig_eff",N_sig_pass[i]/max(N_sig_pass))
    b = ROOT.RooRealVar("b","b",N_bkg_pass[i])
    b_eff = ROOT.RooRealVar("b_eff","b_eff",1.)
    obs = ROOT.RooRealVar("obs","obs",N_bkg_pass[i],0.,5000.)
    poi_list = ROOT.RooArgSet(sig)
    obs_list = ROOT.RooArgSet(obs)

    getattr(ws,'import')(sig)
    getattr(ws,'import')(sig_eff)
    getattr(ws,'import')(b)
    getattr(ws,'import')(b_eff)
    getattr(ws,'import')(obs)

    data = ROOT.RooDataSet("data","data",obs_list)
    data.add(obs_list)

    getattr(ws,'import')(data)

    ws.factory("Poisson::countingModel(obs, sum(sig*sig_eff,b*b_eff))")

    #ws.Print()

    model = ROOT.RooStats.ModelConfig(ws)
    model.SetPdf("countingModel")
    model.SetParametersOfInterest(poi_list)
    model.SetObservables(obs_list)
    model.SetName("S+B Model")

    """
    bModel = model.Clone()
    bModel.SetName("B model")
    oldval = poi_list.find("sig").getVal()
    poi_list.find("sig").setVal(0) #BEWARE that the range of the POI has to contain zero!
    bModel.SetSnapshot(poi_list)
    poi_list.find("sig").setVal(oldval)


    fc = ROOT.RooStats.FeldmanCousins(data,model)
    fc.UseAdaptiveSampling(1)
    fc.FluctuateNumDataEntries(0)
    fc.SetNBins(100)

    fc.SetTestSize(.1)
    fcint = fc.GetInterval()
    limit = fcint.UpperLimit(sig)

    plc = ROOT.RooStats.ProfileLikelihoodCalculator(data,model)
    plc.SetTestSize(0.1)

    interval = plc.GetInterval()
    limit = interval.UpperLimit(sig)
    """

    bc = ROOT.RooStats.BayesianCalculator(data, model)
    bc.SetConfidenceLevel(0.9)
    bc.SetLeftSideTailFraction(0.) #for upper limit
    interval = bc.GetInterval()
    limit = interval.UpperLimit()

    print sig.getVal(), sig_eff.getVal(), N_bkg_pass[i]
    print "This UL is ", limit

    upperlimit.append(limit)

min_UL = min(upperlimit)
iter_min = upperlimit.index(min_UL)

print "The value that optimizes the UL is ", var_min + iter_min*(var_max-var_min)/N_cuts

#Now do the graph
xvalue_array = np.array(cut_xaxis)
yvalue_array = np.array(upperlimit)

limit_graph = ROOT.TGraph(N_cuts,xvalue_array,yvalue_array)
limit_graph.GetYaxis().SetTitle("Arbitrary units")
limit_graph.GetXaxis().SetTitle("MET [GeV]")

c2 = ROOT.TCanvas("c2","c2",800,500)
c2.cd()
limit_graph.SetMarkerStyle(20)
limit_graph.Draw("AP")

c2.SaveAs("cut_bestUL.pdf")

del bc