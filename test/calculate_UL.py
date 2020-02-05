import ROOT

fInput = ROOT.TFile("workspaces/fit_Mll_Backgroundonly_2018.root")
fInput.cd()
ws = fInput.Get("ws")

br_emu = ws.var("br_emu")
br_emu.setRange(-0.00001,0.000001)
poi_list = ROOT.RooArgSet(br_emu)
obs_list = ROOT.RooArgSet(ws.var("M_ll"))
data = ws.data("bkgPDFData")

data_binned = data.binnedClone("data_binned","data_binned")
getattr(ws,'import')(data_binned)

ws.Print()

ws.var("a_bkg").setConstant(1)
ws.var("b_bkg").setConstant(1)
ws.var("c_bkg").setConstant(1)
ws.var("d_bkg").setConstant(1)

#Set the RooModelConfig and let it know what the content of the workspace is about
model = ROOT.RooStats.ModelConfig()
model.SetWorkspace(ws)
model.SetPdf("totPDF")
model.SetParametersOfInterest(poi_list)
model.SetObservables(obs_list)
model.SetName("S+B Model")
model.SetProtoData(data_binned)

bModel = model.Clone()
bModel.SetName("B model")
oldval = poi_list.find("br_emu").getVal()
poi_list.find("br_emu").setVal(0) #BEWARE that the range of the POI has to contain zero!
bModel.SetSnapshot(poi_list)
poi_list.find("br_emu").setVal(oldval)

fc = ROOT.RooStats.FrequentistCalculator(data_binned, bModel, model)
fc.SetToys(350,350)

#Create hypotest inverter passing desired calculator
calc = ROOT.RooStats.HypoTestInverter(fc)

calc.SetConfidenceLevel(0.95)

#Use CLs
calc.UseCLs(1)
calc.SetVerbose(0)
#Configure ToyMC sampler
toymc = fc.GetTestStatSampler()
#Set profile likelihood test statistics
profl = ROOT.RooStats.ProfileLikelihoodTestStat(model.GetPdf())
#For CLs (bounded intervals) use one-sided profile likelihood
profl.SetOneSided(1)
#Set the test statistic to use
toymc.SetTestStatistic(profl)

npoints = 10 #Number of points to scan
# min and max for the scan (better to choose smaller intervals)
poimin = poi_list.find("br_emu").getMin()
poimax = poi_list.find("br_emu").getMax()

min_scan = 0.000000001
max_scan = 0.000001
print "Doing a fixed scan  in interval : ",min_scan, " , ", max_scan
calc.SetFixedScan(npoints,min_scan,max_scan)

# In order to use PROOF, one should install the test statistic on the workers
# pc = ROOT.RooStats.ProofConfig(workspace, 0, "workers=6",0)
# toymc.SetProofConfig(pc)

result = calc.GetInterval() #This is a HypoTestInveter class object

upperLimit = result.UpperLimit()

print "################"
print "The observed CLs upper limit is: ", upperLimit

##################################################################

#Compute expected limit
print "Expected upper limits, using the B (alternate) model : "
print " expected limit (median) ", result.GetExpectedUpperLimit(0)
print " expected limit (-1 sig) ", result.GetExpectedUpperLimit(-1)
print " expected limit (+1 sig) ", result.GetExpectedUpperLimit(1)
print "################"

#Plot the results
freq_plot = ROOT.RooStats.HypoTestInverterPlot("HTI_Result_Plot","Frequentist scan result for the W -> pigamma BR",result)

#xPlot in a new canvas with style
canvas = ROOT.TCanvas()
canvas.cd()
#freq_plot.Draw("2CL")
freq_plot.Draw("EXP")
# freq_plot.GetYaxis().SetRangeUser(0.,0.8)
# freq_plot.GetXaxis().SetRange(0.,0.0000107)
canvas.SaveAs("plots/latest_production/2018/UL_CLs.pdf")

del fc
