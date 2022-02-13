class Solution:
    def is_string_consistent(self, word: str, allowed: set) -> bool:
        return all([c in allowed for c in word])
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set([c for c in allowed])
        
        consistent_strings = [word for word in words if self.is_string_consistent(word, allowed)]
        return len(consistent_strings)

