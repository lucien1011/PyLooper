import numpy as np
import pickle,os

from Common.Module import Module

class SignalRegionSkimmer(Module):
    def analyze(self,data,dataset,cfg):
        cfg.collector.selection_weight = data["passedFullSelection"]
        cfg.collector.selection_weight *= data["mass4l"] > 118.
        cfg.collector.selection_weight *= data["mass4l"] < 130.
