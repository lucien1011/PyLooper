import numpy as np

from Common.Module import Module

class CrossSectionWeighter(Module):
    def analyze(self,data,dataset,cfg):
        cfg.collector.xs_weight = data["genWeight"]*dataset.xs/dataset.sumw
