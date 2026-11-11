class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        #unique vertices
        #Each vertex max one edge
        #No self connecting vertices
        #trying to find if there is a path from source to destination
        #We could do BFS which is O(VE) time (O(V) here since max 1 edge) and O(V) space
        #We store the edges in a set for O(1) lookup which is a 1 time O(E) operation
        if source == destination:
            return True
        if not edges:
            return False

        #Create undirected graph edgeSet
        edgeSet = {}
        for u, v in edges:
            if u in edgeSet:
                edgeSet[u].append(v)
            else:
                edgeSet[u] = [v]
            if v in edgeSet:
                edgeSet[v].append(u)
            else:
                edgeSet[v] = [u]

        
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()
            connections = edgeSet.get(u, []) #all connections that u has
            #For each edge u is connected to
            for v in connections:
                if v not in visited:
                    if v == destination:
                        return True
                    queue.append(v)
                    visited.add(v)

        #If no queue, that means we went through the full connected subgraph
        return False