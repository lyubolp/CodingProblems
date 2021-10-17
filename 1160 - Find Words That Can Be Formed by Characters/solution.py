class Solution:
    def count(self, word: str) -> dict:
        count = {}
        
        for c in word:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        return count
    
    def is_string_good(self, word: List[str], count_chars: dict) -> bool:
        count_word = self.count(word)
        
        for c in count_word:
            if c not in count_chars or count_chars[c] < count_word[c]:
                return False
            
        return True
        
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_chars = self.count(chars)
        
        good_words = [len(word) for word in words if self.is_string_good(word, count_chars)]
        
        return sum(good_words)

