Last year you worked as a security guard at the airport. However, since the requirements for what items can pass security didn’t make sense, you decided to quit and instead use your knowledge of the airport’s terrible regulations to smuggle items onto planes. In fact, you have become so good at this that other people ask you to smuggle their items as well. 

People that want you to smuggle items will give you an order. Each order is given as a pair `(w, x)` where `w` is the item name as a string and `x` is the item quantity as an integer. However, if you take too many orders, the airport security guards will get suspicious of you! Thus, you need to follow a strict guideline on the maximum amount of each item you can smuggle. You will be given a list of orders, from which you need to decide which orders to take. As another safety measure, you decide to take at most one consecutive block of orders: once you decide to not take an order, you cannot take an order further down the line.

Under these conditions, you want to take as many orders as possible.


## Input
The first line of input will contain two space-separated integers: `N` and `T`. `N` is the total number of orders and `T` is the number of distinct types of items. The next line contains `T` entries: <code>S<sub>1</sub></code>, <code>S<sub>2</sub></code>, …, <code>S<sub>T</sub></code>, all of which are space-separated strings. The string <code>S<sub>i</sub></code> `(1 ≤ i ≤ T)` represents the name of the `i`-th item. The line after that contains `T` space-separated integers: <code>Q<sub>1</sub></code>, <code>Q<sub>2</sub></code>, …, <code>Q<sub>T</sub></code>, where <code>Q<sub>i</sub></code> `(1 ≤ i ≤ T)` represents the maximum quantity of <code>S<sub>i</sub></code> that you can smuggle. The next `N` lines contain two space-separated entries: a string <code>w<sub>j</sub></code> and an integer <code>x<sub>j</sub></code> `(1 ≤ j ≤ N)`. Each line is an order to smuggle <code>x<sub>j</sub></code> of item <code>w<sub>j</sub></code>.

## Output
Output one integer: the length of the longest consecutive line of orders you can take while staying under the limit for each item. If you cannot take any order, output `0`.


## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>5</td>
        <td><code>1 ≤ N ≤ 100</code><br>
			<code>1 ≤ T ≤ 10</code><br>
			<code>S<sub>i</sub> has length at most 10</code><br>
			<code>1 ≤ Q<sub>i</sub>, w<sub>j</sub> ≤ 100</code><br>
			<code>For all 1 ≤ j ≤ N, there exists 1 ≤ k ≤ N such that x<sub>j</sub> = S<sub>k</sub></code></td>
    </tr>
    <tr>
        <td>5</td>
        <td><code>1 ≤ N ≤ 10<sup>4</sup></code><br>
		<code>1 ≤ T ≤ 10</code><br>
		<code>S<sub>i</sub> has length at most 10</code><br>
		<code>1 ≤ Q<sub>i</sub>, w<sub>j</sub> ≤ 10<sup>4</sup></code><br>
		<code>For all 1 ≤ j ≤ N, there exists 1 ≤ k ≤ N such that x<sub>j</sub> = S<sub>k</sub></code></td>
    </tr>
</table>
