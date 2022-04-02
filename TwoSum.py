class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Encontrar em um vetor dois valores dos quais a soma resulta em outro determinado valor
        size = len(nums)
        for i in range(size-1):
            for j in range(i + 1, size):
                if(nums[i]+nums[j] == target): 
                    return([i, j])