class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        words = [word for word in s.split(' ') if word != '']
        
        
        reversed_words = []
        
        for word in words:
            reversed_words.insert(0, word)
        
        return " ".join(reversed_words)

