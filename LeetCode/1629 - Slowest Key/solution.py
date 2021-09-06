class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_time = releaseTimes[0]
        max_char = keysPressed[0]
        
        for i in range(1, len(releaseTimes)):
            current_time = releaseTimes[i] - releaseTimes[i - 1]
            if current_time > max_time:
                max_char = keysPressed[i]
                max_time = current_time
            elif current_time == max_time:
                max_char = max(max_char, keysPressed[i])
                max_time = current_time
                
        return max_char

