package HVAC;

import java.util.LinkedList;


    public class HVAC 
    {
    // A user define class to represent a graph where a graph is an array of adjacency lists. 
    // Size of array will be V (number of vertices in graph) which will be the number of equipments
        static class Graph 
        { 
            int V; 
            LinkedList<Equipment> adjListArray[]; 
              
            // constructor  
            Graph(int V) 
            { 
                
                this.V = V; 
                  
                // define the size of array as number of vertices 
                adjListArray = new LinkedList[V]; 
                  
                // Create a new list for each vertex such that adjacent nodes can be stored 
                for(int i = 0; i < V ; i++){ 
                    adjListArray[i] = new LinkedList<Equipment>(); 
                } 
            } 
        } 
          
        // Adds an edge to an undirected graph 
        static void addEdge(Graph graph, Equipment src, Equipment dest) 
        { 
            int srcInt = Integer.parseInt(src.getEquipmentId());
            int destInt = Integer.parseInt(dest.getEquipmentId());
            
            // Add an edge from src to destination  
            graph.adjListArray[srcInt].add(dest); 
              
            // Since graph is undirected, add an edge from dest to src also 
            graph.adjListArray[destInt].add(src); 
        } 
           
        // function to print the adjacency list representation of graph 
        static void printGraph(Graph graph) 
        {        
            for(int v = 0; v < graph.V; v++) 
            { 
                System.out.println("Adjacency list of equipment "+ v); 
                System.out.print("head"); 
                for(Equipment eqp: graph.adjListArray[v]){ 
                    System.out.print(" -> " + eqp.getEquipmentId()); 
                } 
                System.out.println("\n"); 
            } 
        }
}
