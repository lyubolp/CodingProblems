class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_as_sets = [(set(word), len(word)) for word in words]
        
        result = 0
        for i in range(len(words_as_sets) - 1):
            for j in range(i+1, len(words_as_sets)):
                set_i, len_i = words_as_sets[i]
                set_j, len_j = words_as_sets[j]
                
                if len(set_i & set_j) == 0:
                    result = max(result, len_i * len_j)
        
        return result

