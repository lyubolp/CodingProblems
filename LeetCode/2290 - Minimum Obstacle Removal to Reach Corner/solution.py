class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        unvisited = []
        visited = set()

        heapq.heappush(unvisited, (0, (0, 0)))
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                heapq.heappush(unvisited, (math.inf, (i, j)))
        
        target_node = (len(grid) - 1, len(grid[0]) - 1)
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(unvisited) > 0:
            current_distance, current_node = heapq.heappop(unvisited)

            if current_node in visited:
                continue

            if current_node == target_node:
                return current_distance

            neighbours = [self.offset_node(current_node, offset) for offset in offsets]
            neighbours = [neighbour for neighbour in neighbours if self.is_node_valid(neighbour, target_node) and neighbour not in visited]

            neighbours = [(current_distance + grid[neighbour[0]][neighbour[1]], neighbour) for neighbour in neighbours]

            for neighbour in neighbours:
                heapq.heappush(unvisited, neighbour)

            visited.add(current_node)

    def is_node_valid(self, node: tuple[int, int], limit: tuple[int, int]) -> bool:
        return 0 <= node[0] <= limit[0] and 0 <= node[1] <= limit[1]

    def offset_node(self, node: tuple[int, int], offset: tuple[int, int]) -> tuple[int, int]:
        return (node[0] + offset[0], node[1] + offset[1])
