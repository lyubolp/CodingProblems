class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        
        i = 0
        j = 0
        
        target_indexes = (total_len // 2, total_len // 2) if total_len % 2 != 0 else (total_len // 2 - 1, total_len // 2)
        current_index = 0
        
        result1 = 0
        result2 = 0
        
        results_set = [False, False]
        while i < len(nums1) and j < len(nums2):
            if results_set[0] and results_set[1]:
                break
                
            if current_index == target_indexes[0]:
                result1 = min(nums1[i], nums2[j])
                results_set[0] = True
                
            if current_index == target_indexes[1]:
                result2 = min(nums1[i], nums2[j])
                results_set[1] = True
                
            if nums1[i] <= nums2[j]:
                i += 1
                current_index += 1
            else:
                j += 1
                current_index += 1
        
        while i < len(nums1):
            if current_index == target_indexes[0]:
                result1 = nums1[i]
            if current_index == target_indexes[1]:
                result2 = nums1[i]
                
            i += 1
            current_index += 1
                
        while j < len(nums2):
            if current_index == target_indexes[0]:
                result1 = nums2[j]
            if current_index == target_indexes[1]:
                result2 = nums2[j]
                
            j += 1
            current_index += 1
                
        return (result1 + result2) / 2

