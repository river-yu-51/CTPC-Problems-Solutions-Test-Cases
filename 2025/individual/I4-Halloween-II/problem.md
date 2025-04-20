It’s Halloween again and you’re out trick-or-treating! You have just filled up your pillowcase with candy, but unfortunately you get hit with a massive gust of wind that scatters your candies all over the place. Since you’re tired and it’s getting late, you decide to just walk home via the closest path of roads from your current location to your house whilst salvaging as many candies as you can on your way. Luckily, you have a drone that can detect and locate the scattered candies. Strangely enough, all your candies are lost at intersections between two roads.

For example, the following is a `4` by `3` grid of roads, with `4` roads running vertically and `3` roads running horizontally. You start in the top left corner (`S`) and exit in the bottom right corner (`E`).

<pre>
S═╦═╦═╗
║ ║ ║ ║
╠═╬═╬═╣
║ ║ ║ ║
╚═╩═╩═E
</pre>

To make sure that you are covering the shortest possible distance, you can only go either downward or to the right. Note that in every test case, you start in the top left and end in the bottom right. Now let’s put some candies (`c`) on the grid:

<pre>
S═╦═╦═╗
║ ║ ║ ║
╠═c═╬═c
║ ║ ║ ║
c═╩═╩═E
</pre>

We can see that the maximum number of candies obtainable whilst only moving downward and to the right is `2`, as trying to get the bottom left candy forces a path that ignores the other two candies. We can see that there are two ways to obtain two candies: moving `right, down, right, right, down` or `down, right, right, right, down`.

## Input
The first line contains three space-separated integers, `C`, the number of candies, and `m` and `n`, the length and height of the grid, respectively. (An `m` by `n` grid has `m` roads going vertically and `n` roads going horizontally.) The next `C` lines contain two integers each: the `x` and `y` coordinates of one unique candy (candies may be placed on the start and end points). Note that these coordinates are zero-indexed so the top left corner is `(0, 0)` and the bottom right corner is `(n - 1, m - 1)`.

## Output
Output two integers, each on their own line. The first integer, `M`, should be equal to the maximum number of obtainable candies. The second integer, `N`, should be equal to the number of paths that can be traversed to collect `M` candies. 64-bit integers are enough to support all inputs and outputs, but 32-bit integers are not.


## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>3</td>
        <td><code>C = 1</code><br><code>2 ≤ m, n ≤ 10</code></td>
    </tr>
    <tr>
        <td>3</td>
        <td><code>2 ≤ C, m, n ≤ 50</code></td>
    </tr>
</table>
