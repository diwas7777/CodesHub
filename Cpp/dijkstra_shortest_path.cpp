#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <utility>

using namespace std;

// Define a constant for infinity (a very large number)
const int INF = numeric_limits<int>::max();

/**
 * @brief Implements Dijkstra's algorithm to find the shortest path from a source node
 * to all other nodes in a weighted graph.
 *
 * @param adj The adjacency list: adj[u] contains pairs {v, weight} representing an edge
 * from u to v with the given weight.
 * @param V The number of vertices in the graph.
 * @param src The source vertex.
 */
void dijkstra(const vector<vector<pair<int, int>>>& adj, int V, int src) {
    // 1. Initialize distance array. dist[i] stores the shortest distance from src to i.
    vector<int> dist(V, INF);

    // 2. Priority Queue (Min Heap) to store pairs: {distance, vertex}.
    // We use greater<> to make it a Min Heap based on the distance (first element of pair).
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    // 3. Set the distance of the source node to 0 and push it to the priority queue.
    dist[src] = 0;
    pq.push({0, src}); // {distance, vertex}

    while (!pq.empty()) {
        // Extract the vertex 'u' with the minimum distance 'd'
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        // Check if the extracted distance is greater than the current known shortest distance.
        // This handles obsolete entries in the priority queue.
        if (d > dist[u]) {
            continue;
        }

        // Iterate over all neighbors 'v' of 'u'
        for (const auto& edge : adj[u]) {
            int v = edge.first;     // Neighbor vertex
            int weight = edge.second; // Edge weight

            // Relaxation Step: If a shorter path to v is found through u
            if (dist[u] + weight < dist[v]) {
                // Update the distance of v
                dist[v] = dist[u] + weight;
                // Push the new minimum distance to the priority queue
                pq.push({dist[v], v});
            }
        }
    }

    // 4. Print the final shortest distances
    cout << "Shortest distances from source node " << src << ":\n";
    for (int i = 0; i < V; ++i) {
        cout << "Node " << i << ": ";
        if (dist[i] == INF) {
            cout << "Unreachable\n";
        } else {
            cout << dist[i] << "\n";
        }
    }
}

int main() {
    // Number of vertices (nodes 0 to 4)
    int V = 5; 
    
    // Adjacency List: vector of pairs {neighbor, weight}
    vector<vector<pair<int, int>>> adj(V);

    // Adding edges: (u, v, weight)
    // Graph structure:
    // 0 --(4)--> 1
    // |         / |
    // (1)    (1)  (2)
    // |       /   |
    // 2 --(5)--> 3 --(1)--> 4
    
    adj[0].push_back({1, 4});
    adj[0].push_back({2, 1});
    adj[1].push_back({3, 2});
    adj[2].push_back({1, 1});
    adj[2].push_back({3, 5});
    adj[3].push_back({4, 1});

    // Run Dijkstra's algorithm starting from node 0
    int source_node = 0;
    dijkstra(adj, V, source_node);

    return 0;
}
