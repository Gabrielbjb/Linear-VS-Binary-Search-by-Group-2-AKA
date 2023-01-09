
def binarySearch(A, x, low, high):
    if (low > high):
        return -1
    else:
        mid = int((low+high) / 2)
        if (x == A[mid]):
            return mid
        elif x > A[mid]:
            return binarySearch(A,x,mid+1,high)
        else:
            return binarySearch(A,x,low,mid-1)

def linearSearch(A, n, x):
    i = 0
    while (i < n):
        if (A[i] == x):
            return i
        i+=1
    return -1

A = []
i = 0
while len(A) <= 100000000:
    A.append(i)
    i+=1
import time
 

start = time.time()
binarySearch(A,-1,0,len(A))
end = time.time()
print("The time of execution of Binary Search is :",(end-start) * 10**3, "ms")

start = time.time()
linearSearch(A,len(A),-1)
end = time.time()
print("The time of execution of Linear Search is :",(end-start) * 10**3, "ms")
