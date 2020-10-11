import numpy as np
import pickle,os

import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule

from Common.Module import Module

from Stat.Hist1D import Hist1D

mod = SourceModule("""
__global__ void calculate(float *dest, float *a, float *b)
{
  const int i = threadIdx.x;
  dest[i] = a[i] + b[i];
}
""")

calculate = mod.get_function("calculate")

class TestModuleGPU(Module):
    def analyze(self,data,dataset,cfg):
        cfg.collector.dest = np.zeros(1024)
        calculate(drv.Out(cfg.collector.dest), drv.In(data["mass4l"]), drv.In(data["mass4l"]),block=(1024,1,1), grid=(1,1))

class TestModule(Module):
    def analyze(self,data,dataset,cfg):
        cfg.collector.dest = np.zeros(1024)
        cfg.collector.dest = data["mass4l"] + data["mass4l"]

class PlotModule(Module):
    def begin(self,dataset,cfg):
        self.hist = Hist1D(100,0.,120.)

    def analyze(self,data,dataset,cfg):
        self.hist.fill(data["massZ1"],weights=cfg.collector.xs_weight,)

    def end(self,dataset,cfg):
        f = open(os.path.join(cfg.collector.output_path,"hist.csv"),"wb")
        pickle.dump(self.hist,f)
