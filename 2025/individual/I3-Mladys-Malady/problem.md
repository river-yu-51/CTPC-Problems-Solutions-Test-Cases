It is the year 420 and the Queen has gotten sick! As the royal family's doctor, it is your job to craft a potion that can nurse the Queen back to health.

To do this, you will need to use your recipe book and create a specific potion out of the potions that you have in your desposal! The book contains recipes that are given as `A + B → C`, indicating that mixing one unit of potion `A` and one unit of potion `B` yields one unit of potion `C`. (No balancing chemical equations!)

Note that for any potion `C` that is referenced in the recipe book, there will be at most one recipe where `C` is the product (that is, there won't be two distinct recipes that both yield `C`). Furthermore, if potion `A` is used to make potion `C`, then potion `C` will not be in the recipe that makes `A`.
However, it is possible for the same ingredient to be used in the synthesis of two different ingredients.

Since you want to be as resourceful as possible, you decide to use as few potions as you can to craft the required healing potion.


## Input
The first line contains one string <code>S<sub>r</sub></code>: the name of the potion required to heal the Queen. The second line contains two space-separated integers: `P`, the number of types of potions in your stores, and `N`, the number of recipes in the book.
The next line contains `P` strings: <code>s<sub>1</sub></code>, <code>s<sub>2</sub></code>, ..., <code>s<sub>P</sub></code>, where <code>s<sub>i</sub></code> `(1 ≤ i ≤ P)` is the name of the `i`-th potion you have. The next line contains `P` space-separated integers: <code>q<sub>1</sub></code>, <code>q<sub>2</sub></code>, ..., <code>q<sub>P</sub></code>, where <code>q<sub>i</sub></code> `(1 ≤ i ≤ P)` is the quantity of the `i`-th potion you have.
The next `N` lines contain three space-separated strings each: <code>r<sub>(j, 1)</sub></code>, <code>r<sub>(j, 2)</sub></code>, <code>p<sub>j</sub></code> `(1 ≤ j ≤ N)`, where <code>r<sub>(j, 1)</sub></code> and <code>r<sub>(j, 2)</sub></code> represent the two inputs of the `j`-th recipe and <code>p<sub>j</sub></code> represents the output of the `j`-th recipe (reactants and products, if you will).

## Output
Output the minimum total number of potions you need from your stores to create potion <code>S<sub>r</sub></code>. If this is impossible with what you have, output `-1`.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>3</td>
        <td><code>1 ≤ P, N ≤ 50</code></br>
            <code>1 ≤ q<sub>i</sub> ≤ 1000</code></br>
            <code>S<sub>r</sub>, s<sub>i</sub> has length at most 20</code></br>
    </tr>
    <tr>
        <td>2</td>
        <td><code>1 ≤ P, N ≤ 1000</code></br>
            <code>1 ≤ q<sub>i</sub> ≤ 10<sup>9</sup></code></br>
            <code>S<sub>r</sub>, s<sub>i</sub> has length at most 20</code></br>
    </tr>
</table>
