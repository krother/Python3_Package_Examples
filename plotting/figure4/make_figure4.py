#!/usr/bin/env python

from pylab import *
import pandas as pd

data = pd.read_csv('bootstrap_take_all.txt', header=0)

FONT = 14
SYMBOLSIZE = 6

fig = figure(figsize=(7.0, 5.0))

title('Influence of Tanimoto coefficient threshold', fontsize=FONT)
xlabel('similarity threshold $T_c$', fontsize=FONT)
ylabel('RMSD of Gibbs energy [kJ/mol]', fontsize=FONT)

plot(data.sim, data.gcm,'gs', ms=SYMBOLSIZE, markeredgewidth=0.4)
plot(data.sim, data.igers, 'ro', ms=SYMBOLSIZE, markeredgewidth=0.4)

savefig('figure4.png', dpi=300)
