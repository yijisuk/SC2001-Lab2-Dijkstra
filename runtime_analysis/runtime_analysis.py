import os
import numpy as np
import ctypes
from tqdm import tqdm

from dijkstra_functions.dijkstra_functions import Dijkstra_Functions


class RuntimeAnalysis:

    def __init__(self, prefix, graphs):

        self.DF = Dijkstra_Functions()
        self.base_save_path = os.path.join("data", prefix)
        self.prefix = prefix
        self.graphs = graphs

        if not os.path.exists(self.base_save_path):
            os.makedirs(self.base_save_path)


    def dijkstra_runtime_analysis(self):

        for i, graph in tqdm(enumerate(self.graphs)):

            df = self.run_on_single_df(graph)
            df.to_csv(os.path.join(self.base_save_path, f"graphs_rta_{i+1}.csv"), index=False)


    def run_on_single_df(self, df):

        df['ar_time_taken'] = np.nan
        df['mh_time_taken'] = np.nan

        for index, row in df.iterrows():
            V = row['V']
            graph_np = np.array(row['graph'], dtype=np.int32)

            graph_ctypes = (ctypes.POINTER(ctypes.c_int) * V)()
            for i in range(V):
                graph_ctypes[i] = graph_np[i].ctypes.data_as(
                    ctypes.POINTER(ctypes.c_int))

            # Call the dijkstra functions
            src = 0  # Starting vertex
            ar_time_taken = float(
                self.DF.array_queue.dijkstra(graph_ctypes, V, src))
            mh_time_taken = float(
                self.DF.min_heap_queue.dijkstra(graph_ctypes, V, src))

            # Save the time taken into the DataFrame
            df.at[index, 'ar_time_taken'] = ar_time_taken
            df.at[index, 'mh_time_taken'] = mh_time_taken

        return df