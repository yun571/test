/*
 * @lc app=leetcode.cn id=6 lang=java
 *
 * [6] Z 字形变换
 */

// @lc code=start
class Solution {
    public String convert(String s, int numRows) {
        //只有一行 直接返回
        if(numRows < 2) return s;
        //定义长度为numRows的List,并使用StringBuilder用于字符拼接
        List<StringBuilder> rows = new ArrayList<StringBuilder>();
        for(int i = 0; i < numRows; i++) rows.add(new StringBuilder());
        //初始化i和flag
        int i = 0, flag = -1;
        /**
         * 核心--->flag 更新下标
         * 相当于建立了numRows个StringBuilder,在同一行就append
         * 然后更新i下标 通过 
         * if(i == 0 || i == numRows -1) flag = - flag;
         * 控制 (妙呀妙呀)
         * */ 
        for(char c : s.toCharArray()) {
            rows.get(i).append(c);
            if(i == 0 || i == numRows -1) flag = - flag;
            i += flag;
        }
        StringBuilder res = new StringBuilder();
        for(StringBuilder row : rows) res.append(row);
        return res.toString();
    }
}
// @lc code=end

