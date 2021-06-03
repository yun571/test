/*
 * @lc app=leetcode.cn id=7 lang=java
 *
 * [7] 整数反转
 */

// @lc code=start
class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().reverse(1534236469));
        System.out.println(new Solution().reverse(123));
        System.out.println(new Solution().reverse(0));
        System.out.println(new Solution().reverse(654));
        long p = 964632435;
        p = p*10 + 1;
        System.out.println("===========\n"+p+"\n===========");
    }
    public int reverse(int x) {
        if(x==0){
            return 0; }
else{ 
        long a = 0;
                while (x != 0){
                            a = a * 10 + x % 10;
                            x= x /10;
       }
        if (a<=Math.pow(2,31) && a>=Math.pow(-2,31)){
            return (int)a;
        }else{
        return 0;}}
    }
}
// @lc code=end

