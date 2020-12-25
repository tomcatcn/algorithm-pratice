
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 解法  本题可以转化为求斐波那契数列第n项，与前一题有些相似，不同的是，初始是1,1开始。
# 因为青蛙一次可以跳一级或者两级，那么最后一跳分两种情况
# 跳一台阶时候，剩下n-1台阶，跳法有分f(n-1)种
# 跳二台阶时候，剩下n-2台阶，跳法有f(n-2)种
# 所以n台阶的跳法总数f(n) = f(n - 1) + f(n - 2)这和斐波那契数列一样，等于前两个数之和，所以此问题就可以转化为求斐波那契数列的第n项。
# 又因为f(0)=1,f(2) = 1,可以推断出，从1，1初始开始


class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, b+a
        return a % 1000000007
