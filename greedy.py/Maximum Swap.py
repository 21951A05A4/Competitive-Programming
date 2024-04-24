class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=[int (x) for x in str(num)]
        last_index={val:i for i,val in enumerate(nums)}
        for i in range(len(nums)):
            for d in range(9,nums[i],-1):
                if d in last_index and last_index[d]>i:
                    nums[i],nums[last_index[d]]=nums[last_index[d]],nums[i]
                    return int("".join(map(str,nums)))
        return num
