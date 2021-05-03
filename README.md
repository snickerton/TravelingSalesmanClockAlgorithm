# TSP Clock Algorithm

I came up with my own Traveling Salesman Solution that creates a simple polygon (no intersecting sides) from a list of euclidean coordinate points. Then I spent a night trying to see how bad it was.

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
3) Solve P=NP and collect my cool 1 million dollars

![image3](https://raw.githubusercontent.com/snickerton/TravelingSalesmanClockAlgorithm/main/ezgif-2-a2838b4a6f42.gif)

## The Python Application 
I ended up making a 
