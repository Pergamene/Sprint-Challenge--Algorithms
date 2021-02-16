#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - looping until n^3, but increasing by n^2.

b) O(nlogn) - the for loop is looping n times, and the nested while loop is looping logn times since j doubles everytime.

c) O(n) - it does one recursive call for n to 0.

## Exercise II

To minimize the number of eggs dropped the best approach will be to use the binary search algorithm, where we are looking for the lowest floor where an egg breaks:
Start on the middle floor, if the egg breaks then move down half way from the middle to the bottom, if the egg doesn't break then move up half way between the middle floor and the top.  From there drop again and move up or down to the middle again.  Do this until you have found the lowest floor that breaks an egg.  
The complexity of this approach is O(logn) since we are eliminating half of the remaining rooms each time.
