class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchPosition(nums,0,len(nums)-1,target)
    
    def searchPosition(self,nums,left,right,target):
        
        if(right >= left):
            
            mid = (left + right)//2
            
            if (nums[mid] == target):
                return mid
            
            elif (nums[mid] < target):
                return self.searchPosition(nums,mid+1,right,target)
            else:
                return self.searchPosition(nums,left,mid-1,target)
        else:
            return right + 1
            