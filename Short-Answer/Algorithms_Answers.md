#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Since we are looping only once through our data, time complexity scales in a linear fashion in relation to input size. Also, the size of n does not influence the time complexity with regard to the mathematical operations being conducted (multiplication).


b) O(n^2) - Nested for loops are very taxing on performance, essentially squaring the size of our input data. The more for loops we have, the greater our performance will suffer.


c) O(n) - Like the first example, our performance scales in proportion to n. It's also decreasing by one in size with each recursive call.

## Exercise II

As I understand it, we are writing a function that figures out the highest floor from which we can toss eggs out of a building safely without having them break.

Assuming the building height is a sorted list (floors 1 throug n), a possible way to tackle the problem would be conducting a binary search through the floors, rather than test each one individually. This way, we could start from the midpoint of building floors, and depending on whether or not the egg breaks when dropped, we know whether to go higher or lower through our list of floors. Eventually halving our data this way will land us on the first floor where eggs begin to break.

Since we are using a binary search that constantly halves our data, time complexity would be O(log n), more formally known as Logarithmic time.