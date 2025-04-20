You are a hungry hippo and your dream is to enter the national apple pie speed eating championship. Unfortunately, you need to qualify first! To do this, you eat a bit of apple pie each day to build up your tolerance level so it is high enough for the qualifier round. (This sounds like a bad idea.)

The championship qualifier takes place on a straight table, lined with pies of various sizes. Your tolerance level must be at least as high as the pie’s size to eat it. When you eat a pie of size `k`, you get <code>k<sup>2</sup></code> points in the qualifier. For example, eating a pie of size `7` will give you <code>7<sup>2</sup></code> = `49` points. Your task is to find the lowest possible tolerance level that will allow you to score at least `Q` points in the qualifier.

Note that the order of the pies doesn't matter, just because you encounter a pie that you cannot eat does not mean you can't continue eating pies further down the line (that you are qualified to eat). This can be seen in the sample case 1 explanation.

## Input
The first line of input will contain two space-separated integers, `N`, the number of pies on the table and `Q`, the minimum number of points you need to qualify. The next line will contain `N` space-separated integers, <code>S<sub>i</sub></code> `(1 ≤ i ≤ N)`, where <code>S<sub>i</sub></code> is the size of the `i`-th pie. 64-bit integers are large enough for all test cases but 32-bit integers are not.

## Output
Output a single integer: the minimum tolerance level you need to qualify. If it is not possible to qualify no matter what your tolerance level is, output `-1`.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>2</td>
        <td><code>1 ≤ N, S<sub>i</sub> ≤ 100</code><br><code>1 ≤ Q ≤ 10<sup>6</sup></code></td>
    </tr>
    <tr>
        <td>3</td>
        <td><code>1 ≤ N, S<sub>i</sub> ≤ 3 * 10<sup>4</sup></code><br><code>1 ≤ Q ≤ 10<sup>13</sup></code></td>
    </tr>
</table>
