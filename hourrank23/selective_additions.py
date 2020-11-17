n,m,k = 5,2,2
A = [5,3,2,4,1]
S = [3,4]
l,r,x = 1,4,1
l1,r1,x1 = 1,5,3
summation = 0

#if i remove the set S from A then the list index will 
#get fucked cause i removed elements from it so i have to modify 
#variables l and x for the next thing.

#no this won't work cause wht if l doesn't start from index 0
#and if i remove set s and any element comes before l will get
#removed and it will fuck with the l index so it order to do
#that i will have to calculate the indexes of removed items and
#compare it to l and r which is too much work

#so instead i will not remove the set s but put the first 
#exception so that it matches with the set and continues if
#element exists in the set. this way i won't have to even
#write the extra code for the changes which will happen after
#increasing the value x to set A.

for temp1 in range(l-1,r):
	if A[temp1] in S:
		continue
	else:
		A[temp1] += x

for temp1 in A:
	summation += temp1
print(summation)

#this works i just have to beautify this code and i'm done.