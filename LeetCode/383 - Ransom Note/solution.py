class Solution:
    def counting_letters(self, s: str) -> dict:
        result = {}
        for c in s:
            if c in result:
                result[c] += 1
            else:
                result[c] = 1
        return result
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = self.counting_letters(magazine)
        ransom_letters = self.counting_letters(ransomNote)
        
        for key in ransom_letters:
            if key not in magazine_letters or ransom_letters[key] > magazine_letters[key]:
                return False
        return True

