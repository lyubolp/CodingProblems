class Solution:
    def count(self, nums: List[int]) -> Dict[int, int]:
        result = {}
        
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        
        return result
    
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = 0
        
        nums1_dict = self.count(nums1)
        nums2_dict = self.count(nums2)
        
        nums34 = [x + y for y in nums4 for x in nums3]
        nums34_dict = self.count(nums34)
                
        for x in nums1_dict:
            for y in nums2_dict:
                target = -x - y
                if target in nums34_dict:
                    result += nums1_dict[x] * nums2_dict[y] * nums34_dict[target]
        
        return result

