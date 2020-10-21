import numpy as np
import pickle,os
import uproot_methods

from Common.Module import Module

import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule

from Common.Module import Module

class VariableProducer(Module):
    def analyze(self,data,dataset,cfg):
        cfg.collector.lep0_vec = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["lepFSR_pt"][:,0],data["lepFSR_eta"][:,0],data["lepFSR_phi"][:,0],data["lepFSR_mass"][:,0])
        cfg.collector.lep1_vec = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["lepFSR_pt"][:,1],data["lepFSR_eta"][:,1],data["lepFSR_phi"][:,1],data["lepFSR_mass"][:,1])
        cfg.collector.Z_vec = cfg.collector.lep0_vec + cfg.collector.lep1_vec
