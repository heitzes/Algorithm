from collections import defaultdict
def solution(players, callings):
    index = defaultdict(int)
    for ind, player in enumerate(players):
        index[player] = ind
    for player in callings:
        # original index
        org = index[player]
        # ahead player
        ahead = players[org-1]
        players[org-1], players[org] = player, ahead
        index[ahead] = org
        index[player] = org-1
        
    return players