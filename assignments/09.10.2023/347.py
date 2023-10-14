class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        common = counter.most_common()

        ans = []

        for key , i in common:
            if k<= 0:
                break

            k = k-1
            ans.append(key)

        return ans
