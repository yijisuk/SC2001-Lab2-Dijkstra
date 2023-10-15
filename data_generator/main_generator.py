import os
import numpy as np
import pandas as pd
from tqdm import tqdm


class MainGenerator:

    def __init__(self):
        
        pass

    def batch_generation(self, batch_size):

        graphs_agg = []

        for _ in tqdm(range(1, batch_size+1)):

            graphs = self.single_batch()
            graphs_agg.append(graphs)

        return graphs_agg


    def single_batch(self):

        # Initialize an empty list to hold DataFrames
        dfs = []

        # Generate graphs for sizes 100 to 5000, with a step size of 100
        for size in range(100, 5001, 100):

            graph = np.random.randint(0, 100, size=(size, size))
            np.fill_diagonal(graph, 0)
            df_small = pd.DataFrame({'V': [size], 'graph': [graph]})
            dfs.append(df_small)

        agg = pd.concat(dfs, ignore_index=True)

        return agg