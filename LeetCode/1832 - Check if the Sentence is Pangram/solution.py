class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = [0] * 26
          
        for c in sentence:
            index = ord(c) - ord('a')
            count[index] += 1
          
    return all(c != 0 for c in count)

