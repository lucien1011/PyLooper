import numpy as np

from Common.Dataset import Dataset
from Common.Collector import Collector

from Zprime.Dataset.Run2016.SkimMC import qqZZ,ggZZ
from Zprime.Dataset.Run2016.SkimData import data2016

from hep.cms.Weighter.CrossSectionWeighter import CrossSectionWeighter

from Stat.Hist1D import Hist1D

from hep.RunPlotter.RunPlotter import RunPlotter
from hep.RunPlotter.Plot import Plot

from Zprime.Skimmer.AnalysisSkimmer import SignalRegionSkimmer
from Zprime.Weighter.DataMCWeighter import DataMCWeighter

branches    = [
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
verbose     = True
nblock      = 1024
ngrid       = 10
entrysteps  = nblock*ngrid
namedecode  = "utf-8" 

dataset_list = [
        qqZZ,
        ggZZ,
        data2016,
        ]
merged_dataset_list = []
for d in dataset_list:
    d.lumi = 35.9*1000.
    d.branches = branches

collector = Collector(
        output_path = "./output/2020-10-14_plot_SR_Run2016_cfg/",
        )

plots = [
        Plot("mZ1",lambda data,dataset,cfg: data["massZ1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),), 
        Plot("mZ2",lambda data,dataset,cfg: data["massZ2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(60,0.,60.),), 
        Plot("m4l",lambda data,dataset,cfg: data["mass4l"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,70.,110.),), 
        ]

modules = [
        CrossSectionWeighter("CrossSection"),
        SignalRegionSkimmer("SignalRegion"),
        DataMCWeighter("DataMCWeighter"),
        RunPlotter("Plot",),
        ]
