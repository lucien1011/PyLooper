from Common.Dataset import Dataset

class MergedCMSDataset(Dataset):
    def __init__(self,name,isMC=True,sample_list=[],plot_name=None,):
        self.name = name
        self.isMC = isMC
        self.isData = not isMC
        self.sample_list = sample_list
        self.plot_name = self.name if not plot_name else plot_name

