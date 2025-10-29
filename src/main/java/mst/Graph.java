package mst;

import com.google.gson.*;
import java.util.*;

public class Graph {
    List<String> nodes = new ArrayList<>();
    List<Edge> edges = new ArrayList<>();

    public static Graph fromJson(JsonObject json) {
        Graph g = new Graph();
        JsonArray nodes = json.getAsJsonArray("nodes");
        for (JsonElement n : nodes) g.nodes.add(n.getAsString());

        JsonArray edges = json.getAsJsonArray("edges");
        for (JsonElement e : edges) {
            JsonObject edge = e.getAsJsonObject();
            g.edges.add(new Edge(edge.get("from").getAsString(), edge.get("to").getAsString(), edge.get("weight").getAsInt()));
        }
        return g;
    }

    public void runPrim() {
        Prim.primMST(nodes, edges);
    }

    public void runKruskal() {
        Kruskal.kruskalMST(nodes, edges);
    }
}
