/*
 * @lc app=leetcode.cn id=9 lang=java
 *
 * [9] 回文数
 */

// @lc code=start
class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().isPalindrome(121));
        System.out.println(new Solution().isPalindrome(-121));
        System.out.println(new Solution().isPalindrome(2121));
        System.out.println(new Solution().isPalindrome(1112111));
    }
    public boolean isPalindrome(int x) {
        String xStr = String.valueOf(x);
        return isPalindrome(xStr);
    }

    public boolean isPalindrome (String str) {
        int n = str.length();
        int k = n / 2;
        for (int i = 0; i < k; ++i)
        {
            if (str.charAt(i) != str.charAt(n-1-i))
                return false;
        }
        return true;
    }
}
// @lc code=end

