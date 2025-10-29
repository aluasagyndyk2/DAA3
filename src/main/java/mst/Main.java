package mst;

import com.google.gson.*;
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        String inputPath = "src/main/resources/ass_3_input.json";
        String outputPath = "src/main/resources/ass_3_output.json";

        try {
            String json = new String(Files.readAllBytes(Paths.get(inputPath)));
            JsonObject root = JsonParser.parseString(json).getAsJsonObject();
            JsonArray graphs = root.getAsJsonArray("graphs");

            for (JsonElement g : graphs) {
                JsonObject graphObj = g.getAsJsonObject();
                Graph graph = Graph.fromJson(graphObj);

                System.out.println("\n     Graph ID: " + graphObj.get("id").getAsInt() + "   ");

                System.out.println("Prim’s MST:");
                graph.runPrim();

                System.out.println("\nKruskal’s MST:");
                graph.runKruskal();
            }

            Files.write(Paths.get(outputPath), "MST results generated.".getBytes());
            System.out.println("\nResults saved to " + outputPath);
        } catch (IOException e) {
            System.out.println("Input file 'ass_3_input.json' not found in src/main/resources/");
        }
    }
}
