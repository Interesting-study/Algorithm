class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        '''내림차순으로 리스트를 정렬한 후에 두칸씩 이동해서 
        min으로 계산하는 방식을 사용하는 게 좋다고 생각했다.
        
        어차피 min으로 구하는 것의 최댓값을 구하는 것이므로,
        내림차순으로 계산하면 큰 것부터 차례대로 min을 구할 수 있을 것이다.
        '''
        total = 0
        for i in range(0, len(nums), 2):
            total += min(nums[i], nums[i+1])
        
        return total
