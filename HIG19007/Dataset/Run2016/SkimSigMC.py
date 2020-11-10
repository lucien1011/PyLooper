import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

from HIG19007.Dataset.xs import hzzd_xs_dict

from Site import Site

# ______________________________________________________________________ ||
site = Site()
if site.where == site.ufhpc:
    input_dir = "/cmsuf/data/store/user/t2/users/klo/IHEPA/raid/Higgs/DarkZ-NTuple/20191201/SkimTree_DarkPhoton_Run2016Data_m4l70/"
elif site.where == site.laptop:
    input_dir = "/Users/lucien/CMS/NTuple/lucien/Higgs/DarkZ-NTuple/20191201/SkimTree_DarkPhoton_Run2016Data_m4l70/"

tree_path_in_file = "passedEvents"

epsilon                 = 0.5
mass_points             = [1,2,3,4,7,10,15,20,25,30,35,]

# ____________________________________________________________________________________________________________________________________________ ||
hzzd_sample_dict = {}
for m in mass_points:
    hzzd_sample_dict[m] = CMSDataset(
            "HZZd_M"+str(m),
            [TFile(os.path.join(input_dir,"HToZZdTo4L_M125_MZd%s_eps1e-2_13TeV_madgraph_pythia8.root"%str(m)),tree_path_in_file,),],
            xs = hzzd_xs_dict[m]*epsilon**2,
            plot_name = "$H \\rightarrow ZZ_{d}"+" ["+str(m)+"GeV]$",
            isSignal = True,
            )
    hzzd_sample_dict[m].read_sumw_by_text_file(os.path.join(input_dir,"HToZZdTo4L_M125_MZd%s_eps1e-2_13TeV_madgraph_pythia8.txt"%str(m)))

for m,sig in hzzd_sample_dict.items():
    sig.branches = [
                "mass4l",
                "massZ1",
                "massZ2",
                "genWeight",
                "passedFullSelection",
                "passedZXCRSelection",
                "dataMCWeight",
                "pileupWeight",
                "k_qqZZ_qcd_M",
                "k_qqZZ_ewk",
                "idL1",
                "idL2",
                "idL3",
                "idL4",
                ]
