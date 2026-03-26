# 🚗 Shortest Route Optimization System
### (Ride-Sharing Route Finder using Dijkstra’s Algorithm)

---

## 📌 Project Overview
This project simulates a route optimization system similar to ride-sharing applications like Rapido, Uber, and Google Maps. It computes the shortest path between two locations using **Dijkstra’s Algorithm** on a weighted graph.

The system models real-world locations (Bangalore-based) as nodes and roads as edges with distances.

---

## 🎯 Objectives
- Model a road network using graph data structure
- Implement Dijkstra’s shortest path algorithm
- Compute shortest route between source and destination
- Display path, distance, and traversal steps
- Provide Google Maps navigation link
- Visualize graph structure

---

## 🧠 Data Structures Used
- **Graph (Adjacency List)** → Efficient storage of nodes and edges
- **Priority Queue (Min Heap)** → Used in Dijkstra for optimization
- **Dictionary** → To store distances and previous nodes

---

## ⚙️ Algorithm Used
### Dijkstra’s Algorithm

Steps:
1. Initialize all distances as infinity
2. Set source node distance to 0
3. Use a priority queue to pick minimum distance node
4. Update distances of neighboring nodes
5. Track previous nodes for path reconstruction
6. Repeat until shortest path is found

---

## ⏱️ Complexity Analysis
- **Time Complexity:** O((V + E) log V)
- **Space Complexity:** O(V)

Where:
- V = Number of vertices (locations)
- E = Number of edges (roads)

---

## 🚀 Features
- ✅ Find shortest path between locations
- ✅ Display full route (step-by-step)
- ✅ Show total distance
- ✅ Show distance from source to all locations
- ✅ Handle invalid inputs
- ✅ Google Maps route link generation
- ✅ Graph visualization using NetworkX

---

## 🗺️ Example

**Input:**


**Output:**


---

## 🌍 Google Maps Integration
The project generates a direct navigation link:



This allows users to view the computed route in real-world maps.

---

## 📊 Graph Visualization
The system uses:
- `networkx`
- `matplotlib`

To visually display the road network graph.

---

## ⚠️ Limitations
- Does not support negative edge weights
- Uses static graph (no real-time traffic)
- Does not use live GPS data

---

## 🔮 Future Enhancements
- GUI interface using Tkinter or Web App
- Real-time traffic integration
- A* Algorithm implementation
- Dynamic graph updates
- Integration with real map APIs

---

## 🛠️ Technologies Used
- Python 3
- heapq (Priority Queue)
- NetworkX
- Matplotlib

---

## ▶️ How to Run

```bash
python main.py


---

# 📄 ✅ REPORT NOTES (FINAL VERSION)

Paste into `report_notes.txt`:

```text
PROJECT TITLE:
Shortest Route Optimization for Ride-Sharing Applications Using Dijkstra’s Algorithm

------------------------------------------------------------

1. INTRODUCTION
Route optimization plays a crucial role in modern ride-sharing and navigation systems such as Rapido, Uber, and Google Maps. These systems must efficiently determine the shortest path between two locations to minimize travel time and distance.

This project demonstrates how graph-based algorithms can be used to solve such problems effectively.

------------------------------------------------------------

2. PROBLEM STATEMENT
Given a road network represented as a weighted graph:
- Nodes represent locations
- Edges represent roads
- Weights represent distance

The goal is to find the shortest path between a source and a destination.

------------------------------------------------------------

3. OBJECTIVES
- To model a road network using graph data structure
- To implement Dijkstra’s Algorithm
- To compute shortest route between locations
- To display path and total distance
- To analyze algorithm efficiency

------------------------------------------------------------

4. DATA STRUCTURES USED
- Graph (Adjacency List Representation)
- Priority Queue (Min Heap)
- Dictionaries for storing distances and paths

------------------------------------------------------------

5. ALGORITHM USED
Dijkstra’s Algorithm

Working:
1. Assign infinite distance to all nodes
2. Set source distance to 0
3. Select node with minimum distance
4. Update distances of adjacent nodes
5. Repeat until all nodes are processed

------------------------------------------------------------

6. SYSTEM DESIGN
Input:
- Source location
- Destination location

Process:
- Apply Dijkstra’s algorithm
- Compute shortest path

Output:
- Shortest path
- Total distance
- Step-by-step traversal

------------------------------------------------------------

7. IMPLEMENTATION
The project is implemented using Python.

Modules:
- graph_data.py → Graph representation
- dijkstra_algo.py → Algorithm implementation
- utils.py → Path reconstruction & map link
- main.py → User interface
- test_cases.py → Testing module

------------------------------------------------------------

8. RESULTS
The system successfully computes:
- Shortest path between locations
- Distance from source to destination
- Distance to all nodes

------------------------------------------------------------

9. COMPLEXITY ANALYSIS
Time Complexity:
O((V + E) log V)

Space Complexity:
O(V)

------------------------------------------------------------

10. LIMITATIONS
- Does not handle negative weights
- No real-time traffic updates
- Static dataset

------------------------------------------------------------

11. FUTURE SCOPE
- GUI-based application
- Integration with real-time navigation APIs
- Implementation of A* algorithm
- Large-scale map datasets

------------------------------------------------------------

12. CONCLUSION
The project successfully demonstrates the use of Dijkstra’s Algorithm for shortest path computation. It highlights the importance of graph data structures in solving real-world problems like route optimization.

------------------------------------------------------------