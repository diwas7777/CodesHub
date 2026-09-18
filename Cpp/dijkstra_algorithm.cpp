#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Structure to represent an edge in the graph
struct Edge {
    int target;
    int weight;
};

// Function to implement Dijkstra's Algorithm
void dijkstra(int source, const vector<vector<Edge>>& graph, int numVertices) {
    // Min-priority queue to store pairs of (distance, vertex)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    // Vector to store the shortest distance from the source to each vertex
    vector<int> dist(numVertices, INT_MAX);

    // Initialize the source vertex
    dist[source] = 0;
    pq.push({0, source});

    while (!pq.empty()) {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();

        // If a shorter path to u has already been processed, skip it
        if (d > dist[u]) continue;

        // Explore neighbors of u
        for (const auto& edge : graph[u]) {
            int v = edge.target;
            int weight = edge.weight;

            // Relaxation step
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    // Print the computed shortest distances
    cout << "Vertex\tDistance from Source (" << source << ")\n";
    for (int i = 0; i < numVertices; ++i) {
        cout << i << "\t";
        if (dist[i] == INT_MAX) cout << "INF\n";
        else cout << dist[i] << "\n";
    }
}

int main() {
    int numVertices = 5;
    vector<vector<Edge>> graph(numVertices);

    // Hardcoded sample graph layout
    graph[0].push_back({1, 4});
    graph[0].push_back({2, 1});
    graph[1].push_back({3, 1});
    graph[2].push_back({1, 2});
    graph[2].push_back({3, 5});
    graph[3].push_back({4, 3});

    cout << "Running Dijkstra's Algorithm...\n";
    dijkstra(0, graph, numVertices);

    return 0;
}