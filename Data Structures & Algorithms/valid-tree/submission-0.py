class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1 create an empty neighbor list for every node
        # add both directions for every unidirected edges
        #start the dfs at node 0
        # make empty neighbor list for each node [[],[],[]]
        graph = [[] for i in range(n)]
        #set maube to keep track of nodes already visited
        # visited = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node, parent):
            visited.add(node)
        #read the endpoint of the unidirected edges
        #add b as a neighbor of a and vice versa
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
                
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n



        #dfs explores the graph from node
        #mark the current node as visited before checking its neighbors

        #look at every node connected to the current node

        # we skip node because going back to the parent is not a cycle

        if not dfs(neighbor, node):
            return False
        # recursively explore the unvisited neighbors
        #reutrn false if deeper search finds a cycle


        #