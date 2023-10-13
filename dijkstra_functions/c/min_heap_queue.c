#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>


typedef struct MinHeapNode
{
    int v;
    int dist;
} MinHeapNode;

typedef struct MinHeap
{
    int size;
    int capacity;
    int *pos;
    MinHeapNode **array;
} MinHeap;


MinHeapNode *createMinHeapNode(int v, int dist);
MinHeap *createMinHeap(int capacity);
void swapMinHeapNode(MinHeapNode **a, MinHeapNode **b);
void minHeapify(MinHeap *minHeap, int idx);
int isEmpty(MinHeap *minHeap);
void decreaseKey(MinHeap *minHeap, int v, int dist);
MinHeapNode *extractMin(MinHeap *minHeap);

double dijkstra(int **graph, int V, int src);


double dijkstra(int **graph, int V, int src)
{
    clock_t start_time, end_time;
    double cpu_time_used;

    start_time = clock();

    int dist[V];
    MinHeap *minHeap = createMinHeap(V);

    for (int v = 0; v < V; ++v)
    {
        dist[v] = INT_MAX;
        minHeap->array[v] = createMinHeapNode(v, dist[v]);
        minHeap->pos[v] = v;
    }

    minHeap->array[src] = createMinHeapNode(src, dist[src]);
    minHeap->pos[src] = src;
    dist[src] = 0;
    decreaseKey(minHeap, src, dist[src]);

    minHeap->size = V;

    while (!isEmpty(minHeap))
    {
        MinHeapNode *minHeapNode = extractMin(minHeap);
        int u = minHeapNode->v;

        for (int v = 0; v < V; ++v)
        {
            if (graph[u][v] && minHeap->pos[v] < minHeap->size && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
            {
                dist[v] = dist[u] + graph[u][v];
                decreaseKey(minHeap, v, dist[v]);
            }
        }
    }

    end_time = clock();
    cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    return cpu_time_used;
}


MinHeapNode *createMinHeapNode(int v, int dist)
{
    MinHeapNode *newNode = (MinHeapNode *)malloc(sizeof(MinHeapNode));
    newNode->v = v;
    newNode->dist = dist;
    return newNode;
}


MinHeap *createMinHeap(int capacity)
{
    MinHeap *minHeap = (MinHeap *)malloc(sizeof(MinHeap));
    minHeap->size = 0;
    minHeap->capacity = capacity;
    minHeap->pos = (int *)malloc(capacity * sizeof(int));
    minHeap->array = (MinHeapNode **)malloc(capacity * sizeof(MinHeapNode *));
    return minHeap;
}


void swapMinHeapNode(MinHeapNode **a, MinHeapNode **b)
{
    MinHeapNode *temp = *a;
    *a = *b;
    *b = temp;
}


void minHeapify(MinHeap *minHeap, int idx)
{
    int smallest, left, right;
    smallest = idx;
    left = 2 * idx + 1;
    right = 2 * idx + 2;

    if (left < minHeap->size && minHeap->array[left]->dist < minHeap->array[smallest]->dist)
    {
        smallest = left;
    }

    if (right < minHeap->size && minHeap->array[right]->dist < minHeap->array[smallest]->dist)
    {
        smallest = right;
    }

    if (smallest != idx)
    {
        MinHeapNode *smallestNode = minHeap->array[smallest];
        MinHeapNode *idxNode = minHeap->array[idx];

        minHeap->pos[smallestNode->v] = idx;
        minHeap->pos[idxNode->v] = smallest;

        swapMinHeapNode(&minHeap->array[smallest], &minHeap->array[idx]);
        minHeapify(minHeap, smallest);
    }
}


int isEmpty(MinHeap *minHeap)
{
    return minHeap->size == 0;
}


void decreaseKey(MinHeap *minHeap, int v, int dist)
{
    int i = minHeap->pos[v];
    minHeap->array[i]->dist = dist;

    while (i && minHeap->array[i]->dist < minHeap->array[(i - 1) / 2]->dist)
    {
        minHeap->pos[minHeap->array[i]->v] = (i - 1) / 2;
        minHeap->pos[minHeap->array[(i - 1) / 2]->v] = i;
        swapMinHeapNode(&minHeap->array[i], &minHeap->array[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}


MinHeapNode *extractMin(MinHeap *minHeap)
{
    if (isEmpty(minHeap))
    {
        return NULL;
    }

    MinHeapNode *root = minHeap->array[0];
    MinHeapNode *lastNode = minHeap->array[minHeap->size - 1];
    minHeap->array[0] = lastNode;

    minHeap->pos[root->v] = minHeap->size - 1;
    minHeap->pos[lastNode->v] = 0;

    --minHeap->size;
    minHeapify(minHeap, 0);

    return root;
}