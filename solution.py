class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        
        for i in range(len(equations)):
            start, end = equations[i]
            value = values[i]
            
            if start not in graph:
                graph[start] = {}
            
            graph[start][end] = value
            
            if end not in graph:
                graph[end] = {}
            
            graph[end][start] = 1 / value
            
            graph[start][start] = 1
            graph[end][end] = 1
        
        result = []
        for query in queries:
            
            start = query[0]
            end = query[1]

            if start not in graph or end not in graph:
                result.append(-1)
            elif start in graph and end in graph[start]:
                result.append(graph[start][end])
            else:
                stack = [(start, 1)]
                visited = set()
                added = False
                while len(stack) > 0:

                    node, score = stack.pop()

                    if node == end:
                        result.append(score)
                        stack = []
                        added = True
                    elif node not in visited:
                        visited.add(node)
                        for child in graph[node]:
                            stack.append((child, score * graph[node][child]))
                if not added:
                    result.append(-1)
                        
        return result

