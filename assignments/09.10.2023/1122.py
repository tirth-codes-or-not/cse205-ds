class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        ans = []
        temp = []

        for i in arr2:
            for j in arr1:
                if i == j:
                    ans.append(j)
        
        arr1.sort()

        for i in arr1:
            if i not in ans:
                temp.append(i)

        ans = ans+ temp
        return ans

