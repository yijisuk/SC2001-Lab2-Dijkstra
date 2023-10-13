import os
import numpy as np
import pandas as pd
from tqdm import tqdm


class MainGenerator:

    def __init__(self):
        
        pass

    def batch_generation(self, batch_size):

        graphs_agg = []

        for i in tqdm(range(1, batch_size+1)):

            graphs = self.single_batch()
            graphs_agg.append(graphs)

        return graphs_agg


    def single_batch(self):

        # Initialize an empty list to hold DataFrames
        dfs = []

        # Generate graphs for sizes 10 to 2000, with a step size of 10
        for size in range(10, 2001, 10):
            graph = np.random.randint(0, 100, size=(size, size))
            np.fill_diagonal(graph, 0)
            df_small = pd.DataFrame({'V': [size], 'graph': [graph]})
            dfs.append(df_small)

        # Generate graphs for sizes 10^4 to 10^5, with a step size of 100
        # for size in range(10**4, 10**5 + 1, 10**4):
        #     graph = np.random.randint(0, 100, size=(size, size))
        #     np.fill_diagonal(graph, 0)
        #     df_large = pd.DataFrame({'V': [size], 'graph': [graph]})
        #     dfs.append(df_large)

        final_df = pd.concat(dfs, ignore_index=True)
        return final_df