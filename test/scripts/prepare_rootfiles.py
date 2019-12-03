import ROOT
import os
import subprocess
import argparse

#---------------------------------#
p = argparse.ArgumentParser(description='Select whether to download MC or data')
p.add_argument('isData_option', help='Type <<MC>> or <<data>>')
p.add_argument('year_option', help='Type <<2016>>, <<2017>> or <<2018>>')
args = p.parse_args()

# Switch from muon to electron channel
if args.isData_option == "MC":
    isData = False
if args.isData_option == "data":
    isData = True

year = args.year_option
#---------------------------------#

if not os.path.exists("rootfiles"):
    os.makedirs("rootfiles")
if not os.path.exists("rootfiles/latest_production"):
    os.makedirs("rootfiles/latest_production")
if not os.path.exists("rootfiles/latest_production/MC"):
    os.makedirs("rootfiles/latest_production/MC")
if not os.path.exists("rootfiles/latest_production/dataprocess"):
    os.makedirs("rootfiles/latest_production/dataprocess")

print "Processing ", args.isData_option, " for year ", year

if not isData :
    dir_input = "crab_projects/samples_MC_" + year + "/"
    dir_output_bkg = "rootfiles/latest_production/MC/backgrounds/"
    dir_output_sig = "rootfiles/latest_production/MC/signals/"  
else :
    dir_input = "crab_projects/samples_data_" + year + "/"
    dir_output_data = "rootfiles/latest_production/dataprocess/"

list_dirs = os.listdir(dir_input)

complementary_samples_list_2016 = ["ttbarWlnu","ttbarZlnu","WJetsToLNu","QCDHT200to300","QCDHT300to500","QCDHT500to700","QCDHT700to1000","QCDHT1000to1500","QCDHT1500to2000","QCDHT2000toInf","WZ","TTGJets"]
complementary_samples_list_2017 = ["WJetsToLNu1J","WJetsToLNu2J","DY50","TTGJets"]
complementary_samples_list_2018 = ["NOTHING"]

if year == "2016":
    complementary_samples_list = complementary_samples_list_2016
if year == "2017":
    complementary_samples_list = complementary_samples_list_2017
if year == "2018":
    complementary_samples_list = complementary_samples_list_2018

if not isData and not os.path.exists(dir_output_bkg):
    os.makedirs(dir_output_bkg)

if not isData and not os.path.exists(dir_output_sig):
    os.makedirs(dir_output_sig)

for dirname in list_dirs:

    print "Processing sample dir " + dirname

    n_jobs_command = "crab status -d " + dir_input + dirname + " | grep status: " + "| awk " + """'{split($0,array,"/") ; print array[2]}'""" + "| sed 's/.$//'"
    n_jobs = int(subprocess.check_output(n_jobs_command, shell=True))

    print "Number of jobs to be retrieved: ", n_jobs

    crab_command = "crab getoutput -d " + dir_input + dirname
    os.system(crab_command)
    
    samplename = dirname.split("crab_" + year + "_ZEMuAnalysis_")

    if "Signal" in dirname:
        hadd_command = "../scripts/haddnano.py " + dir_output_sig + "ZEMuAnalysis_" + samplename[1] + "_" + year + ".root " + dir_input + dirname + "/results/*.root"
    elif isData:
        hadd_command = "../scripts/haddnano.py " + dir_output_data + "ZEMuAnalysis_" + samplename[1] + "_" + year + ".root " + dir_input + dirname + "/results/*.root"
    else:
        hadd_command = "../scripts/haddnano.py " + dir_output_bkg + "ZEMuAnalysis_" + samplename[1] + "_" + year + ".root " + dir_input + dirname + "/results/*.root"

    os.system(hadd_command)

# Now add samples with different names but same xsec
if not isData:

    for sample in complementary_samples_list:
        hadd_command = "../scripts/haddnano.py " + dir_output_bkg + "ZEMuAnalysis_" + sample + "_" + year + ".root " + dir_output_bkg + "ZEMuAnalysis_" + sample + "_*_" + year + ".root "
        rm_command = "rm -rf " + dir_output_bkg + "ZEMuAnalysis_" + sample + "_?_" + year + ".root "

        os.system(hadd_command)
        os.system(rm_command)

print "All done!"
