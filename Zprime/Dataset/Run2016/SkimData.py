import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ______________________________________________________________________ ||
input_dir = "/cmsuf/data/store/user/t2/users/klo/Zprime/EXO-18-008/80X_Data_DarkZNTuple/"
tree_path_in_file = "passedEvents"

# ______________________________________________________________________ ||
data2016 = CMSDataset(
        "Data2016",
        [TFile(os.path.join(input_dir,"Data_Run2016-03Feb2017_4l.root"),tree_path_in_file,),],
        isMC = False,
        )

# ______________________________________________________________________ ||
