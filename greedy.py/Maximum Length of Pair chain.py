class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        p=pairs.sort(key=lambda x:x[1])
        prev=pairs[0][1]
        i=1
        Count=1
        while i<len(pairs):
            if pairs[i][0]>prev:
                Count+=1
                prev=pairs[i][1]
            i+=1
        return Count
