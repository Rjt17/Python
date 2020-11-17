answer = "True"
answers = []
testcases = int(input())
for x in range(0,testcases):
    a_num = int(input())
    a = list(map(int,input().split()))
    b_num = int(input())
    b = list(map(int,input().split()))
    for x in a:
    	if x not in b:
    		answer = "False"
    		break
    answers.append(answer)
    answer = "True"
for x in answers:
	print(x)