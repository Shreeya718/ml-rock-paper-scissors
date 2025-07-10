import random

def player(prev_play, opponent_history=[], my_history=[], loss_streak=[0]):
    counters = {'R': 'P', 'P': 'S', 'S': 'R'}

    # Track plays
    if prev_play:
        opponent_history.append(prev_play)

    if len(my_history) < len(opponent_history):
        last_opp = opponent_history[-1]
        last_me = my_history[-1] if my_history else ''
        if counters[last_me] == last_opp:
            loss_streak[0] += 1
        else:
            loss_streak[0] = 0

    # Strategy switch if losing streak detected
    if loss_streak[0] >= 5:
        move = random.choice(['R', 'P', 'S'])  # Reset with random
        loss_streak[0] = 0
    elif len(opponent_history) >= 5:
        recent = opponent_history[-5:]
        predicted = max(set(recent), key=recent.count)
        move = counters[predicted]
    elif len(opponent_history) >= 3 and opponent_history[-1] == opponent_history[-3]:
        move = counters[opponent_history[-2]]
    else:
        move = random.choice(['R', 'P', 'S'])

    my_history.append(move)
    return move
