class Solution:
    global nums
    def removeDuplicates(self, nums: List[int]) -> int:
        
        d={}
        i=0
        while i<(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
                i+=1
            elif d[nums[i]]<2:
                d[nums[i]]+=1
                i+=1
            else:
                nums.pop(i)
                
        return len(nums)
    
        
