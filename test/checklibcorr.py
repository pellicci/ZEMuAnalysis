
"""
import correctionlib

fname = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/BTV/2024_Summer24/btagging.json.gz"
cset = correctionlib.CorrectionSet.from_file(fname)

print(list(cset.keys()))

for name in cset.keys():
    if "wp" in name.lower() or "pnet" in name.lower() or "particle" in name.lower():
        corr = cset[name]
        print("\n", name)
        print("description:", corr.description)
        print("inputs:", [(i.name, i.type) for i in corr.inputs])

"""
import correctionlib

fname = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/BTV/2024_Summer24/btagging.json.gz"

cset = correctionlib.CorrectionSet.from_file(fname)

wp_L   = cset["UParTAK4_wp_values"].evaluate("L")
wp_M   = cset["UParTAK4_wp_values"].evaluate("M")
wp_T   = cset["UParTAK4_wp_values"].evaluate("T")
wp_XT  = cset["UParTAK4_wp_values"].evaluate("XT")
wp_XXT = cset["UParTAK4_wp_values"].evaluate("XXT")

print(wp_L, wp_M, wp_T, wp_XT, wp_XXT)
