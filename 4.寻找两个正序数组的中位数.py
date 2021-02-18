'''
Author: Theo_hui
Date: 2021-02-07 20:43:55
Descripttion: 
'''
#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

import math

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 获取数组的长度
        len1,len2=len(nums1),len(nums2)

        # 获得中间的序号
        mid=(len(nums1)+len(nums2))//2

        # 找到中间的位置
        i,j,mid_v=-1,-1,None
        for k in range(mid):
            if i+1<len1:
                if j+1<len2:
                    if nums1[i+1] <nums2[j+1]:
                        mid_v=nums1[i+1]
                        i+=1
                    else:
                        mid_v=nums2[j+1]
                        j+=1
                else:
                    mid_v=nums1[i+1]
                    i+=1
            else:
                mid_v=nums2[j+1]
                j+=1

        # 接着寻找
        mid_v2=nums1[i+1] if i+1<len1 and (j+1>=len2 or nums1[i+1]<nums2[j+1]) else nums2[j+1]
        # 如果是偶数 则保存这个 寻找下一个
        if (len1+len2)%2==0:
            return (float)((mid_v+mid_v2)/2)
        # 否则 放回一个
        else:
            return (float)(mid_v2)

# @lc code=end

