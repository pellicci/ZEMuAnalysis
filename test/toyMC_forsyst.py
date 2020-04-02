import ROOT

fIn = ROOT.TFile("workspaces/fit_Mll_Backgroundonly_Combined.root")
fIn.cd()

wsIn = fIn.Get("ws")

wsIn.Print()

gener_PDF = wsIn.pdf("totPDF_constr_alt")
fit_PDF = wsIn.pdf("totPDF_constr")

M_ll = wsIn.var("M_ll")
br_emu = wsIn.var("br_emu")

mcstudy = ROOT.RooMCStudy(gener_PDF,ROOT.RooArgSet(M_ll),ROOT.RooFit.FitModel(fit_PDF),ROOT.RooFit.Silence(), ROOT.RooFit.Extended(1), ROOT.RooFit.FitOptions(ROOT.RooFit.Save(1), ROOT.RooFit.PrintEvalErrors(0)))
mcstudy.generateAndFit(1000)

#Plot the distributions of the fitted parameter, the error and the pull
brval_frame = mcstudy.plotParam(br_emu, ROOT.RooFit.Bins(40))
brerr_frame = mcstudy.plotError(br_emu, ROOT.RooFit.Bins(40))
brpull_frame = mcstudy.plotPull(br_emu, ROOT.RooFit.Bins(40), ROOT.RooFit.FitGauss(1))

#Plot distribution of minimized likelihood
NLLframe = mcstudy.plotNLL(ROOT.RooFit.Bins(40))

#Actually plot
canvas = ROOT.TCanvas()
canvas.Divide(2,2)
canvas.cd(1)
brval_frame.Draw()
canvas.cd(2)
brerr_frame.Draw()
canvas.cd(3)
brpull_frame.Draw()
canvas.cd(4)
NLLframe.Draw()
canvas.SaveAs("plots/latest_production/2016_2017_2018/plot_toyMC.pdf")