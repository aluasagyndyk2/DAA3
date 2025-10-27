# kruskal.py
# Implementation of Kruskal's algorithm for MST with Union-Find (Disjoint Set).
# Counts key operations and measures execution time.

import time
from typing import List, Dict, Tuple

class UnionFind:
    def __init__(self, elements):
        # parent and rank dictionaries
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}
        self.find_ops = 0
        self.union_ops = 0

    def find(self, x):
        self.find_ops += 1
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.union_ops += 1
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def kruskal_mst(nodes: List[str], edges: List[Dict]) -> Dict:
    """
    Compute MST using Kruskal's algorithm.
    Returns a dictionary with mst_edges (list), total_cost, operations_count, execution_time_ms.
    """
    start_time = time.perf_counter()
    # sort edges by weight
    # Count comparisons as number of edges log or just number of comparisons during sorting is abstract;
    # we will approximate by len(edges) * log2(len(edges)) for reporting simplicity.
    edges_sorted = sorted(edges, key=lambda e: e['weight'])
    sort_comparisons = int(len(edges) * (len(edges).bit_length())) if len(edges) > 0 else 0

    uf = UnionFind(nodes)
    mst_edges = []
    total_cost = 0.0
    operations = 0

    for e in edges_sorted:
        u, v, w = e['from'], e['to'], e['weight']
        operations += 1  # comparing/considering this edge
        # find roots
        ru = uf.find(u)
        rv = uf.find(v)
        operations += uf.find_ops  # accumulate find ops counted in UnionFind
        # if in different sets, union them and include edge
        if ru != rv:
            merged = uf.union(ru, rv)
            operations += uf.union_ops  # accumulate union ops counted in UnionFind
            if merged:
                mst_edges.append({"from": u, "to": v, "weight": w})
                total_cost += w
        # reset per-edge counters in uf to avoid double counting later
        uf.find_ops = 0
        uf.union_ops = 0

        if len(mst_edges) == len(nodes) - 1:
            break

    # Include sorting comparisons as operations
    operations += sort_comparisons

    end_time = time.perf_counter()
    exec_ms = (end_time - start_time) * 1000.0
    return {
        "mst_edges": mst_edges,
        "total_cost": int(total_cost) if float(total_cost).is_integer() else total_cost,
        "operations_count": operations,
        "execution_time_ms": round(exec_ms, 4)
    }
