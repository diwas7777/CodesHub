/*
    Title: Dijkstra's Shortest Path Algorithm in C++
    Author: Your Name
    Description:
        This program implements Dijkstra’s Algorithm to find the shortest
        path from a single source vertex to all other vertices in a weighted graph.

    Why this project is valuable:
        - Demonstrates the use of graphs, priority queues, and adjacency lists
        - Efficient O((V + E) log V) implementation using STL
        - Useful for understanding pathfinding algorithms (core DSA concept)
*/

#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

// Define a pair to store (distance, node)
typedef pair<int, int> pii;

class Graph {
    int vertices;
    vector<vector<pii>> adj; // adjacency list: node -> [(neighbor, weight)]

public:
    // Constructor
    Graph(int V) {
        vertices = V;
        adj.resize(V);
    }

    // Add an edge to the graph
    void addEdge(int u, int v, int w) {
        adj[u].push_back({v, w});
        adj[v].push_back({u, w}); // for undirected graph
    }

    // Dijkstra’s algorithm implementation
    void dijkstra(int start) {
        vector<int> dist(vertices, INT_MAX);
        priority_queue<pii, vector<pii>, greater<pii>> pq;

        dist[start] = 0;
        pq.push({0, start});

        while (!pq.empty()) {
            int currentDist = pq.top().first;
            int currentNode = pq.top().second;
            pq.pop();

            // If a shorter path to currentNode has already been found, skip
            if (currentDist > dist[currentNode]) continue;

            // Explore neighbors
            for (auto &edge : adj[currentNode]) {
                int neighbor = edge.first;
                int weight = edge.second;

                if (dist[currentNode] + weight < dist[neighbor]) {
                    dist[neighbor] = dist[currentNode] + weight;
                    pq.push({dist[neighbor], neighbor});
                }
            }
        }

        // Display result
        cout << "Shortest distances from node " << start << ":\n";
        for (int i = 0; i < vertices; ++i) {
            cout << "Node " << i << " : ";
            if (dist[i] == INT_MAX)
                cout << "Unreachable";
            else
                cout << dist[i];
            cout << endl;
        }
    }
};

// Main function to test Dijkstra’s Algorithm
int main() {
    int V = 6;
    Graph g(V);

    // Add sample edges (u, v, weight)
    g.addEdge(0, 1, 4);
    g.addEdge(0, 2, 2);
    g.addEdge(1, 2, 5);
    g.addEdge(1, 3, 10);
    g.addEdge(2, 4, 3);
    g.addEdge(4, 3, 4);
    g.addEdge(3, 5, 11);

    cout << "=== Dijkstra’s Algorithm Demo ===\n";
    g.dijkstra(0);

    return 0;
}
