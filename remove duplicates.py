class Solution:
    def removeDuplicates(self, nums: list(int)) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            elif d[i]<2:
                d[i]+=1
        nums=[]
        for i in d:
            nums+=[i]*d[i]
        return len(nums)
