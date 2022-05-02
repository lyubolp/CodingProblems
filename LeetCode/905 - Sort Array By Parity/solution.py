class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        items = sorted(list(count.items()), key=lambda x: (x[0] % 2 != 0, x[0]))
        items = sum([[item[0]] * item[1] for item in items], [])
        
        return items

