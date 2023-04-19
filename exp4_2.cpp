#include <iostream>
#include <vector>

using namespace std;

void dfs(vector<vector<int>>& graph, vector<bool>& visited, int cur) {
    visited[cur] = true;
    cout << cur << " ";

    for (int next : graph[cur]) {
        if (!visited[next]) {
            dfs(graph, visited, next);
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

    int start;
    cout << "Enter the starting vertex: ";
    cin >> start;

    vector<bool> visited(n, false);
    dfs(graph, visited, start);
    cout << endl;

    return 0;
}