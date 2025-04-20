You’re a scientist that just discovered a new dimension called the portal dimension! This dimension, as you may have guessed, is filled with portals. To generate a portal, you need to create a closed polygon where each side is a solid beam of light. Unfortunately, your supplies only contain one beam of light, so you’re going to have to do some reflecting in order to create a portal.

Currently, the only location where you can create a portal is known as the cave. The cave is a rectangular grid that contains either mirrors (`/`, `\`) or empty spaces (`#`). Light enters the cave in one of four ways:

* Moving downward from the top edge
* Moving leftward from the right edge
* Moving upward from the bottom edge
* Moving rightward from the left edge

While in the cave, light can move vertically or horizontally. Light does not change direction when moving through an empty space (`#`). If it hits a mirror, it follows the following behavior (intuitively, the light bounces off the way you would expect it to bounce off a perfectly shiny surface in real life):

* Light moving downward will move leftward upon hitting `/` and rightward upon hitting `\`
* Light moving leftward will move downward upon hitting `/` and upward upon hitting `\`
* Light moving upward will move rightward upon hitting `/` and leftward upon hitting `\`
* Light moving rightward will move upward upon hitting `/` and downward upon hitting `\`

Inevitably, one of the following two things will happen, at which point the experiment ends:

* The light beam intersects with itself (light has landed on a previously occupied empty space or mirror) and the polygon enclosed by the beam becomes a portal. In this case, output the total number of spaces enclosed by the beam (don’t count spaces on the beam itself).
* The light beam leaves the cave without creating a portal. In this case, output `-1`.

## Input
The first line contains two space-separated integers: `m`, the height of the cave, and `n`, the width of the cave. The next line contains two space-separated integers: <code>r<sub>e</sub></code> and <code>c<sub>e</sub></code> (<code>1 ≤ r<sub>e</sub> ≤ m</code>, <code>1 ≤ c<sub>e</sub> ≤ n</code>), representing the row and column of the light’s entry point (1-indexed, this point is guaranteed to be on one of the edges but not in a corner). The next `m` lines contain `n` characters each: either `/`, `\`, or `#`, each representing their respective tile above.

## Output
If a portal is formed before the light exits, output the number of spaces (mirrors or empty spaces) enclosed by the light beam. Otherwise, output `-1`.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>6</td>
        <td><code>3 ≤ m, n ≤ 20</code></td>
    </tr>
    <tr>
        <td>6</td>
        <td><code>3 ≤ m, n ≤ 1000</code></td>
    </tr>
</table>
