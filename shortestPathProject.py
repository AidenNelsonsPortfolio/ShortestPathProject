# Author: Aiden Nelson
# Date Created: 3/14/2023
# Date Last Modified: 3/14/2023

# Description: This program will find the shortest path between nodes in different types of graphs
# using algorthims such as Dijkstra's, Bellman-Ford, and DAG shortest path.


from os import listdir
from os.path import isfile


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
    for v in G.V.values():
        v.d = float('inf')
        v.pi = None
    s.d = 0

def dfs(G, s):
    for v in G.V.values():
        v.color = 'white'
        v.pi = None
    time = 0
    time = dfsVisit(G, s, time)
    if time == -1:
        return -1
    for v in G.V.values():
        if v.color == 'white':
            time = dfsVisit(G, v, time)
            if time == -1:
                return -1
    return 0

def dfsVisit(G, u, time):
    time += 1
    u.d = time
    u.color = 'gray'
    for v in G.Adj[u.key]:
        if v.color == 'white':
            v.pi = u
            time = dfsVisit(G, v, time)
            if time == -1:
                return -1
        if v.color == 'gray':
            print("\nWhile doing dfs, it was found that", u.key, "to", v.key, "is a back edge")
            return -1
    u.color = 'black'
    time += 1
    u.f = time
    return time


def TopologicalSort(G):
    # Graph has already been dfs'd, so we can just sort the vertices by finish time
    # Return a list of vertices in topological order using sorted() function, reversed

    return sorted(G.V.values(), key=lambda x: x.f, reverse=True)


def HasNegativeEdges(G):
    for u in G.V:
        for v in G.Adj[u]:
            if G.Adj[u][v] < 0:
                return True
    return False


def Relax (u, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = u


def ExtractMin(Q):
    # Q is a self made min heap
    # This function will remove the minimum element from the heap and return it
    min = Q[0]
    Q[0] = Q[len(Q) - 1]
    Q.pop()
    i = 0
    while i < len(Q):
        if 2 * i + 1 < len(Q) and Q[i].d > Q[2 * i + 1].d:
            Q[i], Q[2 * i + 1] = Q[2 * i + 1], Q[i]
            i = 2 * i + 1
        elif 2 * i + 2 < len(Q) and Q[i].d > Q[2 * i + 2].d:
            Q[i], Q[2 * i + 2] = Q[2 * i + 2], Q[i]
            i = 2 * i + 2
        else:
            break
    return min

def DecreaseKey(heap, i):
    # This function is used to update a key in the min heap of vertices
    while i > 0 and heap[(i-1)//2].d > heap[i].d:
        heap[(i-1)//2], heap[i] = heap[i], heap[(i-1)//2]
        i = (i-1)//2


def Dijkstra (G, s):
    InitializeSingleSource(G, s)
    Q = list(G.V.values())

    # Swap s with first element
    Q[Q.index(s)], Q[0] = Q[0], Q[Q.index(s)]

    keys = set(v.key for v in Q)

    while Q != []:
        u = ExtractMin(Q)
        keys.remove(u.key)
        for v in G.Adj[u.key]:
            if v.key in keys:
                Relax(u, v, G.Adj[u.key][v])
                DecreaseKey(Q, Q.index(v))   


def BellmanFord(G, s):
    InitializeSingleSource(G, s)
    for _ in range(1, len(G.V)):
        for u in G.V:
            for v in G.Adj[u]:
                Relax(G.V[u], v, G.Adj[u][v])

    for u in G.V:
        for v in G.Adj[u]:
            if v.d > G.V[u].d + G.Adj[u][v]:
                return False
    return True

def DagShortestPath(G, s):
    InitializeSingleSource(G, s)
    orderedVertices = TopologicalSort(G)
    for u in orderedVertices:
        for v in G.Adj[u.key]:
            Relax(u, v, G.Adj[u.key][v])

    return 0

def end():
    print("\nThank you for using the Shortest Path Project!\n")


############################################################################################################
# Main
def main():
    # get all files that are .txt files
    files = [f for f in listdir() if isfile(f) and f.endswith('.txt')]

    # Present file options to user
    print("Welcome to the Shortest Path Project!\n")
    print("Please select the number for the file to run the program on:")

    for i in range(len(files)):
        print(str(i + 1) + ". " + files[i])

    # Get user input, check if valid
    print("\nFile # choice: ", end="")
    userInput = input()
    while not userInput.isdigit() or int(userInput) < 1 or int(userInput) > len(files):
        print("Invalid input. Please enter a number between 1 and " + str(len(files)))
        print("\nFile # choice: ", end="")
        userInput = input()

    file = files[int(userInput) - 1]

    # Make graph from file
    V = {}
    Adj = {}

    print("\nOpening file " + file + "...")
    with open(file, 'r') as f:
        for line in f:
            line = line.split()
            key = line[0].split(":")
            key = key[0]
            if key not in V:
                V[key] = Vertex(key)
            
            Adj[key] = {}

            for i in range(1, len(line), 2):
                if line[i] not in V:
                    V[line[i]] = Vertex(line[i])
                Adj[key][V[line[i]]] = int(line[i + 1])


    print('Making graph object...')

    # Make graph object
    G = Graph(V, Adj) 

    while True:
        # Ask for source node
        print("\nPlease enter the source node: ", end="")
        source = input()        
        while source not in G.V:
            print("Invalid input. Please enter a node that is in the graph.")
            print("\nPlease enter the source node: ", end="")
            source = input()
        
        # Check if graph is DAG
        cycles, negEdges = dfs(G, G.V[source])==-1, HasNegativeEdges(G)
        negCycles = False

        if cycles and not negEdges:
            print("\nThe graph is not a DAG and does not have negative edges.\nWill run Dijkstra's algorithm.\n")
            Dijkstra(G, G.V[source])

        elif cycles and negEdges:
            print("\nThe graph is not a DAG, and has negative edges.\nWill run Bellman-Ford algorithm.\n")
            negCycles = not BellmanFord(G, G.V[source])
            
        else:
            print("\nThe graph is a DAG, will run DAG Shortest Path algorithm.\n")
            DagShortestPath(G, G.V[source])

        if negCycles:
            print("The graph has a negative cycle. Cannot compute shortest path.\n")
            return

        while True:
            # Ask for destination node
            print("Please enter the destination node: ", end="")
            destination = input()
            while destination not in G.V or destination==source:
                print("Invalid input. Please enter a node that is in the graph (not source).")
                print("\nPlease enter the destination node: ", end="")
                destination = input()
            
            # Check if path exists
            badPath = False
            path = []
            u = G.V[destination]
            while u != G.V[source]:
                path.append(u.key)
                u = u.pi
                if u == None:
                    badPath = True
                    break
            path.append(source)
            path.reverse()

            # Check if path exists
            if badPath:
                print("\nNo path exists from " + source + " to " + destination + ".", sep="")
            else:
                print("\nThe shortest path from " + source + " to " + destination + " is:")
                print(" -> ".join(path), " with a distance of ", G.V[destination].d, ".", sep="")

            # Ask if user wants to enter new destination
            print("\nEnter a new destination? (y/n): ", end="")
            userInput = input()
            while userInput != 'y' and userInput != 'n':
                print("Invalid input. Please enter y or n.")
                print("\nEnter a new destination? (y/n): ", end="")
                userInput = input()
            if userInput == 'n':
                break

        # Ask if user wants to enter new source node
        print("\nEnter a new source node? (y/n): ", end="")
        userInput = input()
        while userInput != 'y' and userInput != 'n':
            print("Invalid input. Please enter y or n.")
            print("\nEnter a new source node? (y/n): ", end="")
            userInput = input()
        if userInput == 'n':
            return

main()
end()