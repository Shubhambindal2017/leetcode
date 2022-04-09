from queue import Queue

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = {vertice: [] for vertice in range(1, self.num_vertices+1)}
        
    def addEdge(self, u, j):
        self.graph[u].append(j)
        
    def print_graph(self):
        for vertice in self.graph:
            print(f'vertice {vertice}: {self.graph[vertice]}')
        
    def shortest_path_using_bfs(self, start, end):
        q = Queue(self.num_vertices)
        q.put(start)
        visited = {vertice:False for vertice in range(1, self.num_vertices+1)}
        visited[start] = True
        distance = {vertice:-1 for vertice in range(1, self.num_vertices+1)}
        distance[start] = 0
        
        while not q.empty():
            node = q.get()
            
            neighbours = self.graph[node]
            for neighbour in neighbours:
                if not visited[neighbour]:
                    q.put(neighbour)
                    distance[neighbour] = distance[node] + 1
                    visited[neighbour] = True
        print(visited)
        print(distance) 
        return distance[end]
                    
        
        
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        b = []
        n = len(board)
        to_right = True
        for i in range(n-1, -1, -1):
            if to_right:
                b += board[i][:]
                to_right = False
            else:
                b += board[i][:][::-1]
                to_right = True
        print(b)
        gf = Graph(len(board)*len(board))
        # u -> start, v -> end
        for u in range(1, (len(board)*len(board))+1):
            for dice in range(1, 7):
                v = u + dice
                if v <  (len(board)*len(board))+1 and b[v-1] != -1:
                    v = b[v-1]      
                if v <  (len(board)*len(board))+1:
                    gf.addEdge(u, v)
        #gf.graph[2] = []
        #gf.graph[14] = []
        #gf.graph[17] = []
        gf.print_graph()
        return gf.shortest_path_using_bfs(1, len(board)*len(board))