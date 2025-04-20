You have just spent the last week frantically preparing for an upcoming contest that you are administering: the WRCC. The problem is, there are currently a lot of virtual participants and you can’t handle all their questions! You are going to need to find which questions are worthy of answering to make the best use of your time.

Questions will have the following properties: name, answer start time, answer end time, and value. This information will be represented in the following space-separated format:

<code>N<sub>i</sub> S<sub>i</sub> E<sub>i</sub> V<sub>i</sub></code>

Where <code>N<sub>i</sub></code>, <code>S<sub>i</sub></code>, <code>E<sub>i</sub></code>, and <code>V<sub>i</sub></code> represent the question name, the start time, the end time, and the value, respectively.

For example, the following question

`Why-did-airport-security-suck-so-bad? 5 8 4`

Means that the question is `Why-did-airport-security-suck-so-bad?`, your answer would require your time from the `5`th minute to the `8`th minute (both inclusive) and the question would yield `4` points of value once answered. Note that you can only answer one question at a time.

## Input
The first line of the input contains 2 integers: the length of the contest, `T`, and the number of questions, `Q`. Thus, the contest runs from time `1` to time `T` (both inclusive) and there will be `Q` questions that you may answer. The next `Q` lines will contain four space-separated entities each: <code>N<sub>i</sub></code>, <code>S<sub>i</sub></code>, <code>E<sub>i</sub></code>, and <code>V<sub>i</sub></code>, each representing their respective property introduced above.

## Output
Output the maximum possible total value of all questions answered during the contest.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>2</td>
        <td><code>1 ≤ T, Q ≤ 10</code><br><code>1 ≤ S<sub>i</sub> ≤ E<sub>i</sub> ≤ T</code><br><code>1 ≤ V<sub>i</sub> ≤ 10<sup>4</sup></code></td>
    </tr>
    <tr>
        <td>3</td>
        <td><code>1 ≤ T ≤ 10<sup>4</sup></code><br><code>1 ≤ Q ≤ 100</code><br><code>1 ≤ S<sub>i</sub> ≤ E<sub>i</sub> ≤ T</code><br><code>1 ≤ V<sub>i</sub> ≤ 10<sup>4</sup></code></td>
    </tr>
</table>
