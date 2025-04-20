Nikki, still traumatized by a brutal math test from her time at Reston High, can’t believe she’s now the teacher of a high school math course. With final marks due soon, Nikki has been procrastinating and now doesn’t have enough time to calculate them manually. Haunted by her past math struggles, she decides to create a program to handle the task instead, determined to avoid the chaos she once experienced as a student.

The grade of a student is calculated in the following way:

- 70% from test average
- 30% from final exam

For example, a student with a `60` test average and `80` on the final exam would have a final mark of `60 * 0.7 + 80 * 0.3` = `42 + 24` = `66`.

## Input
The first line contains one integer, `N`, the number of tests (excluding the exam). The next line contains `N` space-separated integers <code>T<sub>i</sub></code> `(1 ≤ i ≤ N)`, each one being the mark of one test. The final line contains one integer, `E`, the mark of the exam.

## Output
Output the final grade from the tests and the exam, rounded to the nearest integer. This number should be between `0` and `100`, inclusive.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>8</td>
        <td><code>1 ≤ N ≤ 100</code><br>
			<code>0 ≤ T<sub>i</sub>, E ≤ 100</code></td>
    </tr>
</table>
