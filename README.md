# TSP Clock Algorithm

I came up with my own Traveling Salesman Solution that creates a simple polygon (no intersecting sides) from a list of euclidean coordinate points. Then I spent a night demonstrating how bad it was.

## Background

Without going into too much background, it seemed intuitive to me (and ends up being mathematically correct) that an optimal path should not have intersecting paths. The [Convex Hull algorithm](http://web.mit.edu/course/other/urban_or_book/www/book/chapter6/6.4.7.html) is one I immediately found which took advantage of this. 

My ELI5 of Convex Hull: 
1) Find the smallest polygon with only convex corners that encloses all the points
2) Add the points inside the the polygon while minimizing cost (path length)

![image1](https://www2.isye.gatech.edu/~mgoetsch/cali/VEHICLE/TSP/IMG00018.GIF)
![image2](https://www2.isye.gatech.edu/~mgoetsch/cali/VEHICLE/TSP/IMG00021.GIF)

And to be fair, this is pretty cool and works great. But I couldn't figure out why my original idea wasn't as optimal:

*Can't I just average the points, get a center, and then go clockwise around it and find my path?*

## Clock Algorithm Explanation
My ELI5 of the patented Tony Zhu Clock&trade; Algorithm:
1) Attach a clock hand to the centroid found
2) The order which points hit the hand as it spins clockwise is your path
3) Solve P=NP and collect a cool 1 million dollars

![image3](https://raw.githubusercontent.com/snickerton/TravelingSalesmanClockAlgorithm/main/ezgif-2-a2838b4a6f42.gif)

`Note: center point was eye-balled with sleep deprivation`

## The Python Application 
The python program enclosed does the following:
1) Generates N random points
2) Solves using the Clock Algorithm
3) Tries to beat it with brute force
4) Graphs everything in a cute matplotlib with animations
5) Solves P=NP and collects a cool million dollars for me

![image4](https://raw.githubusercontent.com/snickerton/TravelingSalesmanClockAlgorithm/main/clock_tsp_demo.gif)

`Final values in gif: Clock -> 287.9 | Brute Force Limited -> 284.2`


II also want to take a moment to highlight (or lowlight) one of the more "wtf dumb/genius" things I've done in my life. In this program we run a recursive brute force method and then *stop the recursion* when we beat a pre-existing record. To "break;" out of the recursive function **AND** return a value (the new best path) I pulled the following move:
1) If the new path length has reached the improvement threshold (i.e. we want anything that improves more than 1%)
2) Raise an Exception and encode the return value *in the error message*
3) Catch said Exception and use repr() to convert the message to a string
4) Clean the string so it's just the payload
5) Use eval() to make the python compiler evaluate the string as if it's code (an array)
6) Bingo bango, recursion dead, new path acquired, P=NP solved

## Verdict
It mostly sucks.

Brute force is able to beat it if the number of points is below like 12. On the upside, the speed at which the "Clock path" is calculated is probably pretty darn fast compared to other algorithms. Off the top of my head, the time complexity is O(n) for geometry stuff (angles, average center), plus O(nlogn) for sorting (angles in ascending/clockwise order). You also have to remember this outputs a non-intersecting solution; other algorithms at this time complexity and/or take sub-second calculation times probably can't say the same.


If I ever come back to this, I definitely want to try slapping 2-opt onto that bad boy and seeing how good the solution can get at a rapid rate. There's a bunch of interesting patterns and math stuff I found on how to improve the Clock path and why it sucks to begin with, but that's a write-up for another time.
