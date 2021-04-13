class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(numbers)):
            another = target-numbers[i]
            if another in numbers and numbers.index(another) != i:
                return sorted([i+1, numbers.index(another) + 1])
            
#2536 ms	14.8 MB
