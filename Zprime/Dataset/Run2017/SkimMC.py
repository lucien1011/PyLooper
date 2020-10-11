import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ______________________________________________________________________ ||
input_dir = "/cmsuf/data/store/user/t2/users/klo/UFNTupleRunner_Storage/kinho.lo/Higgs/Zprime-NTuple/20200415/SkimTree_Zprime_Run2017Data_m4l70/"
tree_path_in_file = "passedEvents"

# ______________________________________________________________________ ||
qqZZ = CMSDataset(
        "qqZZ",
        [TFile(os.path.join(input_dir,"ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root"),tree_path_in_file,),],
        xs = 1.256*1000,
        sumw = 6669988.0,
        )

# ______________________________________________________________________ ||
