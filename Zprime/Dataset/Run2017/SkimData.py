import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ______________________________________________________________________ ||
input_dir = "/cmsuf/data/store/user/t2/users/klo/Zprime/EXO-18-008/94X_Data_DarkZNTuple/"
tree_path_in_file = "passedEvents"

# ______________________________________________________________________ ||
data2017 = CMSDataset(
        "Data2017",
        [TFile(os.path.join(input_dir,"Data_Run2017-17Nov2017-v1_noDuplicates.root"),tree_path_in_file,),],
        isMC = False,
        )

# ______________________________________________________________________ ||
