class Solution:
    def capitalize_word(self, word: str) -> str:
        if len(word) >= 3:
            return word.capitalize()
        else:
            return word
        
    def capitalizeTitle(self, title: str) -> str:
        words = [self.capitalize_word(word) for word in title.lower().split(' ')]
        
        return " ".join(words)

