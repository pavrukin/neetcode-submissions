import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # build adjacency list
        adj = [[] for i in range(n)]
        for u, v, w in edges:
            adj[u].append((v,w))

        # initialize initial distances as infinity
        dist=[float("inf")] * n
        # source distance equals =0
        dist[src]=0

        # creat min heap with first value of weight/distance second the vertex
        # initial distance is 0 and the vertex is source (src)
        heap=[(0,src)] 

        while heap:
            # taking the smallest by distance/weight value
            curr_dist, u=heapq.heappop(heap)

            # continue returns to the beginning of while without going further
            if curr_dist>dist[u]:
                continue 

            # we go through all vertexes connected to u one 
            for v,w in adj[u]:
                new_dist=curr_dist+w
                # here define the shortest distance
                if new_dist<dist[v]:
                    dist[v]=new_dist
                    # when the shortest defined we put it to heap
                    heapq.heappush(heap,(new_dist,v))
        
        # result={}
        # for v in range(n):
        #     if dist[v]==float("inf"): result[v]=-1
        #     else: result[v]=dist[v]
        # return result
        
        return {v: (dist[v] if dist[v] != float("inf") else -1) for v in range(n)}

