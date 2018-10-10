class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #dict（hashtable）比list块
        buff_dict = {}
        for i in range (len(nums)):
            n = nums[i]
            #边做索引边查询
            #buff_dict[n]!=i保证不出现重复结果
            if n in buff_dict and buff_dict[n]!= i:
                return (buff_dict[n], i)
            buff_dict[target-n]=i
