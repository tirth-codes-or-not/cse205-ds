class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l1 = []
        for i in accounts:
            sum = 0
            for j in i:
                sum += j
                l1.append(sum)
                l1.sort()
        return l1[-1] 