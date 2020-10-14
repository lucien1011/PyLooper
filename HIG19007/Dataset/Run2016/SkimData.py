import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ______________________________________________________________________ ||
input_dir = "/cmsuf/data/store/user/t2/users/klo/IHEPA/raid/Higgs/DarkZ-NTuple/20181116/SkimTree_DarkPhoton_Run2016Data_m4l70/"
tree_path_in_file = "passedEvents"

# ______________________________________________________________________ ||
data2016 = CMSDataset(
        "Data2016",
        [TFile(os.path.join(input_dir,"Data_Run2016-03Feb2017_4l_noDuplicates.root"),tree_path_in_file,),],
        isMC = False,
        )

# ______________________________________________________________________ ||
