class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(sorted(words))
        return [item[0] for item in counter.most_common(k)]

