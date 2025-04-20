You, Drofo Gabbins, have learned that your enemy Lord Rauson is taking a series of flights to a vacation spot. Since he has no more jewellery for you to steal, you have decided to take this opportunity to sabotage Rauson’s vacation.

You know that Rauson has some flight options from city to city. These options will be given as inputs. Additionally, you know where Rauson will start and end his vacation. Since he is very smart, he will find the fastest possible route to get from his starting point to his destination. Note that he spends no time between flights.

You will be able to disable one flight from Rauson’s options, and your goal is to make Rauson’s vacation either impossible or take as long as it can. Rauson will only choose his flight path after you have disabled a flight. Flights are one-directional and cannot be reversed. For example, if there is a flight from `Atlanta` to `Baltimore`, you may not take this same flight to go from `Baltimore` to `Atlanta` (but there may be another flight from `Baltimore` to `Atlanta`).

## Input
The first line contains two space-separated integers, `N`, the total number of flights Rauson can take and `C`, the number of total cities that Rauson can fly to (including his start point and destination). The second line contains two space-separated strings: the names of his start and end point, in that order. The next `N` lines contain three space-separated entities representing one flight. The first entity is a string representing the start point of the flight, the second entity is a string representing the end point of the flight, and the third entity is a positive integer <code>T<sub>i</sub></code> `(1 ≤ i ≤ N)`, representing how much time that flight takes (in hours). There will never be two flights with the same start and end points.

## Output
If it is possible to completely disconnect the start and end points of the vacation (making the vacation impossible), or if the vacation was already impossible in the first place, output `-1`. Otherwise, output one integer: the maximum amount of flight time it would take Rauson to complete his vacation by disabling a flight, assuming he tries to make it as quick as possible.

## Point Distribution
<table>
    <tr>
        <th>Points</th>
        <th>Restrictions</th>
    </tr>
    <tr>
        <td>6</td>
        <td><code>2 ≤ C, N ≤ 10</code><br>
			<code>1 ≤ T<sub>i</sub> ≤ 100</code></td>
    </tr>
    <tr>
        <td>6</td>
        <td><code>2 ≤ C ≤ 100</code><br>
			<code>2 ≤ N ≤ 1000</code><br>
			<code>1 ≤ T<sub>i</sub> ≤ 1000</code></td>
    </tr>
</table>
