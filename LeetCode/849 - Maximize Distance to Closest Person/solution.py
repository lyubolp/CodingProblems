class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        right_distance = [21000 for i in range(len(seats))]
        
        for i in range(len(seats) - 2, -1, -1):
            if seats[i+1] == 1:
                right_distance[i] = 1
            else:
                if seats[i] == 1:
                    right_distance[i] = 0
                else:
                    right_distance[i] = right_distance[i+1] + 1
        
        left_distance = [21000 for i in range(len(seats))]
        for i in range(1, len(seats)):
            if seats[i - 1] == 1:
                left_distance[i] = 1
            else:
                if seats[i] == 1:
                    left_distance[i] = 0
                else:
                    left_distance[i] = left_distance[i - 1] + 1
                
        
        distances = list(map(lambda left, right: min(left, right), left_distance, right_distance))
        
        return max(distances)

