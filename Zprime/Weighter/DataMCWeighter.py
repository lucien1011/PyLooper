import numpy as np
import pickle,os

from Common.Module import Module

class DataMCWeighter(Module):
    def analyze(self,data,dataset,cfg):
        if dataset.isMC and not dataset.skip_weight:
            cfg.collector.event_weight = cfg.collector.xs_weight * cfg.collector.selection_weight * data["dataMCWeight"] * data["pileupWeight"] * data["k_qqZZ_qcd_M"] * data["k_qqZZ_ewk"]
        else:
            cfg.collector.event_weight = np.ones(data["genWeight"].shape) * cfg.collector.selection_weight


