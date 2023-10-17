import numpy as np
import pandas as pd
from tqdm import tqdm


class MainGenerator:

    def __init__(self):
        
        pass


    def batch_generation(self, batch_size):

        mixed_agg, organized_agg = [], []

        for _ in tqdm(range(1, batch_size+1)):

            mixed_graphs, organized_graphs = self.single_batch()
            mixed_agg.append(mixed_graphs)
            organized_agg.append(organized_graphs)

        return mixed_agg, organized_agg


    def single_batch(self):

        # Initialize empty lists to hold DataFrames
        mixed_dfs = []
        organized_dfs = []

        # Generate graphs for sizes 10 to 90, with a step size of 100
        mixed_dfs, organized_dfs = self.generate_batches(
            10, 91, 10, mixed_dfs, organized_dfs)

        # Generate graphs for sizes 100 to 5000, with a step size of 100
        mixed_dfs, organized_dfs = self.generate_batches(
            100, 5001, 100, mixed_dfs, organized_dfs)

        mixed_agg = pd.concat(mixed_dfs, ignore_index=True)
        organized_agg = pd.concat(organized_dfs, ignore_index=True)

        return mixed_agg, organized_agg
    

    def generate_batches(self, start_size, end_size, step_size, mixed_dfs, organized_dfs):

        for size in range(start_size, end_size, step_size):

            # Generate incomplete (random) graph
            mixed_df_small = self.generate_graph("incomplete", size)
            mixed_dfs.append(mixed_df_small)

            # Generate complete (best-case for Dijkstra) graph
            organized_df_small = self.generate_graph("complete", size)
            organized_dfs.append(organized_df_small)

        return mixed_dfs, organized_dfs


    def generate_graph(self, option, size):

        if option == "incomplete":

            mixed_graph = np.random.randint(0, 100, size=(size, size))
            np.fill_diagonal(mixed_graph, 0)
            df = pd.DataFrame(
                {'V': [size], 'graph': [mixed_graph]})

        elif option == "complete":

            organized_graph = np.zeros((size, size))
            for i in range(size):
                for j in range(i+1, size):
                    organized_graph[i, j] = j - i
                    organized_graph[j, i] = j - i
            np.fill_diagonal(organized_graph, 0)
            df = pd.DataFrame(
                {'V': [size], 'graph': [organized_graph]})

        return df