class Solution:
    def code(self, s: str, is_sentence: bool=False) -> dict:
        count = {}
        next_num = 1
        sentence = s.split() if is_sentence else s
        for c in sentence:
            if c not in count:
                count[c] = next_num
                next_num += 1
                
        return [count[c] for c in sentence]
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_coded = self.code(pattern)
        s_coded = self.code(s, True)
        return pattern_coded == s_coded

