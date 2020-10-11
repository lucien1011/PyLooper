from Common.Dataset import Dataset

class CMSDataset(Dataset):
    def __init__(self,name,componentList,xs=None,sumw=None,isMC=True,lumi=None,):
        self.name = name
        self.componentList = componentList
        self.xs = xs
        self.lumi = lumi
        self.sumw = sumw
        self.isMC = isMC
        self.isData = not isMC
