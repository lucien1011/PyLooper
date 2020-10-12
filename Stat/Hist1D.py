import numpy as np

class Hist1D(object):

    def __init__(self, nbins, xlow, xhigh):
        self.nbins = nbins
        self.xlow  = xlow
        self.xhigh = xhigh
        self.content, self.edges = np.histogram([], bins=nbins, range=(xlow, xhigh))
        self.content = self.content.astype(np.float64)
        self.error2 = self.content.astype(np.float64)
        self.bins = (self.edges[:-1] + self.edges[1:]) / 2.

    def fill(self, arr, weights=None):
        content, edges = np.histogram(arr, bins=self.nbins, range=(self.xlow, self.xhigh), weights=weights,)
        self.content += content
        self.error2 += np.square(content)

    @property
    def data(self):
        return self.bins, self.content

    @property
    def numpy_content(self):
        return np.reshape(np.array(self.content),(len(self.content),1))

    @property
    def numpy_error2(self):
        return np.reshape(np.array(self.content),(len(self.content),1))


    @property
    def numpy_edges(self):
        return np.reshape(np.array(self.edges[:-1]),(len(self.edges[:-1]),1))

    @property
    def numpy_centers(self):
        return np.reshape(np.array(self.bins),(len(self.bins),1))
