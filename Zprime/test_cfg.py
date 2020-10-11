from Common.Dataset import Dataset
from Common.Collector import Collector

from Zprime.Dataset.Run2017.SkimMC import qqZZ
from hep.cms.Weighter.CrossSectionWeighter import CrossSectionWeighter

from TestModule import TestModule,TestModuleGPU,PlotModule

branches = [
                "mass4l",
                "massZ1",
                "massZ2",
                "genWeight",
                ]
verbose = True
entrysteps = 1024
namedecode = "utf-8" 


dataset_list = [
        qqZZ,
        ]
collector = Collector(
        output_path = "./output/",
        )

modules = [
        TestModuleGPU("Test",),
        CrossSectionWeighter("CrossSection"),
        PlotModule("Plot",),
        ]
