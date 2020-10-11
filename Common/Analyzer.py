class Analyzer(object):
    def __init__(self):
        self.header = "*"*100
        pass

    def build_dataset(self,cfg):
        self.dataset_list = cfg.dataset_list
        if cfg.verbose:
            print(self.header)
            print("Building dataset: ")
        for d in self.dataset_list:
            if cfg.verbose:
                print(d.name,len(d.componentList),"files")
            for c in d.componentList:
                c.build()
        if cfg.verbose:
            print(self.header)

    def loop(self,cfg,progressbar): 
        for d in self.dataset_list:
            for i,c in enumerate(d.componentList):
                taskname = d.name+"_"+str(i)
                c.loop(taskname,cfg,d,progressbar) 
