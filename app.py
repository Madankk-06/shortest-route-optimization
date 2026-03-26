import streamlit as st
from graph_data import graph
from dijkstra_algo import dijkstra
from utils import get_path, generate_google_maps_link

st.set_page_config(page_title="Route Optimization", layout="centered")

st.title("🚗 Shortest Route Optimization System")
st.markdown("Find shortest path like Rapido / Google Maps")

# Dropdowns
locations = list(graph.keys())

source = st.selectbox("Select Source Location", locations)
destination = st.selectbox("Select Destination Location", locations)

if st.button("Find Shortest Route"):

    if source == destination:
        st.warning("Source and destination are the same.")
    else:
        distances, previous = dijkstra(graph, source, destination)
        path = get_path(previous, source, destination)

        if not path:
            st.error("No path found.")
        else:
            st.success("Route Found!")

            st.subheader("📍 Shortest Path")
            st.write(" ➝ ".join(path))

            st.subheader("📏 Total Distance")
            st.write(f"{distances[destination]} km")

            st.subheader("🧭 Step-by-step Route")
            for i in range(len(path) - 1):
                st.write(f"{path[i]} ➝ {path[i+1]}")

            # Google Maps link
            link = generate_google_maps_link(source, destination)

            st.subheader("🌍 Open in Google Maps")
            st.markdown(f"[Click here to view route]({link})")
import matplotlib.pyplot as plt
import networkx as nx

if st.button("Show Graph Map"):
    G = nx.Graph()

    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

    st.pyplot(fig)