class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}
        
        for i, num in enumerate(numbers):
            num_map[num] = i+1
            
        for i, num in enumerate(numbers):
            if target - num in num_map and i != num_map[target - num]:
                return [i+1, num_map[target - num]]
            
#64 ms	14.7 MB
