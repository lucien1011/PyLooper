import numpy as np
import pickle,os
import uproot_methods

from Common.Module import Module

import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule

from Common.Module import Module

mod = SourceModule("""
#include <stdio.h>

__global__ void calculate(float *dest, float *lep_pt, float *lep_eta)
{
  const int i = threadIdx.x + blockDim.x * blockIdx.x;
  dest[i] = (lep_pt[i] > 7) && (abs(lep_eta[i]) < 2.5);
}
""")
calculate_selection_weight = mod.get_function("calculate")

class GPUSignalRegionSkimmer(Module):
    def analyze(self,data,dataset,cfg):
        if dataset.isMC:
            cfg.collector.selection_weight = np.zeros(cfg.entrysteps).astype(np.float32)
            calculate_selection_weight(
                    drv.Out(cfg.collector.selection_weight),
                    drv.In(data["lep_pt"].astype(np.float32)),
                    drv.In(data["lep_eta"].astype(np.float32)),
                    block=(cfg.nblock,1,1),
                    grid=(cfg.ngrid,1),
                    )
            cfg.collector.selection_weight = cfg.collector.selection_weight[:cfg.ibatch]

class SignalRegionSkimmer(Module):
    def analyze(self,data,dataset,cfg):
        cfg.collector.selection_weight = np.ones(cfg.ibatch).astype(np.float32)

        muon_id0_req = np.abs(data["lep_id"][:,0]) == 13
        muon_id1_req = np.abs(data["lep_id"][:,1]) == 13
        muon_pt0_req = data["lepFSR_pt"][:,0] > 20.
        muon_pt1_req = data["lepFSR_pt"][:,1] > 10.
        muon_tightId0_req = data["lep_tightId"][:,0] == 1.
        muon_tightId1_req = data["lep_tightId"][:,1] == 1.

        muon_req = muon_id0_req * muon_id1_req * muon_pt0_req * muon_pt1_req * muon_tightId0_req * muon_tightId1_req

        electron_id0_req = np.abs(data["lep_id"][:,0]) == 11
        electron_id1_req = np.abs(data["lep_id"][:,1]) == 11
        electron_pt0_req = data["lepFSR_pt"][:,0] > 25.
        electron_pt1_req = data["lepFSR_pt"][:,1] > 20.
        electron_tightId0_req = data["lep_tightId"][:,0] == 1.
        electron_tightId1_req = data["lep_tightId"][:,1] == 1.
        
        electron_req = electron_id0_req * electron_id1_req * electron_pt0_req * electron_pt1_req * electron_tightId0_req * electron_tightId1_req
        
        lep_iso1_req = data["lep_RelIsoNoFSR"][:,0] < 0.35 
        lep_iso2_req = data["lep_RelIsoNoFSR"][:,1] < 0.35 

        lep_req = np.logical_or(muon_req,electron_req) * lep_iso1_req * lep_iso2_req 
        
        cfg.collector.cutbased_pho_req = self.cut_based_id_pho(data)
        pho_req = cfg.collector.cutbased_pho_req.sum() >= 2

        cfg.collector.selection_weight *= lep_req
        cfg.collector.selection_weight *= pho_req
            
    def cut_based_id_pho(self,data,wpName="2017"):
        if wpName == "2017":
            barrel_neuIso_req = 0.317 + 0.01512*data["pho_pt"] + 2.258e-5*data["pho_pt"]*data["pho_pt"]
            barrel_pho_req = (data["pho_hadronicOverEm"] < 0.02148) * (data["pho_chargedHadronIso"] < 0.00996) * (data["pho_neutralHadronIso"] < barrel_neuIso_req) * (np.abs(data["pho_eta"]) < 1.4441) * data["pho_hasPixelSeed"] == 0
            endcap_neuIso_req = 2.716 + 0.0117*data["pho_pt"] + 2.3e-5*data["pho_pt"]*data["pho_pt"]
            endcap_pho_req = (data["pho_hadronicOverEm"] < 0.0321) * (data["pho_chargedHadronIso"] < 0.517) * (data["pho_neutralHadronIso"] < endcap_neuIso_req) * (np.abs(data["pho_eta"]) < 1.566) * (np.abs(data["pho_eta"]) < 2.5) * data["pho_hasPixelSeed"] == 0 
            return np.logical_or(barrel_pho_req,endcap_pho_req,) * np.abs(data["pho_eta"]) < 2.5
        else:
            raise RuntimeError

