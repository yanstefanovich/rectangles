# Rectangles

This is my solution to a coding challenge as a part of an interview process.

I was so happy with my approach to get the solution, so much so that I decided to capture it in this repo.

## Objective
Implement algorithms to analyze characteristics between two rectangles and the data structure to define a rectangle:
1. ***Intersection***: Determine if the two rectangles have intersecting lines.<br>
<img src="./images/intersection.png" width="50%" alt="Example of intersection"><img src="./images/intersection-no.png" width="50%" alt="Example of no intersection">

2. ***Containment***: Determine if a rectangle is wholly contained within another rectangle.<br>
<img src="./images/containment.png" width="50%" alt="Example of containment"><img src="./images/containment-no.png" width="50%" alt="Example of no containment">

1. ***Adjacency***: Determine if the two rectangles are adjacent.<br>
<img src="./images/adjacency-whole.png" width="50%" alt="Example of partial adjacency"><img src="./images/adjacency-partial.png" width="50%" alt="Example of partial containment">
<img src="./images/adjacency-sub-line.png" width="50%" alt="Example of sub-line adjacency"><img src="./images/adjacency-no.png" width="50%" alt="Example of no adjacency">

## My Approach
### The Data Structure
My starting point was thinking of how to approach the data structure. Traditionally, mapping out a rectangle mathematically, one would define it by its four verteces on the cartesian plane. This yeilds in 4 sets of 2 data points, one for each vertex. The resulting data structure may look something like this: `[[0,0], [1,0], [1,1], [0,1]]` &mdash; starting from the lower left vertex and moving in a clockwise direction. I do not like this approach for two reasons:
1. There is a lot of data to work through and there is not a good way to organize it semantically.
2. I felt like finding the solution with that approach would require more mathematical calculations than was necessary for this problem.

Next, I tried to see what the data structure would look like if I defined the edges instead. In my first iteration of this approach I mapped out the edges as they run on the rectangle starting from the lower left vertex. My initial data structure looked something like this:
```
    y      x      y      x
 [[0,1], [0,1], [1,0], [1,0]]
 ```
 I quickly realized the redundancy in this approach. Going around the rectangle clockwise, at the top right vertext, on the way back to wards the lower left vertex, we get the negated version of the same edge and thus it was sufficient to denote only one of the y and one of the x edges &mdash; `[[0,1], [0,1]]`. To improve the semantics, I changed the data structure from an array to an object:
 ```
 {
   x: [starting position, ending position],
   y: [starting position, ending position]
 }

 Example:
 { x: [0,1], y: [0,1] }
 ```
 The result is a smaller/simplified data set over the vertex method and in my opinion it is also easier to grasp at a glance.

 ## Intersection