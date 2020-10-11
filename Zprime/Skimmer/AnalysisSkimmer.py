import numpy as np
import pickle,os

from Common.Module import Module

class SignalRegionSkimmer(Module):
    def analyze(self,data,dataset,cfg):
        cfg.collector.selection_weight = data["passedFullSelection"]
        cfg.collector.selection_weight *= data["mass4l"] > 80.
        cfg.collector.selection_weight *= data["mass4l"] < 100.
        cfg.collector.selection_weight *= np.abs(data["idL1"]) == 13
        cfg.collector.selection_weight *= np.abs(data["idL2"]) == 13
        cfg.collector.selection_weight *= np.abs(data["idL3"]) == 13
        cfg.collector.selection_weight *= np.abs(data["idL4"]) == 13
