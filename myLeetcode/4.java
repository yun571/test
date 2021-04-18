/*
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
ms1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

分析：
1.先合并
2.排序（如何高效）
2.1 正序数组，考虑到何时插入
2.2 直接冒泡排序
2.3 快速排序
2.4 
3.找到中位数
3.1 奇数 返回n/2
3.2 偶数 返回(n/2-1 + n/2)


*/



//暴力法
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] nums;
        int m = nums1.length;
        int n = nums2.length;
        nums = new int[m+n];
        if(m == 0){
            if(n%2 == 0){
                return (nums2[n/2-1] + nums2[n/2]) / 2;
            }else{
                return nums2[n/2];
            }
        }
        if(n == 0){
            if(m%2 == 0){
                return (nums1[m/2-1] + nums1[m/2]) / 2;
            }else{
                return nums1[m/2];
            }
        }
        //都不为空 合并数组
        int count = 0;
        int i = 0, j = 0;
        while (count != (m + n)) {
            if (i == m) {
                while (j != n) {
                    nums[count++] = nums2[j++];
                }
                break;
            }
            if (j == n) {
                while (i != m) {
                    nums[count++] = nums1[i++];
                }
                break;
            }
    
            if (nums1[i] < nums2[j]) {
                nums[count++] = nums1[i++];
            } else {
                nums[count++] = nums2[j++];
            }
        }
        if (count % 2 == 0) {
            return (nums[count / 2 - 1] + nums[count / 2]) / 2.0;
        } else {
            return nums[count / 2];
        }
    }
}