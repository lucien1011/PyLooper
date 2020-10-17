import numpy as np
import pickle,os

from Common.Module import Module

class FakeRateWeighter(Module):
    def analyze(self,data,dataset,cfg):
        if dataset.name == "ZX":
            cfg.collector.event_weight = np.ones(data["genWeight"].shape) * cfg.collector.selection_weight
            idx_3p1f = data["nFailedLeptonsZ2"] == 1
            idx_2p2f = data["nFailedLeptonsZ2"] == 2
            cfg.collector.event_weight[idx_3p1f] *= data["FRWeightProd"][idx_3p1f]
            cfg.collector.event_weight[idx_2p2f] *= -1.*data["FRWeightProd"][idx_2p2f]
