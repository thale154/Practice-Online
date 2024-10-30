class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Calculate LIS ending at each index
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        # Step 2: Calculate LDS starting at each index
        lds = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        # Step 3: Find the maximum length of bitonic subsequence
        max_len = 0
        for i in range(1, n-1):
            if lis[i] > 1 and lds[i] > 1:  # valid peak
                max_len = max(max_len, lis[i] + lds[i] - 1)
        
        # Minimum removals to make the array a mountain array
        return n - max_len
