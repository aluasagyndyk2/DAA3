# Assignment 3 - Minimum Spanning Tree (Java, IntelliJ, Maven)

Project is a ready-to-open Maven project for IntelliJ IDEA. It implements Prim's and Kruskal's algorithms,
reads `ass_3_input.json` from `src/main/resources/`, runs both algorithms for each graph, measures execution time (ms),
counts operations with a deterministic metric, and writes `ass_3_output.json` to `src/main/resources/`.

How to open:
1. Open IntelliJ IDEA -> Open -> select this project's folder (where pom.xml is).
2. Let Maven import dependencies (Gson).
3. Run `mst.Main` (Run -> Main.java).
4. Output file will be created at `src/main/resources/ass_3_output.json`.

You can also run from command line:
```
mvn -q -DskipTests package
mvn -q -DskipTests exec:java -Dexec.mainClass="mst.Main" -Dexec.args="src/main/resources/ass_3_input.json src/main/resources/ass_3_output.json"
```

