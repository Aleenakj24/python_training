#upper limit-lower limit+1
list=[21,1,6,2,1,2,4,7,8,1,2]
k=10
r,l,s,m=0,0,0,0
while r<len(list):
    s+=list[r]#add r to the sum
    while s>k:
        s-=list[l]#if sum is greater than k, we have to increment l and slide the window by removing l
        l+=1
    length=r-l+1#if sum is less or equal to k, calculate the length of subarray and update the max value,inc r
    m=max(m,length)
    r+=1
print(m)

#multiplication
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        r,l,s,m,count=0,0,1,0,0
        while r<len(nums):
            s*=nums[r]
            while s>=k:
                s//=nums[l]
                l+=1
            count+=r-l+1
          
            r=r+1
        return count
        
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        r,l,s,m,count=0,0,1,0,0
        rr=len(nums)-1
        lr=len(nums)-1
        while r<len(nums):
            s+=nums[r]
            while s>=k:
                s-=nums[l]
                l+=1
            count+=r-l+1
          
            r=r+1
        return count
    
#leetcode 3
#1004 max cons ones
#69