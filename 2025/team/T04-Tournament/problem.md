You’ve been assigned to keep track of the results of a tournament at your school. Being a CS nerd, you decide to build a program to accomplish this task.

In the tournament, every team plays every other team once (round-robin style), receiving `W` points for a win, `D` points for a draw, and `L` points for a loss. Each game either ends in a decisive result (one winner, one loser) or ends in a draw. At the end of the tournament, the highest scoring team wins. If there are multiple teams tied for first place, then a secondary score is calculated for each team by summing the following three numbers:

<ul>
    <li>The sum of the points of all teams they won against multiplied by <code>W</code></li>
    <li>The sum of the points of all teams they drew against multiplied by <code>D</code></li>
    <li>The sum of the points of all teams they lost against multiplied by <code>L</code></li>
</ul>

Once this calculation is done, the team with the highest secondary score who tied for first place in terms of points wins the tournament.

## Input
The first line contains five space-separated integers: `N`, the number of teams, `K`, the number of decisive games, `W`, the number of points per win, `D`, the number of points per draw, and `L`, the number of points per loss. Note that the values of `W`, `D`, and `L` do not follow an order (ex. `W` is not necessarily greater than or equal to `D` or `L`). The second line contains `N` space-separated strings: one for the name of each team. The next `K` lines contain two strings each, all separated by spaces. Each line represents a decisive game between two teams. The first string is the name of the team that won and the second string is the name of the team that lost. All other games between teams are draws.

## Output
Output one string: the name of the team that won the tournament. The winner will always be unique after both rounds of scoring are applied.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>8</td>
        <td><code>1 ≤ N ≤ 40</code><br>
			<code>1 ≤ K ≤ N * (N - 1) / 2</code><br>
			<code>0 ≤ W, D, L ≤ 1000</code></td>
    </tr>
</table>
