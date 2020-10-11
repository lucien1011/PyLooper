from Stat.Hist1D import Hist1D 
import pickle
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

h_qqZZ = pickle.load(open("output/qqZZ/hist_mZ1.csv","rb"))
h_data = pickle.load(open("output/Data2017/hist_mZ1.csv","rb"))

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(6,1)
ax1 = fig.add_subplot(gs[:4,:])
ax2 = fig.add_subplot(gs[4:,:])

ax1.hist(h_qqZZ.edges[:-1], bins=h_qqZZ.nbins, weights=h_qqZZ.hist,)
dataerr = np.sqrt(h_data.hist)
ax1.errorbar(h_data.edges[:-1], h_data.hist, yerr=dataerr, marker=".", linestyle="None")

ratio = h_data.hist/h_qqZZ.hist
ratio[ratio == np.inf] = 0
ax2.errorbar(h_qqZZ.edges[:-1],ratio)
ax2.set_xlim(ax1.get_xlim())
ax2.set_ylim(0.,2.)
start, end = ax2.get_ylim()
ax2.yaxis.set_ticks(np.arange(start, end, 0.25))
ax2.grid()

fig.savefig("mZ1.png")

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(6,1)
ax1 = fig.add_subplot(gs[:4,:])
ax2 = fig.add_subplot(gs[4:,:])

h_qqZZ = pickle.load(open("output/qqZZ/hist_mZ2.csv","rb"))
h_data = pickle.load(open("output/Data2017/hist_mZ2.csv","rb"))
ax1.hist(h_qqZZ.edges[:-1], bins=h_qqZZ.nbins, weights=h_qqZZ.hist,)
dataerr = np.sqrt(h_data.hist)
ax1.errorbar(h_data.edges[:-1], h_data.hist, yerr=dataerr, marker=".", linestyle="None")

ratio = h_data.hist/h_qqZZ.hist
ratio[ratio == np.inf] = 0
ax2.errorbar(h_qqZZ.edges[:-1],ratio)
ax2.set_xlim(ax1.get_xlim())
ax2.set_ylim(0.,2.)
start, end = ax2.get_ylim()
ax2.yaxis.set_ticks(np.arange(start, end, 0.25))
ax2.grid()

fig.savefig("mZ2.png")
