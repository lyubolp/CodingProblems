from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [num for num in nums if num % 2 == 0]
        odd = [num for num in nums if num % 2 != 0]

        even_index = 0
        odd_index = 0

        result = []
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[even_index])
                even_index += 1
            else:
                result.append(odd[odd_index])
                odd_index += 1
        
        return result


if __name__ == "__main__":
    s = Solution()
    nums = [4,2,5,7]

    print(s.sortArrayByParityII(nums))