data = []

with open('input.txt') as f:
    for line in f:
        data.append(line.strip().split())

plays = {
    'A': 'rock',
    'X': 'rock',
    'B': 'paper',
    'Y': 'paper',
    'C': 'scissors',
    'Z': 'scissors'
}


def play(you, me):
    score = 0
    if me == 'rock':
        score += 1
    elif me == 'paper':
        score += 2
    elif me == 'scissors':
        score += 3

    if you == me:
        return score + 3
    if you == 'rock':
        if me == 'paper':
            return score + 6
        if me == 'scissors':
            return score
    if you == 'paper':
        if me == 'scissors':
            return score + 6
        if me == 'rock':
            return score + 0
    if you == 'scissors':
        if me == 'rock':
            return score + 6
        if me == 'paper':
            return score + 0
    raise Exception


score = 0
for game in data:
    you = plays[game[0]]
    me = plays[game[1]]
    score += play(you, me)

print(score)