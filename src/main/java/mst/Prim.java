package mst;

import java.util.*;

public class Prim {
    public static void primMST(List<String> nodes, List<Edge> edges) {
        Set<String> visited = new HashSet<>();
        List<Edge> mst = new ArrayList<>();
        String start = nodes.get(0);
        visited.add(start);

        while (visited.size() < nodes.size()) {
            Edge minEdge = null;
            for (Edge e : edges) {
                if (visited.contains(e.from) && !visited.contains(e.to)) {
                    if (minEdge == null || e.weight < minEdge.weight)
                        minEdge = e;
                }
            }
            if (minEdge == null) break;
            mst.add(minEdge);
            visited.add(minEdge.to);
        }

        for (Edge e : mst)
            System.out.println(e.from + " - " + e.to + " : " + e.weight);
    }
}
