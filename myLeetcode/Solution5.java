/* 给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：

输入：s = "cbbd"
输出："bb"

示例 3：

输入：s = "a"
输出："a"

示例 4：

输入：s = "ac"
输出："a"

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成 */

class Solution5 {
    public static void main(String[] args) {
        // System.out.println(new Solution5().longestPalindrome("1"));
        // System.out.println(new Solution5().longestPalindrome("121"));
        // System.out.println(new Solution5().longestPalindrome("1211111111"));
        System.out.println(new Solution5().longestPalindrome("111222111"));
    }
    public String longestPalindrome(String A) {
        //记录回文子串起始终止位置
        int begin=0,end=0;
        //记录A的长度
        int n =  A.length();
        /* 
        暴力法
        便利所有字串,如果长度为1,则直接返回A
        */
        if(n==1){
            return A;
        }
        for(int i=0;i < n;i++){
            for(int j = i+1;j < n;j++){
                //每一个字串A[i][j],判断是否为回文串
                String str = A.substring(i,j+1);
                // System.out.println("子串为-->"+str);
                if(isPalindrome(str)){
                    if((j-i) > ( end- begin)){
                        //更新begin和end
                        begin = i;
                        end = j;
                    }
                }
            }
        }
        return A.substring(begin,end+1);
    }   

    //判断是否为回文子串
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