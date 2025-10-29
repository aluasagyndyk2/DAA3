package mst;

import java.util.*;

public class Kruskal {
    public static void kruskalMST(List<String> nodes, List<Edge> edges) {
        List<Edge> mst = new ArrayList<>();
        UnionFind uf = new UnionFind(nodes);

        edges.sort(Comparator.comparingInt(e -> e.weight));

        for (Edge e : edges) {
            if (uf.union(e.from, e.to)) {
                mst.add(e);
            }
        }

        for (Edge e : mst)
            System.out.println(e.from + " - " + e.to + " : " + e.weight);
    }
}
