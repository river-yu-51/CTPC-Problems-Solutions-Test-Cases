# Get inputs
[N, K, W, D, L] = [int(x) for x in input().split()]

teams = input().split() # get all teams

results = { team1 : { team2 : 'd' for team2 in teams if team1 != team2} for team1 in teams } # keep track of every team's result against every other team - without additional inputs, we assume all games are draws
points = { team : 0 for team in teams} # store points of each team

# For every decisive game, mark it both as a win for the winner's result against the loser and a loss for the loser's result against the winner
for i in range(K):
    [winner, loser] = [x for x in input().split()]
    results[winner][loser] = 'w'
    results[loser][winner] = 'l'

# For every team, add their points by looking through their wins, losses, and draws
for team in teams:
    for opponent in results[team]:
        if results[team][opponent] == 'w': points[team] += W
        elif results[team][opponent] == 'd': points[team] += D
        else: points[team] += L
    # Multiply all the teams' points by 10^15. This will be used to "buff" the team's score so that the secondary score can be simply added to the team's points value
    # Note that a lower-scoring team can never override a higher-scoring team through secondary scores as the maximum possible secondary score will always be below
    # Maximum points per team: 40 (max team count) * 1000 (max score per win/loss/draw) = 4 * 10^4
    # Maximum secondary score = 40 (max team count) * 1000 (assuming 1000 points against all opponents) * (4 * 10^4) (maximum opponent score) = 1.6 * 10^9
    points[team] *= 10**15

# Calculate secondary score for each team by getting the number of secondary points they score against every team (W/D/L) * opponent's original points (not after being multiplied by 10^15)
for team in teams:
    for opponent in results[team]:
        if results[team][opponent] == 'w': points[team] += W * (points[opponent] // 10**15)
        elif results[team][opponent] == 'd': points[team] += D * (points[opponent] // 10**15)
        else: points[team] += L * (points[opponent] // 10**15)

# Output team with the most points after considering both original score and secondary score
print(max(points, key=points.get))
