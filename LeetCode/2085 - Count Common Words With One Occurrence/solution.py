class Solution:
    def counter(self, words: List[str]) -> dict:
        result = {}

        for word in words:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
                
        return result
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = self.counter(words1)
        count2 = self.counter(words2)
        
        result = 0
        for word in count1:
            if count1[word] == 1 and word in count2 and count2[word] == 1:
                result += 1
                
        return result

