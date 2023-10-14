class Solution:
    def frequencySort(self, s: str) -> str:

        temp = {}
        count = 0

        for i in s:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
            
            count = max(count , temp[i])

        ans = []
        while count > 0:
            for i, freq in temp.items():
                if freq == count:
                    ans.append(i * freq)
                    temp[i] = 0
            count -= 1
        
        return "".join(ans)