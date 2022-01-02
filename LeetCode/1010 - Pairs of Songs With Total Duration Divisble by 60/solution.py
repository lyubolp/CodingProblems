class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        normalized_times = [item % 60 for item in time]
        
        normalized_times_dict = {}
        
        for i, item in enumerate(normalized_times):
            if item not in normalized_times_dict:
                normalized_times_dict[item] = [i]
            else:
                normalized_times_dict[item] += [i]
        
        result = 0
        
        for i, time in enumerate(normalized_times):
            target_time = 60 - time if time != 0 else 0
            
            if target_time in normalized_times_dict:
                result += len([1 for index in normalized_times_dict[target_time] if i < index])
                
        return result

