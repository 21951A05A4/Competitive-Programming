#1.count and say 
class Solution:
    def countAndSay(self, n: int) -> str:
        j=1
        s="1"
        while (j<n):
            count=1
            string=s
            s=""
            for i in range(1,len(string)):
                if string[i]==string[i-1]:
                    count+=1
                else:
                    s+=str(count)+string[i-1]
                    count=1
            s+=str(count)+string[-1]
            j+=1
        return s

#2.Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
        n=len(strs)
        for i in strs:
            x=sorted(i)
            print(x)
            y="".join(x)
            if y not in m:
                m[y]=[i]
            else:
                m[y].append(i)
        return m.values()

#3. Evaluate reverse polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for op in tokens:
            if op=='+':
                a,b=stack.pop(),stack.pop()
                stack.append(b+a)
            elif op=='-':
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif op=='*':
                a,b=stack.pop(),stack.pop()
                stack.append(b*a)
            elif op=='/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(op))
        return stack.pop()

#4.Longest common prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<2:
            return strs[0]
        strs.sort()
        common_prefix=""
        i=0
        while i<len(strs[0]) and i<len(strs[-1]):
            if strs[0][i]==strs[-1][i]:
                common_prefix+=strs[0][i]
                i+=1
            else:
                break
        return common_prefix
