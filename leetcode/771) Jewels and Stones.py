#https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        jewel_in_cnt = {j: 0 for j in jewels}

        for s in stones:
            if s in jewel_in_cnt:
                jewel_in_cnt[s] += 1

        return sum(jewel_in_cnt.values())
        """
        return sum(s in jewels for s in stones)
