class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            clockwise = distance[start:destination]
            counterclockwise = distance[destination:] + distance[:start]
        else:
            clockwise = distance[destination:start]
            counterclockwise = distance[start:] + distance[:destination]
            
        return min(sum(clockwise), sum(counterclockwise))

