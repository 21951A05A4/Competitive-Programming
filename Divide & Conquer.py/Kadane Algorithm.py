def kadane(A):
    max_current=max_global=A[0]
    for i in range(1,len(A)):
        max_current=max(A[i],max_current+A[i])
        max_global=max(max_global,max_current)
    return max_global
A=[-1,2,-3,0,-2]
print(kadane(A))
