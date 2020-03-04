import ROOT
import math

ROOT.gStyle.SetOptStat(0)

eff_mu = 0.8
eff_ele = 0.8

h_ratio = ROOT.TH2F("h_ratio","h_ratio",20,0.79,1.,20,0.79,1.)

for i in xrange(19) :
	eff_mu_temp = eff_mu + i*0.01
	for j in xrange(19) :
		eff_ele_temp = eff_ele + j*0.01

		numerator = math.sqrt(1. - (1.-eff_mu_temp) * (1.-eff_ele_temp) * 0.3)
		denominator = math.sqrt(1. - 0.3* (1-eff_mu_temp)**2.) * math.sqrt(1. - 0.3* (1.-eff_ele_temp)**2.)

		ratio = numerator/denominator

		print eff_mu_temp, eff_ele_temp, ratio

		h_ratio.Fill(eff_mu_temp,eff_ele_temp,ratio)


h_ratio.GetZaxis().SetRangeUser(0.9,1.1)

c1 = ROOT.TCanvas()
c1.cd()
h_ratio.Draw("COLZ")
c1.SaveAs("eff_ratio_test.pdf")