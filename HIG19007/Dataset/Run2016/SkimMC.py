import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ______________________________________________________________________ ||
input_dir = "/cmsuf/data/store/user/t2/users/klo/IHEPA/raid/Higgs/DarkZ-NTuple/20190122/SkimTree_DarkPhoton_Run2016Data_m4l70/"
tree_path_in_file = "passedEvents"

# ______________________________________________________________________ ||
ggH = CMSDataset(
        "ggH",
        [TFile(os.path.join(input_dir,"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root"),tree_path_in_file,),],
        xs = 48.52*0.0002768,
        sumw = 999800.0,
        plot_name = "$gg \\rightarrow H$",
        )

# ______________________________________________________________________ ||
qqZZ = CMSDataset(
        "qqZZ",
        [TFile(os.path.join(input_dir,"ZZTo4L_13TeV_powheg_pythia8.root"),tree_path_in_file,),],
        xs = 1.256,
        sumw = 6669988.0,
        plot_name = "$qq \\rightarrow ZZ$",
        )

# ______________________________________________________________________ ||
ggZZ4mu = CMSDataset(
        "ggZZ4mu",
        [TFile(os.path.join(input_dir,"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root"),tree_path_in_file,),],
        xs = 0.001586,
        sumw = 995200.0,
        plot_name = "$gg \\rightarrow ZZ \\rightarrow 4\\mu$",
        )

# ______________________________________________________________________ ||
ggZZ4e = CMSDataset(
        "ggZZ4e",
        [TFile(os.path.join(input_dir,"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root"),tree_path_in_file,),],
        xs = 0.001586,
        sumw = 965000.0,
        plot_name = "$gg \\rightarrow ZZ \\rightarrow 4\\mu$",
        )

# ______________________________________________________________________ ||
ggZZ4tau = CMSDataset(
        "ggZZ4tau",
        [TFile(os.path.join(input_dir,"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root"),tree_path_in_file,),],
        xs = 0.001586,
        sumw = 495800.0,
        plot_name = "$gg \\rightarrow ZZ \\rightarrow 4\\mu$",
        )

# ______________________________________________________________________ ||
ggZZ2e2mu = CMSDataset(
        "ggZZ2e2mu",
        [TFile(os.path.join(input_dir,"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root"),tree_path_in_file,),],
        xs = 0.001586,
        sumw = 1469600.0,
        plot_name = "$gg \\rightarrow ZZ \\rightarrow 4\\mu$",
        )

# ______________________________________________________________________ ||
ggZZ2e2tau = CMSDataset(
        "ggZZ2e2tau",
        [TFile(os.path.join(input_dir,"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root"),tree_path_in_file,),],
        xs = 0.001586,
        sumw = 500000.0,
        plot_name = "$gg \\rightarrow ZZ \\rightarrow 4\\mu$",
        )

# ______________________________________________________________________ ||
ggZZ2mu2tau = CMSDataset(
        "ggZZ2mu2tau",
        [TFile(os.path.join(input_dir,"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root"),tree_path_in_file,),],
        xs = 0.001586,
        sumw = 499800.0,
        plot_name = "$gg \\rightarrow ZZ \\rightarrow 4\\mu$",
        )

# ______________________________________________________________________ ||
VBF = CMSDataset(
        "VBF",
        [TFile(os.path.join(input_dir,"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root"),tree_path_in_file,),],
        xs = 0.001044,
        sumw = 499312.0,
        plot_name = "$VBF$",
        )

# ______________________________________________________________________ ||
WminusH = CMSDataset(
        "WminusH",
        [TFile(os.path.join(input_dir,"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root"),tree_path_in_file,),],
        xs = 0.000147,
        sumw = 186036.0,
        plot_name = "$W^{-}H$",
        )

# ______________________________________________________________________ ||
WplusH = CMSDataset(
        "WplusH",
        [TFile(os.path.join(input_dir,"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root"),tree_path_in_file,),],
        xs = 0.000232,
        sumw = 279824.0,
        plot_name = "$W^{+}H$",
        )

# ______________________________________________________________________ ||
ZH = CMSDataset(
        "ZH",
        [TFile(os.path.join(input_dir,"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8.root"),tree_path_in_file,),],
        xs = 0.000668,
        sumw = 470416.0,
        plot_name = "$ZH$",
        )

# ______________________________________________________________________ ||
mc_bkg_samples = [
        ggH,
        qqZZ,
        ggZZ4mu,
        ggZZ4e,
        ggZZ4tau,
        ggZZ2e2mu,
        ggZZ2mu2tau,
        ggZZ2e2tau,
        VBF,
        WplusH,
        WminusH,
        ZH,
        ]
