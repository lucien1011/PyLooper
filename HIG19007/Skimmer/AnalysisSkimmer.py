import numpy as np
import pickle,os

from Common.Module import Module

class SignalRegionSkimmer(Module):
    def analyze(self,data,dataset,cfg):
        if dataset.name != "ZX":
            cfg.collector.selection_weight = data["passedFullSelection"]
        else:
            cfg.collector.selection_weight = data["passedZXCRSelection"]
        cfg.collector.selection_weight *= data["mass4l"] > 118.
        cfg.collector.selection_weight *= data["mass4l"] < 130.
