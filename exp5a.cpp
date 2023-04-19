#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int h(int node, int goal) {
    return abs(node - goal);
}

void best_first_search(vector<vector<int>>& graph, int start, int goal) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<bool> visited(graph.size(), false);

    pq.push({h(start, goal), start});
    visited[start] = true;

    while (!pq.empty()) {
        int cur = pq.top().second;
        pq.pop();
        cout << cur << " ";

        if (cur == goal) {
            cout << endl;
            return;
        }

        for (int next : graph[cur]) {
            if (!visited[next]) {
                visited[next] = true;
                pq.push({h(next, goal), next});
            }
        }
    }
}

int main() {
    int n, m;
    cout << "Enter the number of vertices: ";
    cin >> n;
    cout << "Enter the number of edges: ";
    cin >> m;

    vector<vector<int>> graph(n);
    int u, v;
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int start, goal;
    cout << "Enter the starting vertex: ";
    cin >> start;
    cout << "Enter the goal vertex: ";
    cin >> goal;

    best_first_search(graph, start, goal);

    return 0;
}