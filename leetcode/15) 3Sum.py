    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)-2):
            #중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            #간격을 좁히며 sum 값을 계산
            left, right = i+1, len(nums) -1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 :
                    left += 1
                elif sum > 0 :
                    right -= 1
                else:
                    #sum = 0일때
                    result.append((nums[i], nums[left], nums[right]))
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return result
