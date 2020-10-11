import os,sys,importlib,time
from Common.Analyzer import Analyzer

from ProgressBar.ProgressBar import ProgressBar

# __________________________________________________________________________________________ ||
spec = importlib.util.spec_from_file_location("configuration", sys.argv[1])
cfg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cfg)

# __________________________________________________________________________________________ ||
if cfg.verbose:
    print("Starting")
start_time = time.time()

ana = Analyzer()
progressbar = ProgressBar()
ana.build_dataset(cfg)
ana.loop(cfg,cfg.modules,cfg.collector,progressbar,)

elapsed_time = time.time() - start_time
print("Time used: "+str(elapsed_time)+"s")
