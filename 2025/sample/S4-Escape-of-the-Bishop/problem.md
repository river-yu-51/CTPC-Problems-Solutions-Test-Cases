This is a similar problem to “Escape of the Queen” in the 2023 team contest.

You are currently trapped in a chess board with obstacles. As a bishop, you can only move diagonally in a straight line (though you can move as far as you can if your way is unobstructed) in a single move. Given a grid of empty spaces (`.`) and obstacles (`#`), output the minimum number of moves you need to escape. You start in the top left corner and you need to reach the bottom right to escape.

## Input
The first line of input will consist of two integers: the width of the board, `w`, and the height of the board, `h` `(2 ≤ w, h ≤ 30)`. The next `h` lines will contain `w` characters each, with each of these characters being a square on the board. Empty spaces are marked with a `.` and obstacles are marked with a `#`.

## Output
Output a single integer: the minimum number of moves needed to reach the bottom right square. If escaping is impossible, output `-1`.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>5</td>
        <td><code>2 ≤ w, h ≤ 30</code></td>
    </tr>
</table>
