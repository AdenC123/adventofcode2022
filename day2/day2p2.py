data = []

with open('input.txt') as f:
    for line in f:
        data.append(line.strip().split())

plays = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',

    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

lose = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

win = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}


def play(you, result):
    score = 0
    me = ''
    if result == 'draw':
        me = you
    elif result == 'win':
        me = win[you]
    elif result == 'lose':
        me = lose[you]

    if me == 'rock':
        score += 1
    elif me == 'paper':
        score += 2
    elif me == 'scissors':
        score += 3

    if you == me:
        return score + 3
    elif (you, me) in win.items():
        return score + 6
    elif (you, me) in lose.items():
        return score

    # if you == me:
    #     return score + 3
    # if you == 'rock':
    #     if me == 'paper':
    #         return score + 6
    #     if me == 'scissors':
    #         return score
    # if you == 'paper':
    #     if me == 'scissors':
    #         return score + 6
    #     if me == 'rock':
    #         return score + 0
    # if you == 'scissors':
    #     if me == 'rock':
    #         return score + 6
    #     if me == 'paper':
    #         return score + 0
    # raise Exception

score = 0
for game in data:
    you = plays[game[0]]
    result = plays[game[1]]
    score += play(you, result)

print(score)