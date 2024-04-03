#1. Daily temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        res=[0]*len(temperatures)
        for i in range (len(temperatures)-1,-1,-1):
            while s and temperatures[s[-1]]<=temperatures[i]:
                s.pop()
            res[i]=0 if len(s)==0 else s[-1]-i
            s.append(i)
        return res


#2.Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            c=0
            for j in range(nums2.index(i),len(nums2)):
                if(nums2[j]>i):
                    res.append(nums2[j])
                    c+=1
                    break
            if(c==0):
                res.append(-1)
        return res

#3.Baseball Game
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        s=0
        for i in operations:
            if i=="C":
                s-=stack.pop()
            elif i=="D":
                stack.append(2*stack[-1])
                s+=stack[-1]
            elif i=="+":
                stack.append(stack[-1]+stack[-2])
                s+=stack[-1]
            else:
                stack.append(int(i))
                s+=stack[-1]
        return s

#4.The Number of Weak Characters
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        max_defense=0
        weak_count=0

        for a,d in properties:
            if d<max_defense:
                weak_count+=1
            else:
                max_defense=d
        return weak_count

#5.The number of visible persons in Queue

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack=[]
        res=[1]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            count=0
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                count+=1
            if stack:
                res[i]+=count
            else:
                res[i]=count
            stack.append(i)
	res[-1]=0
        return res

#6.Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1=[]
        l2=[]
        for i in s:
            l1.append(s.index(i))
        for i in t:
            l2.append(t.index(i))
        if l1==l2:
            return True
        return False
