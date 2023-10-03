'''

                    NOC:Programming, Data Structures and Algorithms using Python, Chennai Mathematical Institute
                                                    Prof. Madhavan Mukund
                                                    Topic: GCD and Sorting

'''

def gcd(m,n):
    if (m < n):
        (m,n)=(n,m)
    while(m%n != 0):
        (m,n) = (n,m%n)
    return n

def SelectionSort(l):
    for i in range(len(l)):
        minpos=i
        for j in range(i,len(l)):
            if(l[j]<l[minpos]):
                minpos = j
            (l[i],l[minpos]) = (l[minpos],l[i])
            
def InsertionSort(l):
    for sliceEnd in range(len(l)):
        pos = sliceEnd
        while(pos > 0 and l[pos] < l[pos-1]):
            (l[pos],l[pos-1]) = (l[pos-1],l[pos])
            pos = pos-1

l = [4,8,2,5,4]
#SelectionSort(l)
InsertionSort(l)
print(l)
print("Gcd is:",gcd(14,63))