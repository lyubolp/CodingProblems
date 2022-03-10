class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        result = sorted([[num, count[num]] for num in count], key=lambda x: (x[1], -x[0]))

        return sum([[num[0]] * num[1] for num in result], [])

