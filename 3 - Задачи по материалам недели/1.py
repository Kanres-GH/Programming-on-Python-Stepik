n = int(input())
total = dict()
wins_score = dict()
wins = dict()
loses = dict()
ties = dict()
temp = dict()
score = dict()
total_list = []
for i in range(n):
    s = input().split(';')
    total_list.append(s)
    wins[s[0]] = wins[s[2]] = 0
    loses[s[0]] = loses[s[2]] = 0
    ties[s[0]] = ties[s[2]] = 0
    total[s[0]] = total[s[2]] = 0
    score[s[0]] = score[s[2]] = 0
# Total
for i in total_list:
    total[i[0]] += 1
    total[i[2]] += 1

# Wins, loses, ties, score
for i in total_list:
    wins_score[i[0]] = int(i[1])
    wins_score[i[2]] = int(i[3])
    if wins_score[i[0]] > wins_score[i[2]]:
        wins[i[0]] += 1
        loses[i[2]] += 1
        score[i[0]] += 3
    elif wins_score[i[0]] < wins_score[i[2]]:
        wins[i[2]] += 1
        loses[i[0]] += 1
        score[i[2]] += 3
    elif wins_score[i[0]] == wins_score[i[2]]:
        ties[i[0]] += 1
        ties[i[2]] += 1
        score[i[0]] += 1
        score[i[2]] += 1
    wins_score.clear()
for i in total:
    print(f'{i}:{total[i]} {wins[i]} {ties[i]} {loses[i]} {score[i]}')