# A Question of Questions (2025 S3, 5 pts)

You have just spent the last week frantically preparing for an upcoming contest that you are administering: the WRCC. The problem is, there are currently a lot of virtual participants and you can’t handle all their questions! You are going to need to find which questions are worthy of answering to make the best use of your time.

Questions will have the following properties: name, answer start time, answer end time, and value. This information will be represented in the following space-separated format:

Q<sub>i</sub> S<sub>i</sub> E<sub>i</sub> V<sub>i</sub>

Where Q<sub>i</sub>, S<sub>i</sub>, E<sub>i</sub>, and V<sub>i</sub> represent the question name, the start time, the end time, and the value, respectively.

For example, the following question

Why-did-airport-security-suck-so-bad? 5 8 4

Means that the question is Why-did-airport-security-suck-so-bad?, your answer would require your time from the 5th minute to the 8th minute (both inclusive) and the question would yield 4 points of value once answered. Note that you can only answer one question at a time.

## Input
The first line of the input contains 2 integers: the length of the contest, T, and the number of questions, Q. Thus, the contest runs from time 1 to time T (both inclusive) and there will be Q questions that you may answer. The next Q lines will contain four space-separated entities each: Q<sub>i</sub>, S<sub>i</sub>, E<sub>i</sub>, and V<sub>i</sub>, each representing their respective property introduced above.

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
        <td>1 ≤ T, Q ≤ 10<br>1 ≤ S<sub>i</sub>, E<sub>i</sub> ≤ T<br>1 ≤ V<sub>i</sub> ≤ 10<sup>4</sup></td>
    </tr>
    <tr>
        <td>3</td>
        <td>1 ≤ T ≤ 10<sup>4</sup><br>1 ≤ Q ≤ 100<br>1 ≤ S<sub>i</sub>, E<sub>i</sub> ≤ T<br>1 ≤ V<sub>i</sub> ≤ 10<sup>4</sup></td>
    </tr>
</table>
