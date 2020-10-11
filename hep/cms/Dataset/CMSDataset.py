from Common.Dataset import Dataset

class CMSDataset(Dataset):
    def __init__(self,name,componentList,xs=None,sumw=None):
        self.name = name
        self.componentList = componentList
        self.xs = xs
        self.sumw = sumw
