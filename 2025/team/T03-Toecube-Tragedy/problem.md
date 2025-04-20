Your teachers have just banned football during recess at your school because too many students were getting hurt. Therefore, your school has come up with a replacement sport: toecube. In toecube, players use their toes to maneuver a cube to the opponent’s end zone, and has much simpler rules compared to football, given below:

<ul>
    <li>Toecube is played between two teams: Team A and Team B. Possession at the start of the game is determined randomly (nobody said it was fair).</li>
    <li>The field is <code>100</code> Smoots long (one Smoot is approximately 1.7 meters), with endzones on each side. If the cube reaches any team’s endzone, the other team scores <code>1</code> point. That is, each team only needs to advance <code>50</code> Smoots from the middle to score a point.</li>
    <li>As soon as any team scores a point, the cube is reset to the middle and the team that was scored against starts with possession of the cube.</li>
    <li>When play starts, the team in possession gets one down. If they advance <code>10</code> or more Smoots, they earn another down, allowing them to start in possession once more, in the further advanced location. However, if at any point a team advances less than <code>10</code> Smoots, play is reset completely, with the cube returning to the middle and the opposite team taking possession. Note that advancing less than <code>10</code> Smoots to score a point is fine: they get a point and the opposite team takes possession afterward. Advancing past the endzone to score a point is also allowed and works the same way as advancing to the endzone normally.</li>
</ul>

Your job is to scorekeep your school’s final championship game. Unfortunately, both teams were so bad that you fell asleep and the game is already over! Luckily, you have a sheet that represents the number of Smoots per down in chronological order. You are going to need to recover the final score with this information.

## Input
The first line of input will contain one integer `N`: the number of total downs. The second line of input contains one character: either `A` or `B`, which represents the starting team. The third line of input contains `N` space-separated integers, with the `k`-th integer <code>d<sub>k</sub></code> `(1 ≤ k ≤ N)` representing the distance of the `k`-th down.

## Output
Output two integers on the same line, separated by a single space. The first integer should be the number of points team A has and the second integer should be the number of points team B has.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>8</td>
        <td><code>1 ≤ N ≤ 1000</code><br>
			<code>0 ≤ d<sub>k</sub> ≤ 50</code></td>
    </tr>
</table>
