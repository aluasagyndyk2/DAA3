# main.py
# Entry point: reads input.json, runs Prim and Kruskal for each graph,
# and writes output.json. All comments and identifiers are in English.

import os
import json
from utils import read_input, write_output
from prim import prim_mst
from kruskal import kruskal_mst

def process_graph(graph):
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    results = {}

    # Input stats
    results["input_stats"] = {
        "vertices": len(nodes),
        "edges": len(edges)
    }

    # Run Prim
    prim_res = prim_mst(nodes, edges)
    results["prim"] = prim_res

    # Run Kruskal
    kruskal_res = kruskal_mst(nodes, edges)
    results["kruskal"] = kruskal_res

    return results

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "..", "data", "input.json")
    output_path = os.path.join(base_dir, "..", "data", "output.json")

    data = read_input(input_path)
    graphs = data.get("graphs", [])

    final_results = {"results": []}

    for g in graphs:
        res = {"graph_id": g.get("id")}
        res.update(process_graph(g))
        final_results["results"].append(res)

    write_output(output_path, final_results)
    print(f"Output written to {output_path}")

if __name__ == "__main__":
    main()
