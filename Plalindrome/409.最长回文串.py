#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    # 字典+贪心
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        dic = collections.Counter(s)
        for v in dic.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
# @lc code=end