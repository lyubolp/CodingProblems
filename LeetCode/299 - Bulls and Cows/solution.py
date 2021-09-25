class Solution:
    def get_count(self, word: str) -> dict:
        result = {}
        for c in word:
            if c not in result:
                result[c] = 1
            else:
                result[c] += 1
        return result
    
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        secret_count = self.get_count(secret)
        guess_count = self.get_count(guess)
        
        for c in guess_count:
            if c in secret_count:
                cows += min(guess_count[c], secret_count[c])
                
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bulls += 1
                cows -= 1
                
        return "{}A{}B".format(bulls, cows)

