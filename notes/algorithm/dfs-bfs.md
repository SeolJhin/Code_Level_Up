| 구분      | DFS                 | BFS                   |
| ------- | ------------------- | --------------------- |
| 의미      | Depth First Search  | Breadth First Search  |
| 탐색 방식   | 한 방향으로 끝까지 들어감| 현재 위치에서 가까운 곳부터 퍼짐    |
| 핵심 자료구조 | Stack / 재귀          | Queue                 |
| 느낌      | `↓ ↓ ↓` 깊게 파기       | `→ → →` 물결처럼 확산       |
| 최단거리    | 일반적으로 보장 X          | 가중치 없는 그래프에서 보장 O |
| 경로 탐색   | 특정 경로, 모든 경우 탐색에 강함 | 최소 이동 횟수 탐색에 강함       |
| 대표 문제   | 백트래킹, 사이클, 조합 탐색    | 미로 최단거리, 최소 횟수, 전파    |
| 시간복잡도   | O(V + E)            | O(V + E)              |


void dfs(int node) {
    visited[node] = true;

    for (int next : graph[node]) {
        if (!visited[next]) {
            dfs(next);
        }
    }
}

queue<int> q;

q.push(start);
visited[start] = true;

while (!q.empty()) {

    int cur = q.front();
    q.pop();

    for (int next : graph[cur]) {

        if (!visited[next]) {
            visited[next] = true;
            q.push(next);
        }
    }
}