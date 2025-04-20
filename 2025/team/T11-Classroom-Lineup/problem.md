You’re a teacher who is trying to get your Kindergarten class to line up for their year-end picture, and you want them to be in a particular order by name. For example, if your class has `3` kids, `Alice`, `Bob`, and `Charlie`, there are `6` ways for them to line up:

* `Alice Bob Charlie`
* `Alice Charlie Bob`
* `Bob Alice Charlie`
* `Bob Charlie Alice`
* `Charlie Alice Bob`
* `Charlie Bob Alice`

The above permutations are displayed in lexicographical (alphabetical by name) order. We reference the `k`-th permutation as the permutation in the `k`-th position when all permutations are arranged lexicographically. For example, the `2`nd permutation in the previous example would be `Alice Charlie Bob`. You will be given a class list and a positive integer `k`, and you must find the `k`-th permutation of your class list.

Unfortunately, the kids in your class are extremely demanding and want to stand next to their friend (in your class, students have at most one friend, and friendship is commutative–that is, if `x` is the friend of `y`, then `y` is the friend of `x`). Let’s say `Alice` and `Bob` are friends and insist on standing next to each other. Now, there are only `4` ways for them to line up:

* `Alice Bob Charlie`
* `Bob Alice Charlie`
* `Charlie Alice Bob`
* `Charlie Bob Alice`

Now, if you were asked to find the `2`nd permutation, the correct output would be `Bob Alice Charlie`.

## Input
The first line contains three space-separated integers, `N`, the number of students, `Q`, the number of friendships, and `k`, the index of the permutation you need to return. The next line contains `N` space-separated strings (<code>S<sub>i</sub></code>, `1 ≤ i ≤ N`): each representing the name of one student (student names can be in any order). The next `Q` lines contain two strings each: <code>S<sub>m</sub></code> and <code>S<sub>n</sub></code> (`1 ≤ m`, `n ≤ N`, `m != n`), representing the fact that <code>S<sub>m</sub></code> and <code>S<sub>n</sub></code> are friends. Note that 32-bit integers may not be able to hold all values, but 64-bit integers will be able to hold all values.

## Output
Output the `k`-th permutation sorted lexicographically, where every student with friends is beside their friend. Note that such a permutation will always exist.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>4</td>
        <td><code>1 ≤ N ≤ 10</code><br>
			<code>Q = 0</code><br>
			<code>1 ≤ k ≤ 10!</code>*</td>
    </tr>
    <tr>
        <td>4</td>
        <td><code>2 ≤ N ≤ 10</code><br>
			<code>1 ≤ Q ≤ N // 2</code><br>
			<code>1 ≤ k ≤ 10!</code></td>
    </tr>
    <tr>
        <td>4</td>
        <td><code>2 ≤ N ≤ 20</code><br>
			<code>0 ≤ Q ≤ N // 2</code><br>
			<code>1 ≤ k ≤ 20!</code></td>
    </tr>
</table>

*The exclamation mark in all three cases represents the factorial operator, which in math is defined, for any positive integer `M`, to be the multiplication of all positive integers from `1` to `M`. Note that `10!` is approximately <code>3.6 * 10<sup>6</sup></code> and `20!` is approximately <code>2.4 * 10<sup>18</sup></code>.

Additionally, `//` above indicates floor division. (e.g. `4 // 2` = `2`, `5 // 2` = `2`)
