from collections import deque


def bfs(V, adj):
    bfs = []
    visiter = [False] * V
    queue = deque()
    queue.append(0)
    visiter[0] = True
    while queue:
        node = queue.popleft()
        bfs.append(node)
        for i in adj[node]:
            if not visiter[i]:
                queue.append(i)
                visiter[i] = True
    return bfs


# Sample usage
if __name__ == "__main__":
    V = 5
    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[0].append(2)
    adj[0].append(3)
    adj[2].append(4)
    ans = bfs(V, adj)
    print(ans)
