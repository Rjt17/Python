number_of_ranks = 7
ranked = [100,100,50,40,40,20,10]
games = 4
score = [5,25,50,120]

ranked = list(dict.fromkeys(ranked)) #duplicate entries removed from list named ranked

def descending_sort(ranked):
	for x in range(0,len(ranked)):
		for y in range(0,len(ranked)):
			if ranked[x]>ranked[y]:
				ranked[x],ranked[y] = ranked[y],ranked[x]


for x in score:						#iterate through list named score
	current_score = x

	if current_score in ranked:		#ranking if score is already in ranked scores
		print("rank is : " + str(ranked.index(current_score) + 1))
	else:							#ranking if scores is not in ranked scores already
		ranked.append(current_score)
		descending_sort(ranked)
		print("rank is : " + str(ranked.index(current_score) + 1))