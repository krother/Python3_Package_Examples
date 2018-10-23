"""
PageRank algorithm - example application of matrices

https://en.wikipedia.org/wiki/PageRank

SPOILER ALERT: contains data from Pandemic Legacy Season 2
"""

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


pairs1 = pd.read_csv('city_pairs.csv', names=['city1', 'city2'])
pairs2 = pd.read_csv('city_pairs.csv', names=['city2', 'city1'])
pairs = pd.concat([pairs1, pairs2])

# create adjacency matrix
adjacency = pd.crosstab(pairs['city1'], pairs['city2'])

# create graph object with NetworkX library
g = nx.from_pandas_adjacency(adjacency)

# run PageRank algorithm and add result to matrix
rank = nx.pagerank(g, alpha=0.85)
adjacency['rank'] = pd.Series(rank)

adjacency = adjacency.sort_values(by='rank', ascending=False)

# relabel columns
short = [x.replace(' ', '')[:3] for x in adjacency.columns]
adjacency.set_axis(1, short)

print(adjacency)

# color by city state
cities = pd.read_csv('cities.csv', names=['state'], index_col=0)
# cities = pd.read_csv('cities.csv', names=['city', 'state'])
col = {'safe': 0.0, 'live': 0.5, 'dead': 1.0}
cities['color'] = cities['state'].apply(col.get)
colors = [cities.loc[city]['color'] for city in g.nodes()]
plt.figure()
nx.draw(g, node_color=colors, labels=dict(zip(g.nodes(), g.nodes())))

plt.show()
