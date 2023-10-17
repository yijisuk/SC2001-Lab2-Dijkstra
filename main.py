from data_generator.main_generator import MainGenerator
from runtime_analysis.runtime_analysis import RuntimeAnalysis


if __name__ == "__main__":

    MG = MainGenerator()
    mixed_graphs, organized_graphs = MG.batch_generation(5)

    rta_incomplete = RuntimeAnalysis("incomplete", mixed_graphs)
    rta_incomplete.dijkstra_runtime_analysis()

    rta_complete = RuntimeAnalysis("complete", organized_graphs)
    rta_complete.dijkstra_runtime_analysis()