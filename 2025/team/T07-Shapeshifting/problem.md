You’re a chess shapeshifter trapped in a large dungeon. You need to make use of your powerful abilities to escape by transforming into either a knight, bishop, or rook at the right times. You have some mana to help you in this task but using mana makes you tired so you want to minimize your total mana usage to make sure you have enough energy to escape!

You have the following two abilities:

1. Shapeshift: Allows you to morph into a knight, bishop, or rook. Each of these entities moves in the same way as they do in chess. Shapeshifting costs `1` mana. In each test case, you will start out as either a knight, bishop, or rook, and after shapeshifting into another piece, you will shapeshift back to your starting piece after one move.

2. Move: Allows you to move to any square that is attacked by your current chess piece. Moving costs `1` mana regardless of distance traveled. Note that knights can move through obstacles but bishops and rooks cannot—although bishops and rooks can move any distance in one move while knights can only move to at most eight other squares in one move.

The movement patterns of each chess piece are highlighted below in #s:


<pre>
Knight (N):     Bishop (B):     Rook(R):
Moves in        Moves           Moves 
“L” shape       diagonally      orthogonally
..#.#..         .#...#.         ...#... 
.#...#.         ..#.#..         ...#...
...N...         ...B...         ###R###
.#...#.         ..#.#..         ...#...
..#.#..         .#...#.         ...#...
</pre>

A map of the dungeon will be presented in the following format:

<pre>
<code>.o..o</code>
<code>o.o..</code>
<code>...o.</code>
</pre>

A legend for the map is shown below:

- `.` = Empty space
- `o` = Obstacle


You always start in the top left corner and the exit is the bottom right corner.

## Input
The first line contains a string: either `Knight`, `Bishop`, or `Rook` - the piece that you start as and reset to after shapeshifting. The second line contains two space-separated integers, `m` and `n`, the height and width of the dungeon, respectively. The next `m` lines will have n characters each, laying out the map of the dungeon.

## Output
Output one integer, the minimum amount of mana required to escape. Note that escaping is possible in all test cases.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>10</td>
        <td><code>2 ≤ m, n ≤ 50</code></td>
    </tr>
</table>
