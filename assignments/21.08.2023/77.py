class Solution:
    def combine(self, n: int, k: int):
        def backtrack(start, current_combination):
            if(len(current_combination) == k):
                result.append(list(current_combination))
                return

            for i in range(start, n+1):
                current_combination.append(i)   
                backtrack(i+1, current_combination)
                current_combination.pop()

        result = []
        backtrack(1, [])
        return result  