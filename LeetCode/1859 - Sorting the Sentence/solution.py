class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        words = [(word[-1], word[:-1]) for word in words]
        words.sort(key=lambda x: x[0])
        words = [word[1] for word in words]
        
        return " ".join(words)

