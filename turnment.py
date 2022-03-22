HOME_TEAM_WON = 1


# The below method will taka O(n) time as we will need to pass through the competitions list
# and O(k) space as we do not need to store all elements of our teams.
def tournamentWinner(competitions, results):
    current_best_team = ""
    scores = {current_best_team: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]

        home_team, away_team = competition

        winning_team = home_team if result == HOME_TEAM_WON else away_team

        update_scores(winning_team, 3, scores)

        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team

    return current_best_team


def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += 3
