import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ______________________________________________________________________ ||
skim_dir = "/cmsuf/data/store/user/t2/users/klo/HToZaToLLGG/UFHZZLiteAnalyzer/HToZA_MC17_bkg/"
input_dir = "/cmsuf/data/store/user/t2/users/klo/HToZaToLLGG/HToZA_MC17_bkg/"
#tree_path_in_file = "Ana/passedEvents"
tree_path_in_file = "passedEvents"
hist_path_in_file = "Ana/sumWeights"

# ______________________________________________________________________ ||
DYJetsToLL = CMSDataset(
        "DYLLJets",
        [TFile(os.path.join(skim_dir,"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17MiniAODv2.root"),tree_path_in_file,),],
        xs = 6104.0,
        plot_name = "DYJets",
        )
DYJetsToLL.read_sumw_by_hist(os.path.join(input_dir,"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17MiniAODv2.root"),hist_path_in_file)

# ______________________________________________________________________ ||
TTJets = CMSDataset(
        "TTJets",
        [TFile(os.path.join(skim_dir,"TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root"),tree_path_in_file,),],
        xs = 687.1,
        plot_name = "TTJets",
        )
TTJets.read_sumw_by_hist(os.path.join(input_dir,"TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root"),hist_path_in_file)

# ______________________________________________________________________ ||
mc_bkg_samples = [
        DYJetsToLL,
        TTJets,
        ]
for b in mc_bkg_samples:
    b.branches = [
                "genWeight",
                "dataMCWeight",
                "pileupWeight",
                "lepFSR_pt",
                "lepFSR_eta",
                "lepFSR_phi",
                "lepFSR_mass",
                "lep_pt",
                "lep_eta",
                "lep_phi",
                "lep_id",
                "lep_tightId",
                "lep_RelIsoNoFSR",
                "pho_pt",
                "pho_eta",
                "pho_phi",
                "pho_sigmaEtaEta",
                "pho_chargedHadronIso",
                "pho_neutralHadronIso",
                "pho_hadronicOverEm",
                "pho_EleVote",
                "pho_hasPixelSeed",
                ]
