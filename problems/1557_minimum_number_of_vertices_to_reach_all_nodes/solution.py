class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # create a set of all nodes
        starting_nodes = set()
        for i in range(n):
            starting_nodes.add(i)
        # iterate over the edges and remove nodes when we can access them
        for edge in edges:
            source = edge[0]
            destination = edge[1]
            if destination in starting_nodes:
                starting_nodes.remove(destination)
        # return list of starter nodes
        return list(starting_nodes)