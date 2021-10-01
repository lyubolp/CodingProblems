from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False

        partition_sum = sum(nums) // k
        visited = [False for i in range(len(nums))]

        return self.dfs(nums, visited, 0, k, partition_sum, 0)
            

    def dfs(self, nums: List[int], visited: List[bool], start_index: int, k: int, target_sum: int, current_sum: int) -> bool:
        if k == 1:
            return True
        if current_sum > target_sum:
            return False
        elif current_sum == target_sum:
            return self.dfs(nums, visited, 0, k - 1, target_sum, 0)

        for i in range(start_index, len(nums)):
            if not visited[i]:
                visited[i] = True
                if self.dfs(nums, visited, i + 1, k, target_sum, current_sum + nums[i]):
                    return True
                visited[i] = False

        return False

if __name__ == "__main__":
    s = Solution()

    nums = [4,3,2,3,5,2,1]
    k = 4
    print(s.canPartitionKSubsets(nums, k))