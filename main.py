from graph_data import graph
from dijkstra_algo import dijkstra
from utils import get_path
from visualize_graph import draw_graph

def line():
    print("=" * 50)

def display_locations():
    line()
    print("Available Locations:")
    for location in graph.keys():
        print("-", location)
    line()

def find_shortest_route():
    from utils import get_path, generate_google_maps_link
    display_locations()

    start = input("Enter source location: ").strip()
    end = input("Enter destination location: ").strip()

    if start not in graph or end not in graph:
        print("\nInvalid source or destination.")
        return

    if start == end:
        print("\nSource and destination are same.")
        print("Distance: 0 km")
        return

    distances, previous = dijkstra(graph, start, end)
    path = get_path(previous, start, end)

    if not path:
        print("\nNo path found.")
    else:
        line()
        print("=== ROUTE RESULT ===")
        print("Source:", start)
        print("Destination:", end)

        print("\nShortest Path:")
        print(" -> ".join(path))

        print("\nTotal Distance:", distances[end], "km")

        print("\nStep-by-step Traversal:")
        for i in range(len(path)-1):
            print(f"{path[i]} → {path[i+1]}")
        line()
        link = generate_google_maps_link(start, end)
        print("\nOpen in Google Maps:")
        print(link)

def show_all_distances():
    display_locations()
    start = input("Enter source location: ").strip()

    if start not in graph:
        print("Invalid source.")
        return

    distances, _ = dijkstra(graph, start)

    line()
    print("Distance from", start)
    for node, dist in distances.items():
        print(f"{node}: {dist} km")
    line()

def main():
    while True:
        line()
        print("Shortest Route Optimization System")
        print("1. Display Locations")
        print("2. Find Shortest Route")
        print("3. Show Distance to All Locations")
        print("4. Show Graph Map")
        print("5. Exit")
        line()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_locations()
        elif choice == "2":
            find_shortest_route()
        elif choice == "3":
            show_all_distances()
        elif choice == "4":
            draw_graph()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()