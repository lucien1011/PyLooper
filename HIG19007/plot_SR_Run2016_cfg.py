from Common.Dataset import Dataset
from Common.Collector import Collector

from HIG19007.Dataset.Run2016.SkimMC import ggH,qqZZ,ggZZ4mu,ggZZ4e,ggZZ4tau,ggZZ2e2mu,ggZZ2mu2tau,ggZZ2e2tau,VBF,WplusH,WminusH,ZH,mc_bkg_samples
from HIG19007.Dataset.Run2016.SkimData import data2016
from HIG19007.Dataset.Run2016.SkimZXCR import ZX

from hep.cms.Weighter.CrossSectionWeighter import CrossSectionWeighter

from hep.cms.Dataset.MergedCMSDataset import MergedCMSDataset

from Stat.Hist1D import Hist1D

from hep.RunPlotter.RunPlotter import RunPlotter
from hep.RunPlotter.Plot import Plot

from HIG19007.Skimmer.AnalysisSkimmer import SignalRegionSkimmer
from HIG19007.Weighter.DataMCWeighter import DataMCWeighter

branches = [
                "mass4l",
                "massZ1",
                "massZ2",
                "genWeight",
                "passedFullSelection",
                "dataMCWeight",
                "pileupWeight",
                "k_qqZZ_qcd_M",
                "k_qqZZ_ewk",
                "idL1",
                "idL2",
                "idL3",
                "idL4",
                ]
verbose = True
entrysteps = 1024*10
namedecode = "utf-8" 

dataset_list = mc_bkg_samples + [data2016] 
for d in dataset_list:
    d.lumi = 35.9*1000.
merged_dataset_list = [
        MergedCMSDataset("Higgs",sample_list=[ggH,VBF,WplusH,WminusH,ZH,],plot_name="Higgs",),
        MergedCMSDataset("ZZ",sample_list=[qqZZ,ggZZ4mu,ggZZ4e,ggZZ4tau,ggZZ2e2mu,ggZZ2mu2tau,ggZZ2e2tau],plot_name="ZZ",),
        ]

collector = Collector(
        output_path = "./output/2020-10-12_plot_SR_Run2016_cfg/",
        )

plots = [
        Plot("mZ1",lambda data,dataset,cfg: data["massZ1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(80,40.,120.),), 
        Plot("mZ2",lambda data,dataset,cfg: data["massZ2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(60,0.,60.),), 
        Plot("m4l",lambda data,dataset,cfg: data["mass4l"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,100.,140.),), 
        ]

modules = [
        CrossSectionWeighter("CrossSection"),
        SignalRegionSkimmer("SignalRegion"),
        DataMCWeighter("DataMCWeighter"),
        RunPlotter("Plot",),
        ]
