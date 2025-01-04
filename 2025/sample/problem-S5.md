# Laser Maze (2025 S5, 6 pts)

This was one of the hardest problems in the 2023 team contest, and will be approximately as challenging as the hardest few problems in the 2025 contest.

You've gotten stuck in a room with lasers pointing everywhere! You know that these are super-powerful lasers and touching a single one is deadly. All lasers extend from a point on a wall to another wall. You need to determine the number of tiles that are safe to walk on. The locations of the lasers are given by their start and end points. Coordinates are given with (0, 0) at the top left corner, with positive x in the east direction and positive y in the south direction.

For example, if the room's width is 10 and the height is 5, with lasers from (1, 0) to (1, 4), (0, 3) to (9, 3), and (8, 4) to (4, 0), the room would look like this, where X represents the lasers:

```
.X..X.....
.X...X....
.X....X...
XXXXXXXXXX
.X......X.
```

In this example, we can count the number of safe tiles to be 32.

## Input
The first line of input will consist of three integers, n, w, and h. n is the number of lasers, and w and h are the width and height of the room in tiles respectively. It is guaranteed that all diagonal lasers have a slope of ±1.

## Output
Output a single integer: the number of tiles which are safe.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>3</td>
        <td>1 ≤ n ≤ 50<br>4 ≤ w, h ≤ 100</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1 ≤ n ≤ 500<br>4 ≤ w, h, ≤ 10<sup>5</sup></td>
    </tr>
</table>
