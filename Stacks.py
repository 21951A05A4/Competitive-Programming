#1.minstack
class MinStack:

    def __init__(self):
        self.mainStack=[]
        self.minStack=[]    

    def push(self, val: int) -> None:
        self.mainStack.append(val) 

        if not self.minStack or val<=self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        popped=self.mainStack.pop()
        
        if popped == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


#2.implement Queue using stacks
class MyQueue:

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
       return len(self.stack)==0 

#linked list:
class Qnode(object):
    def __init__(self,val):
        self.val=val
        self.next=None
class MyQueue:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,x:int)->None:
        node=Qnode(x)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def pop(self)->int:
        temp=self.head
        self.head=temp.next
        return temp.val
    def peek(self)->int:
        return self.head.val
    def empty(self)->bool:
        return self.head=None


#3.remove Duplicate letters
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        seen=set()
        last_occ={c:i for i,c in enumerate(s)}
        print(last_occ)
        for i,c in enumerate(s):
            if c not in seen:
                while stack and c<stack[-1] and i<last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return "".join(stack)

#4.Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        r=""
        num=0
        stack=[]
        for c in s:
            if c .isdigit():
                num=num*10+int(c)
            elif c=="[":
                stack.append(r)
                stack.append(num)
                r=""
                num=0
            elif c=="]":
                pnum=stack.pop()
                pstr=stack.pop()
                r=pstr+pnum*r
            else:
                r+=c
        return r

#5. validate stack sequences
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        j=0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return stack==[]
        if pushed==popped:
            return True
        else:
            return False

#6. Daily temperatures
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


#7.Next Greater Element I
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

#8.Baseball Game
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

#9.The Number of Weak Characters
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

#10.The number of visible persons in Queue

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

#11.Isomorphic Strings
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
