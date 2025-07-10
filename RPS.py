import random

def player(prev_play, opponent_history=[]):
    counters = {'R': 'P', 'P': 'S', 'S': 'R'}
    
    if prev_play:
        opponent_history.append(prev_play)

    # Start with random choices to gather data
    if len(opponent_history) < 5:
        return random.choice(['R', 'P', 'S'])

    # Cycle detection: check if opponent repeats every 2 moves
    if len(opponent_history) >= 3 and opponent_history[-1] == opponent_history[-3]:
        predicted = opponent_history[-2]
    else:
        # Frequency-based strategy
        recent_moves = opponent_history[-5:]
        predicted = max(set(recent_moves), key=recent_moves.count)

    return counters[predicted]
