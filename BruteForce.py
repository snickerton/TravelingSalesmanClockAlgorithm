import numpy as np
import math

class BruteForce:
    def __init__(self, best):
        self.smallest_route = best
        self.best_lis = []

    def calculate_length(self, lis, coors):
        path2 = 0
        prev_point = coors[lis[0]]
        for index in lis[1:]:
            point = coors[index]
            vector = np.subtract(point, prev_point)
            path2 += math.sqrt(vector[0] ** 2 + vector[1] ** 2)
            prev_point = point

        point = coors[lis[0]]
        vector = np.subtract(point, prev_point)
        path2 += math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        return path2

    def brute_force(self, lis, coors, remain, improvement_limit):
        # if calculate_length(lis,coors)>smallest_route:
        #     # if the path is already larger than our best, we're not going to somehow improve
        #     return

        if len(remain) == 0:
            tes = lis
            dis = self.calculate_length(tes,coors)
            # print(dis)
            if dis < self.smallest_route:
                print("Winning: ", str(tes))
                self.best_lis = tes
                if ((self.smallest_route-dis) / self.smallest_route) > improvement_limit:
                    raise Exception(self.best_lis)
                smallest_route = dis
                print("New found! dis: {} \n \t {}".format(dis, str(tes)))
                with open("BestPath.txt","a") as f:
                    f.write(str(dis)+"\t" + str(tes) + "\n")
            return

        for i,x in enumerate(remain):
            self.brute_force(lis+[x], coors, [t for t in remain if t != x], improvement_limit)
        return self.best_lis
