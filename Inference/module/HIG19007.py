import tensorflow as tf
import numpy as np

from Common.Module import Module

class InputModule(Module):
    def analyze(self,data,training,cfg):
        cfg.pois = np.array([[m/35.] for m in training.data_wrapper.input_path_dict])
        cfg.x = np.array([data[i]["massZ2"].to_numpy()/35. for i,m in enumerate(training.data_wrapper.input_path_dict)])
        cfg.inputs = np.apply_along_axis(lambda x: np.histogram(x, bins=cfg.bins, density=1.)[0], 1, cfg.x) 
