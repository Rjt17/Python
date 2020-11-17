n,m,k = 5,2,2
A = [5,3,2,4,1]
S = [3,4]
l,r,x = 1,4,1

        additives = 0
        
        for temp in range(l-1,r):
            if A[temp] in S:
                continue
            else:
                A[temp] += x

        for temp1 in A:
            additives += temp1
        
        print(additives)
        additives = 0