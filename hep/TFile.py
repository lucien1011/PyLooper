import uproot

from ProgressBar.ProgressReport import ProgressReport

class TFile(object):
    """Wrapper for root file"""
    def __init__(self,input_path,tree_path_in_file):
        self.input_path = input_path
        self.tree_path_in_file = tree_path_in_file

    def build(self):
        self.file = uproot.open(self.input_path)
        self.tree = self.file[self.tree_path_in_file]

    def loop(self,taskname,cfg,dataset,modules,collector,progressbar):
        report = ProgressReport(taskname,0,self.tree.numentries)
        for m in modules:
            m.begin(collector)
        for data in self.tree.iterate(cfg.branches, entrysteps=cfg.entrysteps,namedecode=cfg.namedecode,):
            for m in modules:
                m.analyze(data,collector)
            report.done += cfg.entrysteps
            progressbar.present(report)
        for m in modules:
            m.end(collector)
