# City Transport Network Optimization

## 1. Definition

This project implements an **optimization system for city transport networks** using two classical graph algorithms:  
**Prim's Algorithm** and **Kruskal's Algorithm**.  
The goal is to determine the **Minimum Spanning Tree (MST)** of each transport network, minimizing the total connection cost between all nodes (e.g., stations, intersections, or city districts).

Both algorithms were implemented in **Python** following Clean Code principles, with clear structure, documentation, and modular design.

---

## 2. Project Structure

```
CityTransportOptimization/
│
├── src/
│   ├── main.py              # Main program controller
│   ├── prim.py              # Implementation of Prim's algorithm
│   ├── kruskal.py           # Implementation of Kruskal's algorithm
│   ├── utils.py             # Helper functions for JSON I/O
│
├── data/
│   ├── input.json           # Example input file (city graphs)
│   ├── output.json          # Program output file (generated automatically)
│
├── report/
│   ├── report.md            # Analytical report (results and interpretation)
│
└── README.md                # This documentation file
```

---

## 3. How to Run the Program

1. Make sure you have **Python 3.8+** installed.  
2. Open the project in your IDE (IntelliJ, PyCharm, or VS Code).  
3. Run the main file:
   ```bash
   python src/main.py
   ```
4. The program will read data from `data/input.json` and automatically generate the results in `data/output.json`.

---

## 4. Analytical Report

### 4.1 Results

| Algorithm | Graph ID | Total Weight | Operations Count | Execution Time (ms) |
|------------|-----------|---------------|------------------|---------------------|
| Prim       | 1         | 15            | 22               | 0.12                |
| Kruskal    | 1         | 15            | 18               | 0.09                |
| Prim       | 2         | 27            | 34               | 0.15                |
| Kruskal    | 2         | 27            | 29               | 0.11                |

*(Note: The numbers are example results based on the current dataset.)*

---

### 4.2 Interpretation

- **Prim’s Algorithm** grows the MST by continuously adding the lowest-weight edge connected to the existing tree.  
  It performs slightly more operations but is efficient for **dense graphs**.

- **Kruskal’s Algorithm** sorts all edges and connects components step-by-step, ensuring no cycles form.  
  It is generally faster for **sparse graphs** due to fewer edge comparisons.

- The **total weights** of MSTs are equal, which confirms the **correctness** of both algorithms —  
  they produce the same optimal result, but with different computational behavior.

---

### 4.3 Comparison

| Aspect | Prim | Kruskal |
|--------|------|----------|
| Data structure used | Priority Queue (Min Heap) | Union-Find (Disjoint Sets) |
| Suitable for | Dense graphs | Sparse graphs |
| Speed | Slightly slower | Slightly faster |
| Implementation complexity | Moderate | High |
| Memory usage | Higher | Lower |

---

### 4.4 Conclusion

Both Prim and Kruskal algorithms successfully find the **Minimum Spanning Tree** of a city transport network.  
However, their efficiency depends on the graph’s structure:

- For **dense urban networks**, Prim’s algorithm performs better with adjacency matrices.  
- For **sparse regional connections**, Kruskal’s algorithm is more efficient.  

This project demonstrates that by comparing multiple algorithmic approaches,  
we can choose the most suitable one to **optimize infrastructure costs and improve transport planning efficiency**.

---

## 5. Future Improvements

- Implement Dijkstra’s algorithm for shortest paths between key stations.  
- Integrate visualization of MSTs using libraries like `networkx` or `matplotlib`.  
- Extend input format to support weighted directed graphs.

---

## 6. Author

**Developed by:** Alua Sagyndyk  
**Year:** 2025  
**Course:** Design and Analysis of Algorithms
