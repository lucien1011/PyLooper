from Common.Dataset import Dataset
from Common.Collector import Collector

from hep.cms.Weighter.CrossSectionWeighter import CrossSectionWeighter
from hep.cms.Dataset.MergedCMSDataset import MergedCMSDataset

from Stat.Hist1D import Hist1D

from hep.RunPlotter.RunPlotter import RunPlotter
from hep.RunPlotter.Plot import Plot

from HToZa.Dataset.Run2017.SkimMC import mc_bkg_samples,DYJetsToLL,TTJets
from HToZa.Skimmer.AnalysisSkimmer import SignalRegionSkimmer
from HToZa.Producer.VariableProducer import VariableProducer
from HToZa.Weighter.DataMCWeighter import DataMCWeighter,GPUDataMCWeighter

verbose = True
nblock = 1024
ngrid = 50
entrysteps = nblock*ngrid
namedecode = "utf-8" 

dataset_list = [
        DYJetsToLL,
        #TTJets,
        ]
for d in dataset_list:
    d.lumi = 41.7*1000.
merged_dataset_list = [
        MergedCMSDataset("DYJets",sample_list=[DYJetsToLL],plot_name="DYJets",),
        #MergedCMSDataset("TTJets",sample_list=[TTJets],plot_name="TTJets",),
        ]
collector = Collector(
        output_path = "./output/2020-10-20_plot_SR_Run2017_cfg/",
        )

plots = [
        Plot("lep_pt_0",lambda data,dataset,cfg: data["lep_pt"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,0.,120.),), 
        Plot("lep_pt_1",lambda data,dataset,cfg: data["lep_pt"][:,1],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,0.,120.),), 
        Plot("pho_pt_0",lambda data,dataset,cfg: data["pho_pt"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,0.,120.),), 
        Plot("pho_eta_0",lambda data,dataset,cfg: data["pho_eta"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,-3.,3.),), 
        Plot("pho_phi_0",lambda data,dataset,cfg: data["pho_phi"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,-4.,4.),), 
        Plot("pho_HoverE_0",lambda data,dataset,cfg: data["pho_hadronicOverEm"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,0.,0.05),), 
        Plot("pho_chIso_0",lambda data,dataset,cfg: data["pho_chargedHadronIso"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,0.,0.02),), 
        Plot("pho_neuIso_0",lambda data,dataset,cfg: data["pho_neutralHadronIso"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,0.,1.),), 
        Plot("pho_sigmaEtaEta_0",lambda data,dataset,cfg: data["pho_sigmaEtaEta"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,0.,0.04),), 
        Plot("pho_pt_1",lambda data,dataset,cfg: data["pho_pt"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,0.,120.),), 
        Plot("pho_eta_1",lambda data,dataset,cfg: data["pho_eta"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,-3.,3.),), 
        Plot("pho_phi_1",lambda data,dataset,cfg: data["pho_phi"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,-4.,4.),), 
        Plot("pho_HoverE_1",lambda data,dataset,cfg: data["pho_hadronicOverEm"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,0.,0.05),), 
        Plot("pho_chIso_1",lambda data,dataset,cfg: data["pho_chargedHadronIso"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,0.,0.02),), 
        Plot("pho_neuIso_1",lambda data,dataset,cfg: data["pho_neutralHadronIso"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,0.,1.),), 
        Plot("pho_sigmaEtaEta_1",lambda data,dataset,cfg: data["pho_sigmaEtaEta"][:,0],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,0.,0.04),), 
        Plot("Z_m",lambda data,dataset,cfg: cfg.collector.Z_vec.mass,lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,0.,120.),), 
        ]

modules = [
        CrossSectionWeighter("CrossSection"),
        SignalRegionSkimmer("SignalRegion"),
        GPUDataMCWeighter("GPUDataMCWeighter"),
        #DataMCWeighter("DataMCWeighter"),
        VariableProducer("VariableProducer"),
        RunPlotter("Plot",),
        ]
