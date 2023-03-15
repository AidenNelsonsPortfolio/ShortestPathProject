# Author: Aiden Nelson
# Date Created: 3/14/2023
# Date Last Modified: 3/14/2023

# Description: This program will find the shortest path between nodes in different types of graphs
# using algorthims such as Dijkstra's, Bellman-Ford, and DAG shortest path.

class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = 'white'
        self.pi = None
        self.d = float('inf')
        self.f = float('inf')

class Graph:
    def __init__(self, V, Adj):
        self.V = V
        self.Adj = Adj

def InitializeSingleSource(G, s):
    for v in G.V:
        v.d = float('inf')
        v.pi = None
    s.d = 0

def dfs(G):
    for v in G.V:
        v.color = 'white'
        v.pi = None
    time = 0
    for v in G.V:
        if v.color == 'white':
            time = dfsVisit(G, v, time)

def dfsVisit(G, u, time):
    time += 1
    u.d = time
    u.color = 'gray'
    for v in G.Adj[u]:
        if v.color == 'white':
            v.pi = u
            dfsVisit(G, v)
    u.color = 'black'
    time += 1
    u.f = time
    return time


def TopologicalSort(G):
    dfs(G)
    G.V.sort(key=lambda x: x.f, reverse=True)

def Relax (u, v, w):
    if v.d > u.d + w(u, v):
        v.d = u.d + w(u, v)
        v.pi = u

def Dijkstra (G, w, s):
    InitializeSingleSource(G, s)
    S = []
    Q = G.V
    while Q != []:
        u = ExtractMin(Q)
        S.append(u)
        for v in G.Adj[u]:
            Relax(u, v, w)

def BellmanFord(G, w, s):
    InitializeSingleSource(G, s)
    for i in range(1, len(G.V)):
        for u in G.V:
            for v in G.Adj[u]:
                Relax(u, v, w)
    for u in G.V:
        for v in G.Adj[u]:
            if v.d > u.d + w(u, v):
                return False
    return True

def DagShortestPath(G, w, s):
    TopologicalSort(G)
    InitializeSingleSource(G, s)
    for u in G.V:
        for v in G.Adj[u]:
            Relax(u, v, w)


