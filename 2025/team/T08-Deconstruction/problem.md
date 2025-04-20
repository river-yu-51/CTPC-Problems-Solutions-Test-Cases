As an experienced demolisher, you have been assigned with the task of deconstructing a massive building using explosives! The building is represented with an `n` by `m` schematic of tiles that lays out the strength values of each tile. For example, the following schematic represents a `4` by `2` building:

<pre>
05 11 26 77
20 03 42 08
</pre>

Where each number corresponds to a tile. You have a detonator that can reduce the strength of tiles in the following way:

First, choose a tile to detonate. This tile will lose `2` strength due to the impact.
Every other tile in the building loses `1` strength due to the explosion.

For example, detonating the `05` in the above building yields the following updated schematic:

<pre>
03 10 25 76
19 02 41 07
</pre>

Whenever a tile reaches zero or lower, it is considered demolished. The entire building is demolished once every tile in the building is demolished. Constantly detonating tiles will eventually result in the demolition of the building, but you want to demolish everything in as few detonations as possible. Note that there are no restrictions on which tile you can detonate.

## Input
The first line contains two space-separated integers, `n` and `m`, the width and height of the initial schematic, respectively. The next `m` lines contain `n` integers, <code>i<sub>k</sub></code> `(1 ≤ k ≤ n)`, the strength of the `k`-th tile in that row.

## Output
Output one integer: the minimum number of detonations required to demolish the building.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>3</td>
        <td><code>1 ≤ m, n, ≤ 25</code><br>
			<code>1 ≤ i<sub>k</sub> ≤ 100</code></td>
    </tr>
    <tr>
        <td>3</td>
        <td><code>1 ≤ m, n, ≤ 25</code><br>
			<code>1 ≤ i<sub>k</sub> ≤ 1000</code></td>
    </tr>
    <tr>
        <td>4</td>
        <td><code>1 ≤ m, n, ≤ 25</code><br>
			<code>1 ≤ i<sub>k</sub> ≤ 10<sup>9</sup></code></td>
    </tr>
</table>
