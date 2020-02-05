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
N_cuts = 30
var_min = 50.
var_max = 90.

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
    
    if tree_signal.M_ll < 80. or tree_signal.M_ll > 100. :
        continue

    if tree_signal.lep1pt < 26. or tree_signal.met > 28.:
        continue 

    var1 = tree_signal.jetptmax
    weight = tree_signal.mcweight

    for i in xrange(N_cuts) :
        cut_val = var_min + i*(var_max - var_min)/N_cuts

        if var1 < cut_val :
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

    if tree_background.M_ll < 80. or tree_background.M_ll > 100. :
        continue

    if tree_background.lep1pt < 26. or tree_background.met > 28. :
        continue
    
    var1 = tree_background.jetptmax
    weight = tree_background.mcweight

    for i in xrange(N_cuts) :
        cut_val = var_min + i*(var_max - var_min)/N_cuts

        if var1 < cut_val :
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
