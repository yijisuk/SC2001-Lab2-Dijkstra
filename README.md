# SC2001-Lab2-Dijkstra

Empirical time complexity comparison on Dijkstra's algorithm's two implementation cases: 
<br>(a) using a linear array as a priority queue
<br>(b) using a minimizing heap as a priority queue

## Answering the Questions
### (a) Theoretical and Empirical Time Complexity Analysis, using a Linear Array

**Step 1: Finding the vertex with minimum distance value from the current vertex** 

> **O(V)** time, since all vertices should be scanned through, to extract the vertex with the minimum distance.

**Step 2: Updating vertex distance values**

> **O(V)** time, since every time a vertex gets picked, the distance value of other vertices should be updated, where the data lies on an adjacency matrix.

**Overall Time Complexity**

> Each operation takes **O(V)** time, which is repeated for **V** times, thus the overall time complexity would be **O(V^2)**.

### (b) Theoretical and Empirical Time Complexity Analysis, using a Minimizing Heap

**Step 1: Finding the vertex with minimum distance value from the current vertex**

- **Step1-1) Insertion into the minimizing heap**

  > First starting, all vertices should be inserted to the heap. This takes **O(VlogV)** since **V** elements are inserted, and each insertion takes **O(logV)**.

- **Step1-2) Extraction of the minimum element from the heap**
  > Each extraction (finding the vertex with minimum distance value) from the heap takes **(OlogV) time. Since this is repeated through all vertices, this part takes **O(VlogV)**.

> The overall time complexity for Step 1 would be **O(VlogV)**.

**Step 2: Updating vertex distance values**

> Updating the distance value of other vertices is done through using *decrease key operation*, which takes **O(logV) time in a binary heap. If all edges are considered the overall time for this operation would be **O(ElogV)**.

**Overall Time Complexity**

> Step 1 takes **O(VlogV)**, Step 2 takes **O(ElogV)**. Combining both, the overall time complexity would be **O((V+E)logV)**

### (c) Comparison and Recommendation

From the theoretical analysis, it's evident that the adjacency matrix with an array approach has a time complexity of $O(V^2)$, while the adjacency list with minimizing heap has a time complexity of $O((V + E) log V)$.  

#### When is using an Array as a Priority Queue Recommended?
> The array for priority queue is optimal when the V size is small.

When the number of vertices $V$ is small, the difference between $V^2$ and $V log V$ might not be significant. In such cases, the overhead introduced by the minimizing heap (like balancing the heap after every operation) might make the array-based approach slightly faster. 

![image](https://github.com/yijisuk/SC2001-Lab2-Dijkstra/assets/63234184/471ad193-d6d4-4216-baab-439d1a389161)


#### When is using a Minimizing Heap as a Priority Queue Recommended?
> A minimizing heap is more efficient as V grows larger.

As $V$ grows larger, the quadratic growth of $V^2$ will make the array approach increasingly slower compared to the log-linear growth of $V log V$.

![image](https://github.com/yijisuk/SC2001-Lab2-Dijkstra/assets/63234184/78594ef9-4cf8-4f61-87d6-ad9c82c848b6)
