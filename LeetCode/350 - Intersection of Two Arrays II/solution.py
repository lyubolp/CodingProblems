from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}

        for item in nums1:
            if item not in count1:
                count1[item] = 1
            else:
                count1[item] += 1

        count2 = {}
        for item in nums2:
            if item not in count2:
                count2[item] = 1
            else:
                count2[item] += 1
            
        result = []

        for key in count1:
            if key in count2:
                for i in range(min(count1[key], count2[key])):
                    result.append(key)
        return result

if __name__ == "__main__":
    s = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    print(s.intersect(nums1, nums2))