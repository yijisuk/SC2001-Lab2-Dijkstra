from data_generator.main_generator import MainGenerator
from runtime_analysis.runtime_analysis import RuntimeAnalysis


if __name__ == "__main__":

    MG = MainGenerator()
    graphs = MG.batch_generation(5)

    RTA = RuntimeAnalysis(graphs)
    RTA.dijkstra_runtime_analysis()