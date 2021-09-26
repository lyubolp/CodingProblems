class Solution:
    def count(self, word: str) -> dict:
        result = {}
        for c in string.ascii_lowercase:
            result[c] = 0
            
        for c in word:
            result[c] += 1
        
        return result
    
    def count_str(self, count: dict) -> str:
        result = []
        keys = list(count.keys())
        keys.sort()
        for key in keys:
            result.append(str(count[key]))

        return " ".join(result)
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = self.count(word)
            count_str = self.count_str(count)
            if count_str not in groups:
                groups[count_str] = [word]
            else:
                groups[count_str].append(word)

        result = [groups[key] for key in groups]
        
        return result

