class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = dict()
        
        for i in range(len(nums)):
            if(nums[i] not in dic):
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        
        nums.sort()
        
        i = 0 
        j = len(nums)-1
        
        
        while(i < j):
        
            if(nums[i] + nums[j] == target):
                a  = dic[nums[i]][0]
                b = dic[nums[j]][0]
                
                if(a == b):
                    b = dic[nums[j]][1]
                
                return [a,b]
        
            elif (nums[i] + nums[j] < target):
                i+=1
            else:
                j-=1

        
        