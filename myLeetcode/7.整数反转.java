/*
 * @lc app=leetcode.cn id=7 lang=java
 *
 * [7] 整数反转
 */

// @lc code=start
class Solution {
    public int reverse(int x) {
        int len = 0;
        if(x != 0){
            len = getLen(x);
            for(int i=0;i < len;i++){
                x+=Math.pow(x%10, len-i-1);
            }
        }
        return x;
    }

    public int getLen(int x){
        int len=0;
        if(x < 0){
            x = -x;
            len++;
        }
        if(x < 10){
            return ++len;
        }
        while((x/10) >= 0){
            x=x/10;
            len++;  
        }
        System.out.println("len--->"+len);
        return len;
    }
}
// @lc code=end

