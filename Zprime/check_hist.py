from Stat.Hist1D import Hist1D 
import pickle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

h = pickle.load(open("output/hist.csv","rb"))
plt.hist(h.edges[:-1], bins=h.nbins, weights=h.hist)
plt.savefig("test.png")
