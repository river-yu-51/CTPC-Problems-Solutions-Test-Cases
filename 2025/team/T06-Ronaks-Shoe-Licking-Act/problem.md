You are the assistant of Ronak Patel, a professional actor who specializes in acts where he licks a bunch of different shoes. It’s just minutes before his next performance and you need to help him acquire all the shoes he needs for the act!

Each shoe is represented by an uppercase or lowercase letter. His full performance can thus be represented by a string, for example the string `Aqg` means he first licks shoe `A`, then licks shoe `q`, then licks shoe `g`, and then he is done.

Ronak can only lick shoes in certain ways, known as sub-acts (represented as strings, again where each character represents a shoe). He is going to need to combine many sub-acts to create his full performance. For example, if he needs to perform the act `qWerty` and can perform the sub-acts `qWe`, `r`, `ty`, `Wty`, `qwer`, and `rty`, he can complete the performance with the following combinations of sub-acts:

- `qWe` then `r` then `ty`
- `qWe` then `rty`

However, this is under the assumption that he has all the necessary shoes (which is not the case)! A sub-act may also contain underscores. Underscores represent a missing shoe. For example, if Ronak still needs to perform the act `qWerty` and can perform the sub-acts `qWe`, `r`, `ty`, `Wty`, `q_er`, and `rty`, he can complete the performance with the following combinations of sub-acts:

<ul>
    <li><code>0</code> missing shoes: <code>qWe</code> <code>r</code> <code>ty</code></li>
    <li><code>0</code> missing shoes: <code>qWe</code> <code>rty</code></li>
    <li><code>1</code> missing shoe: <code>q_er</code> <code>ty</code> (where <code>_</code> is replaced by <code>W</code>)</li>
</ul>

Your goal will be to try and minimize the number of missing shoes so you don’t need to buy as many of them (they’re extremely expensive). If multiple underscores can be replaced by the same shoe, you still need to buy multiple shoes as Ronak is very picky and will only lick each shoe once. However, each sub-act can be used as many times as you want!

## Input
The first line contains one string of length `L` containing uppercase and lowercase characters: the string representing the performance. The next line contains one integer `S`, the number of sub-acts Ronak can perform. The next `S` lines contain one string each containing uppercase letters, lowercase letters, and underscores. Note that all sub-acts have a length less than or equal to `L`.

## Output
Output one integer: the minimum number of missing shoes for the entire performance. Note that the performance in every test case will be possible with the given sub-acts.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>5</td>
        <td><code>1 ≤ L, S ≤ 10</code></td>
    </tr>
    <tr>
        <td>5</td>
        <td><code>1 ≤ L ≤ 1000</code><br>
			<code>1 ≤ S ≤ 100</code></td>
    </tr>
</table>
