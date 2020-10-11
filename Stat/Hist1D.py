import numpy as np

class Hist1D(object):

    def __init__(self, nbins, xlow, xhigh):
        self.nbins = nbins
        self.xlow  = xlow
        self.xhigh = xhigh
        self.hist, self.edges = np.histogram([], bins=nbins, range=(xlow, xhigh))
        self.hist = self.hist.astype(np.float64)
        self.bins = (self.edges[:-1] + self.edges[1:]) / 2.

    def fill(self, arr, weights=None):
        hist, edges = np.histogram(arr, bins=self.nbins, range=(self.xlow, self.xhigh), weights=weights,)
        self.hist += hist

    @property
    def data(self):
        return self.bins, self.hist
