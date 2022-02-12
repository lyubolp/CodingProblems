class Solution:
    def __init__(self):
        self.first_row = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        self.second_row = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        self.third_row = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
    def is_word_in_keyboard_row(self, word: str) -> bool:
        is_first_row = all([c in self.first_row for c in word.lower()])
        is_second_row = all([c in self.second_row for c in word.lower()])
        is_third_row = all([c in self.third_row for c in word.lower()])
        
        return is_first_row or is_second_row or is_third_row
    def findWords(self, words: List[str]) -> List[str]:
        return [word for word in words if self.is_word_in_keyboard_row(word)]

