package HVAC;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class Main {
    
    public Main() {
        super();
    }

    public static void main(String[] args) {
        // create the graph with 7 vertices which are equipments in our case
                int V = 7; 
                
                // Assuming test cases to solve the problem
                Equipment e1 = new Equipment("1", new Sensor(45.5f,12.5f,true));
                Equipment e2 = new Equipment("3", new Sensor(55.6f,34.3f,false));
                Equipment e3 = new Equipment("5", new Sensor(65.34f,56,false));
                Equipment e4 = new Equipment("2", new Sensor(102,34,true));
                Equipment e5 = new Equipment("4", new Sensor(100.10f,78,true));
                Equipment e6 = new Equipment("6", new Sensor(120,67,true));
                
                HVAC.Graph graph = new HVAC.Graph(V); 
                
                // connect the equipments with edges which in our case is the airducts.
                HVAC.addEdge(graph, e1, e2); 
                HVAC.addEdge(graph, e1, e5); 
                HVAC.addEdge(graph, e2, e3); 
                HVAC.addEdge(graph, e2, e3); 
                HVAC.addEdge(graph, e2, e5); 
                HVAC.addEdge(graph, e3, e4); 
                HVAC.addEdge(graph, e4, e5);
                HVAC.addEdge(graph, e5, e6); 
               
                // print the adjacency list representation of the above graph structure 
                HVAC.printGraph(graph);
                
                
                // iterate through the map to find the equipment
                Map<String,Sensor> e = new HashMap<>();
                for(int v = 0; v < graph.V; v++) 
                { 
                    for(Equipment eq: graph.adjListArray[v]){
                        
                        String eqId= eq.getEquipmentId();
                        float temp = eq.getSensors().getTemperature();
                        boolean status= eq.getSensors().getStatus();
                        if(status){
                            if(temp>100){
                               e.put(eqId,eq.getSensors());
                            }
                        }
                    } 
                    //System.out.println("\n"); 
                }
                
                // print the equipments found
                System.out.println("Equipments which are ON and have temperature greater than 100 are: ");
                    Iterator it = e.entrySet().iterator();
                    while (it.hasNext()) {
                        Map.Entry entry = (Map.Entry)it.next();
                        System.out.println(entry.getKey() + " where " + entry  .getValue().toString());
                        it.remove(); // avoids a ConcurrentModificationException
                    }
                }    
                
                
}

