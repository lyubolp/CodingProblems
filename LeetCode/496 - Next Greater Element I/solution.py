
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for num in nums1:
            j = nums2.index(num)

            bigger = -1
            for el in nums2[j:]:
                if el > num:
                    bigger = el
                    break

            result.append(bigger)

        return result

