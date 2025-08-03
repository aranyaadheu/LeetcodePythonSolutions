class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index = {}
        for idx, num in enumerate(nums):
            if num in num_to_index and idx - num_to_index[num] <= k:
                return True
            num_to_index[num] = idx
        
        return False