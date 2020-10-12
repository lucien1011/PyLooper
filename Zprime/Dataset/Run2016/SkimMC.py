import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ______________________________________________________________________ ||
input_dir = "/cmsuf/data/store/user/t2/users/klo/Zprime/EXO-18-008/80X_MCProd_DarkZNTuple/"
tree_path_in_file = "passedEvents"

# ______________________________________________________________________ ||
qqZZ = CMSDataset(
        "qqZZ",
        [TFile(os.path.join(input_dir,"ZZTo4L_13TeV_powheg_pythia8.root"),tree_path_in_file,),],
        xs = 1.256,
        sumw = 6669988.,
        plot_name = "$qq \\rightarrow ZZ$",
        )

# ______________________________________________________________________ ||
ggZZ = CMSDataset(
        "ggZZ",
        [TFile(os.path.join(input_dir,"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root"),tree_path_in_file,),],
        xs = 0.001586,
        sumw = 995200.,
        plot_name = "$gg \\rightarrow ZZ$",
        )
