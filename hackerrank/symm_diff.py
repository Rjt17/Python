number_eng = int(input())
eng_list = list(map(int, input().strip().split(' ')))
number_french = int(input())
french_list = list(map(int, input().strip().split(' ')))

diff = []

for x in range(0,len(eng_list)):
	if eng_list[x] not in french_list:
		diff.append(eng_list[x])

for x in range(0,len(french_list)):
	if french_list[x] not in eng_list:
		diff.append(french_list[x])

print(len(diff))