import rpy2.robjects as ro
r = ro.r
T = r("read.table('csq_input.txt', header=TRUE, sep='\t')")
#print r.names(T)
cont_table = r.table(T[1],T[2])
chitest = r['chisq.test']
print chitest(T[1],T[2])
