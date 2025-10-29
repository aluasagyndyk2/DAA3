package mst;

import java.util.*;

public class UnionFind {
    Map<String, String> parent = new HashMap<>();

    public UnionFind(List<String> nodes) {
        for (String n : nodes) parent.put(n, n);
    }

    public String find(String x) {
        if (!parent.get(x).equals(x))
            parent.put(x, find(parent.get(x)));
        return parent.get(x);
    }

    public boolean union(String a, String b) {
        String rootA = find(a), rootB = find(b);
        if (rootA.equals(rootB)) return false;
        parent.put(rootA, rootB);
        return true;
    }
}
