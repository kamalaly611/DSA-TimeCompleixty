player_score={}

with open("scores.csv", "r") as f:
    for line in f:
        tokens=line.split(',')
        player=tokens[0]
        score=int(tokens[1])
        
        if player in player_score:
            player_score[player].append(score)
        else:
            player_score[player]=[score]


for player, score_list in player_score.items():
    max_score=min(score_list)
    min_score=min(score_list)
    avg_score=sum(score_list)/len(score_list)
    print(f"{player}==>Min:{min_score}, Max:{max_score}, Avg{avg_score}")