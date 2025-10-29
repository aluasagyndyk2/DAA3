#  Minimum Spanning Tree (MST) Algorithms Comparison

##  1. Introduction
This project focuses on the implementation and comparison of two well-known Minimum Spanning Tree (MST) algorithms: **Kruskal’s Algorithm** and **Prim’s Algorithm**.  
The main objective is to analyze how these algorithms perform in terms of **time efficiency**, **implementation complexity**, and **suitability for different types of graphs**.

A **Minimum Spanning Tree** of a connected, weighted, and undirected graph is a subset of edges that connects all vertices with the **minimum total edge weight** and without any cycles.

---

##  2. Objectives
The key objectives of this project are:
1. To understand the working principles of MST algorithms (Kruskal and Prim).  
2. To implement both algorithms in **Java**.  
3. To read graph input data from a **JSON file**.  
4. To compare performance based on the number of nodes and edges.  
5. To analyze and interpret the results.

---


### 3. Steps Performed
1. Parse the JSON input file and create graph structures (nodes and weighted edges).  
2. Implement Kruskal’s and Prim’s algorithms separately.  
3. Measure execution time for each algorithm.  
4. Display results and MST edges.  
5. Compare efficiency and complexity.

---

##  4. Results and Analysis
--- Kruskal's MST ---
Edges in MST:
A - C (3)
C - D (2)
B - C (4)
E - D (6)
Total Weight: 15
Execution Time: 0.0021 sec

--- Prim's MST ---
Edges in MST:
A - C (3)
C - D (2)
D - E (6)
B - C (4)
Total Weight: 15
Execution Time: 0.0018 sec

### 4.2 Comparison Table

| Criteria | Kruskal’s Algorithm | Prim’s Algorithm |
|-----------|----------------------|------------------|
| **Approach** | Edge-based (Sorts all edges) | Vertex-based (Selects nearest) |
| **Data Structures Used** | Union-Find, Edge List | Priority Queue, Adjacency Matrix |
| **Best For** | Sparse graphs | Dense graphs |
| **Time Complexity** | O(E log E) | O(E + V log V) |
| **Ease of Implementation** | Simple to implement | Slightly complex |
| **Observed Time (Example)** | 2.1 ms | 1.8 ms |

---

##  5. Interpretation
From the experimental results, it can be observed that:
- **Prim’s algorithm** tends to perform slightly faster on **dense graphs** due to its vertex-based selection strategy.  
- **Kruskal’s algorithm** performs well on **sparse graphs**, as fewer edges need to be sorted.  
- Both algorithms always produce the same total MST weight, verifying correctness.

---

##  6. Conclusion
Both **Kruskal’s** and **Prim’s** algorithms efficiently construct the Minimum Spanning Tree for a given graph.  
However, the choice between them depends on the graph’s density and structure:
- Use **Kruskal’s** for sparse graphs (fewer edges).  
- Use **Prim’s** for dense graphs (many edges).  

This project enhanced understanding of **graph theory**, **greedy algorithms**, and **time complexity analysis** in real-world applications of data structures.




### 4.1 Sample Output
