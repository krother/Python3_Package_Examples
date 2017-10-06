from rpy import *

def readTable(filename):
	f = r.read_table(filename,sep='\t')
	return f['V3'], f['V5'], f['V7']

def stdev(distr):
	return r.sd(distr)

def av(distr):
	return r.mean(distr)

distributions = readTable('RandomDistribution.tsv')

for d in distributions:
	print av(d), stdev(d)
