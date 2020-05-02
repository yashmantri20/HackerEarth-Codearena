# Doraemon gave Nobita a gadget that swaps words inside a string in the following manner : 
# If there are W words, word 1 is swapped with word W, word 2 is swapped with word W-1 and so on. 
# The problem is that Nobita himself cannot verify the answer for large strings. Help him write a program to do so.
# INPUT : the first line of the input contains the number of test cases. Each test case consists of a single line containing the string.


T = int(input())

for i in range(T):
    s = list(map(str,input().split()))
    length = len(s)
    k = int(length/2)
    for i in range(k):
        temp = s[i]
        s[i] = s[length - 1 - i]
        s[length - 1 - i] = temp
    print(" ".join(s))