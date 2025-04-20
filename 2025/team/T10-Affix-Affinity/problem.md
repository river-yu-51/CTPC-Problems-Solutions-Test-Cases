You are just about to hand in your English Final, a 5000-word essay on the benefits of watching skibidi toilet, when you suddenly realize that you don’t have a title! You want to come up with the fanciest and most innovative title to impress your teacher. However, your title needs to follow some guidelines:

* The title must be exactly one word.
* There must be a root word within the title. This word must be selected from a choice of <code>R<sub>n</sub></code> allowed root words.
* The word can have at most `P` prefixes, where each prefix comes before the root word (in any order).
* The word can have at most `S` suffixes, where each suffix comes after the root word (in any order).
* You will be given a set of <code>P<sub>n</sub></code> prefixes and <code>S<sub>n</sub></code> suffixes. These are the only ones that you can use. The union of these two sets is known as the set of affixes. To form your title, you must choose at most `P` prefixes from the <code>P<sub>n</sub></code> available ones, and you must choose at most `S` suffixes from the <code>S<sub>n</sub></code> available ones.
* Each root word and affix has a score associated with it. Your total score for your title will be equal to the sum of the score of the root word and the sum of the score of all affixes.

You will be assigned a target score of `K`. This is the exact score your title must add up to (no more, no less). Since you are running out of time on your essay, you want to find the shortest possible title that will follow all required restrictions.
 
Note:
In this question specifically, prefixes and suffixes are defined as full words. That is, any string that is a proper substring of a root word of another affix is not considered an affix. There are only `P` available prefixes and `S` available suffixes.

## Input
The first line contains six space-separated integers: `K`, <code>R<sub>n</sub></code>, <code>P<sub>n</sub></code>, <code>S<sub>n</sub></code>, `P`, and `S`. The next <code>R<sub>n</sub></code> lines will have one string per line, where each line indicates an allowed root word. The next <code>P<sub>n</sub></code> lines after that will have one string per line, where each line indicates an allowed prefix. The next <code>S<sub>n</sub></code> lines after that will have one string per line, where each line indicates an allowed suffix. All <code>R<sub>n</sub> + P<sub>n</sub> + S<sub>n</sub></code> lines following the first will have a space and an integer <code>N<sub>i</sub></code> (where the number on the `i`-th line is <code>N<sub>i</sub></code>) after the given string, indicating the score of the root word or the affix.

## Output
Output the length of the shortest title that will give you a total score of `K` (Note that creating a title with score `K` will be possible for every test case).

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>6</td>
        <td><code>1 ≤ K ≤ 10</code><br>
			<code>1 ≤ R<sub>n</sub>, P<sub>n</sub>, S<sub>n</sub> ≤ 5</code><br>
			<code>0 ≤ P, S ≤ 5</code><br>
			<code>1 ≤ N<sub>i</sub> ≤ 3</code></td>
    </tr>
    <tr>
        <td>6</td>
        <td><code>1 ≤ K, R<sub>n</sub>, P<sub>n</sub>, S<sub>n</sub> ≤ 100</code><br>
		<code>0 ≤ P, S ≤ 100</code><br>
		<code>1 ≤ N<sub>i</sub> ≤ 10</code></td>
    </tr>
</table>
