# prim.py
# Implementation of Prim's algorithm for Minimum Spanning Tree (MST).
# Counts key operations and measures execution time.

import heapq
import time
from typing import List, Dict, Tuple

def prim_mst(nodes: List[str], edges: List[Dict]) -> Dict:
    """
    Compute MST using Prim's algorithm.
    Returns a dictionary with mst_edges (list), total_cost, operations_count, execution_time_ms.
    """
    start_time = time.perf_counter()
    # Build adjacency list
    adj = {n: [] for n in nodes}
    for e in edges:
        u, v, w = e['from'], e['to'], e['weight']
        adj[u].append((w, u, v))
        adj[v].append((w, v, u))

    operations = 0
    visited = set()
    mst_edges = []
    total_cost = 0.0

    # Use a heap (priority queue)
    # Start from the first node
    if not nodes:
        return {"mst_edges": [], "total_cost": 0, "operations_count": 0, "execution_time_ms": 0.0}

    start = nodes[0]
    visited.add(start)
    heap = []
    # push initial edges
    for item in adj[start]:
        heapq.heappush(heap, item)
        operations += 1  # heap push counted as an operation

    # Main loop
    while heap and len(visited) < len(nodes):
        w, u, v = heapq.heappop(heap)
        operations += 1  # heap pop
        operations += 1  # check visited
        if v in visited:
            continue
        # choose this edge
        visited.add(v)
        mst_edges.append({"from": u, "to": v, "weight": w})
        total_cost += w
        # add adjacent edges of v
        for item in adj[v]:
            # each push is counted
            heapq.heappush(heap, item)
            operations += 1

    end_time = time.perf_counter()
    exec_ms = (end_time - start_time) * 1000.0
    return {
        "mst_edges": mst_edges,
        "total_cost": int(total_cost) if float(total_cost).is_integer() else total_cost,
        "operations_count": operations,
        "execution_time_ms": round(exec_ms, 4)
    }
