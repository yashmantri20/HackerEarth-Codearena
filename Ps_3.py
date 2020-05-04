'''A movie rating website is hacked to maximize the total rating of a particular show. The hacker decides to flip (negative becomes positive and vice versa) the sign of K ratings. He has to perform exactly K flips on N ratings stored in the database. The flips may or may not be optimal. He can also flip the sign of the same rating more than once.

Write a program to calculate the highest possible total rating of the show.

Input format
First line : Two space-separated integers, N and K
second line : N space-separated integers denoting the ratings

Output format
Print the highest possible rating.

SAMPLE INPUT 
4 2
-1 1 -1 1
SAMPLE OUTPUT 
4
'''

#Partially Accepted 

n,m=map(int,input().split())
l=list(map(int,input().split()))
i=0
while m!=0 :
    if i<n :
        if l[i]<0 :
            m-=1
            l[i]=abs(l[i])

    i+=1
    if i>n :
        break
print(sum(l))