Your English teacher forgot to drink coffee today so they thought it was math class! The teacher gives you two strings containing only lowercase letters with equal length. You need to add them according to the following process:

Each letter is given an index based on their 1-indexed position in the alphabet. Thus, `a = 1`, `b = 2`, … , `z = 26`.
Every character in the first string is added to the character in the second string with the same position. The addition result is essentially shifting the first letter by the placement in the alphabet of the second letter. If the numeric equivalent of the sum is greater than `26`, it wraps back around to the start of the alphabet. After this step is complete, a string of equal length to the first two should be obtained. For example, `a + b → c` (`1 + 2 → 3`) and `b + y → a` (`2 + 25 → 27 → 1`)

For example, the strings `abcxz` and `yaabc` would be added in the following way:

<pre>
1st letter: a + y → 1 + 25 → 26 → z
2nd letter: b + a → 2 + 1 → 3 → c
3rd letter: c + a → 3 + 1 → 4 → d
4th letter: x + b → 24 + 2 → 26 → z
5th letter: z + c → 26 + 3 → 29 → 3 → c
</pre>

Thus, `abcxz` + `yaabc` = `zcdzc`.

## Input
The input consists of two lines: one word of length `L` on each line, consisting of lowercase letters only.

## Output
Output one string: the result of the addition.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>8</td>
        <td><code>1 ≤ L ≤ 250</code></td>
    </tr>
</table>
