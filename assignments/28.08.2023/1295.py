class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([i for i in nums if len(str(i)) % 2 == 0])
        


        '''count=int()
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count'''