class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        min_pair = []
        min_sum = 0
        '''내림차순으로 리스트를 정렬한 후에 두개씩 넣어서
        min으로 계산하는 방식을 사용하는 게 좋다고 생각했다.
        
        어차피 min으로 구하는 것의 최댓값을 구하는 것이므로,
        내림차순으로 계산하면 큰 것부터 차례대로 min을 구할 수 있을 것이다.
        '''
        for i in nums:
            min_pair.append(i)
            if len(min_pair) == 2:
                min_sum += min(min_pair)
                min_pair = []
                
        return min_sum
