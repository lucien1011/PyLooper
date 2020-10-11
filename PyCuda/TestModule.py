import numpy as np
import pickle,os

import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule

from Common.Module import Module

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
