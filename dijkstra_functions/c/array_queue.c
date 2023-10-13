#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>


int minDistance(int dist[], int sptSet[], int V);
void printSolution(int dist[]);
double dijkstra(int **graph, int V, int src);


double dijkstra(int **graph, int V, int src)
{
    // Start the clock to measure the time taken
    clock_t start_time, end_time;
    double cpu_time_used;

    start_time = clock();

    // dist[i] will hold the shortest distance from src to node i
    int dist[V];

    // sptSet[i] will be true if node i is included in the shortest path tree
    int sptSet[V];

    // Initialize all distances as INFINITE and set sptSet[] as false
    for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, sptSet[i] = 0;

    // Distance from source to itself is always 0
    dist[src] = 0;

    // Find the shortest path for all vertices
    for (int count = 0; count < V - 1; count++)
    {
        // Pick the minimum distance vertex from the set of vertices not yet processed
        int u = minDistance(dist, sptSet, V);

        // Mark the picked vertex as processed
        sptSet[u] = 1;

        // Update dist value of the adjacent vertices of the picked vertex
        for (int v = 0; v < V; v++)
        {
            // Update dist[v] only if it is not in sptSet, there is an edge from u to v,
            // and the total weight of the path from src to v through u is smaller than dist[v]
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
            {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    // Stop the clock and calculate the time taken
    end_time = clock();
    cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    // Return the time taken for the algorithm to run
    return cpu_time_used;
}


// Loops through all vertices
// and identifies with the vertex with the smallest distance
int minDistance(int dist[], int sptSet[], int V)
{
	int min = INT_MAX;
	int min_index;

	for (int v = 0; v < V; v++)
		if (sptSet[v] == 0 && dist[v] <= min)
		{
			min = dist[v];
			min_index = v;
		}

	return min_index;
}