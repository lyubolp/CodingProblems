class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dfs = [(0, set(), "")]
        target_node = len(graph) - 1
        paths = set()
        
        while len(dfs) > 0:
            current_node, current_visited, current_path = dfs.pop()
            
            current_visited.add(current_node)
            current_path = current_path + str(current_node) + ","
            
            if current_node == target_node:
                paths.add(current_path)
                continue
                
            for next_node in graph[current_node]:
                if next_node not in current_visited:
                    dfs.append((next_node, current_visited.copy(), current_path))
        
        return [item.split(',')[:-1] for item in paths]

