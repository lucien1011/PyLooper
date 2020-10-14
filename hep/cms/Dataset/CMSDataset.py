from Common.Dataset import Dataset

class CMSDataset(Dataset):
    def __init__(self,name,componentList,xs=None,sumw=None,isMC=True,lumi=None,plot_name=None,skip_weight=False):
        self.name = name
        self.componentList = componentList
        self.xs = xs
        self.lumi = lumi
        self.sumw = sumw
        self.isMC = isMC
        self.isData = not isMC
        self.skip_weight = skip_weight
        self.plot_name = self.name if not plot_name else plot_name

