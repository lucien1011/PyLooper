import os,pickle
import numpy as np

from Common.Module import Module

from Utils.mkdir_p import mkdir_p 

class RunPlotter(Module):
    def analyze(self,data,dataset,cfg):
        for p in cfg.plots:
            array_to_fill = p.array_func(data,dataset,cfg)
            event_weight_to_fill = p.event_weight_func(data,dataset,cfg)
            p.hist.fill(array_to_fill,event_weight_to_fill)

    def end(self,dataset,cfg):
        output_dir = os.path.join(cfg.collector.output_path,dataset.name)
        mkdir_p(output_dir)
        for p in cfg.plots:
            f = open(os.path.join(output_dir,p.name+".p"),"wb")
            pickle.dump(p.hist,f)
