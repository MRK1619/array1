from re import I
#Next Palmutation

class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        
        if n<2 :
            return nums
        
        inverse = -1
        i = n-2
        
        while i>=0:
            if nums[i]<nums[i+1]:
                inverse = i
                break
            i -=1
        if inverse<0:
            nums.sort()
            i=0
            while nums[i]==0:
                i+=1
            if i!=0:
                nums[0],nums[i]=nums[i],nums[0]
            return nums
        i=n-1
        
        while i>=0:
            if nums[inverse]<nums[i]:
                nums[inverse], nums[i]=nums[i],nums[inverse]
                break
            i-=1
        nums[inverse+1:]=reversed(nums[inverse+1:])
        return nums
ob1=Solution()
print(ob1.nextPermutation([1,4,7,6,3]))
                