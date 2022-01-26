import math

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        res = []
        
        for i in nums:
            exp = int(math.pow(i,2))
            index = self.getInsertPosition(res,0,len(res)-1,exp)
            res.insert(index,exp)
            
        return res
            
        
    
    def getInsertPosition(self,nums,left,right,target):
        
        if(right>=left):
            mid = (left + right)//2
        
            
            if(nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                return self.getInsertPosition(nums,mid+1,right,target)
            else:
                return self.getInsertPosition(nums,left,mid-1,target)
        else:
            return right + 1