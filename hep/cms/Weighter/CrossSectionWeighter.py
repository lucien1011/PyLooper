import numpy as np

from Common.Module import Module

class CrossSectionWeighter(Module):
    def analyze(self,data,dataset,cfg):
        if dataset.isMC: 
            cfg.collector.xs_weight = data["genWeight"]*dataset.xs*dataset.lumi/dataset.sumw
        else:
            cfg.collector.xs_weight = np.ones(data["genWeight"].shape)
