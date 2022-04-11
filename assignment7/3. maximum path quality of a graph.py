class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph=defaultdict(list)
        
        for in_,out,cost in edges:
            graph[in_].append((out,cost))
            graph[out].append((in_,cost))
        
        
        self.max_res=0
        @cache
        def dfs(node,time,val,seen):
         
            if node==0:
                self.max_res=max(self.max_res,val)
            
            for neigh,t in graph[node]:
                if time+t>maxTime:
                      continue
                dfs(neigh,  time+t,  val+(neigh not in seen) * values[neigh],   seen | frozenset([neigh]) )
        dfs(0,0,values[0],frozenset([0]))
        return self.max_res
