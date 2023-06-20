spruns=0
def length_of_path(path):
    path=list(zip(path, path[1:]+path[:1]))
    del(path[len(path)-1])
    length=0
    for i in path:
        length+=((i[0][0]-i[1][0])**2+(i[0][1]-i[1][1])**2)**(1/2)
    return length
def shortest_from_paths(paths):
    if len(paths)==0:
        return None
    shortest=paths[0]
    min_length=999999999
    for i in paths:
        if length_of_path(i)<min_length:
            shortest=i
            min_length=length_of_path(i)
    return shortest
def point_of_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    return [(x2*(x3-x4)*y1+x1*(x4-x3)*y2+(x2-x1)*(x4*y3-x3*y4))/((x3-x4)*y1+(x4-x3)*y2+(x2-x1)*(y3-y4)), (x1*y2*(y4-y3)+x2*y1*(y3-y4)+(y1-y2)*(x3*y4-x4*y3))/(x1*(y4-y3)+x2*(y3-y4)+(x3-x4)*(y1-y2))]
def intersect(a, b, c, d, norecurse=False):
    try:
        intersection=point_of_intersection(a[0], a[1], b[0], b[1], c[0], c[1], d[0], d[1])
    except ZeroDivisionError:
        if not norecurse:
            return intersect(*([i[1], i[0]] for i in [a, b, c, d]), norecurse=True)
        return 0
    if intersection[0]>max(a[0], b[0]) or intersection[0]<min(a[0], b[0]):
        return 0
    if intersection[0]>max(c[0], d[0]) or intersection[0]<min(c[0], d[0]):
        return 0
    if intersection[1]>max(a[1], b[1]) or intersection[1]<min(a[1], b[1]):
        return 0
    if intersection[1]>max(c[1], d[1]) or intersection[1]<min(c[1], d[1]):
        return 0
    if intersection in [a, b, c, d]:
        return 1
    if intersection[0] in [a[0], b[0], c[0], d[0]]:
        return 2
    if intersection[1] in [a[1], b[1], c[1], d[1]]:
        return 2
    return 3
def goes_through_obstacle(a, b, obstacle):
    pairs=list(zip(obstacle, obstacle[1:]+obstacle[:1]))
    if a in obstacle and b in obstacle:
        if (a, b) in pairs or (b, a) in pairs:
            return False
        return True
    for i in pairs:
        if a not in i and b not in i:
            if intersect(a, b, i[0], i[1])>=1:
                return True
    return False
def shortest_path(start, end, obstacles, avoid=[]):
    global spruns
    spruns+=1
    straight=True
    for i in obstacles:
        if goes_through_obstacle(start, end, i):
            straight=False
            break
    if straight:
        return [start, end]
    possible_paths=[]
    for i in obstacles:
        for j in i:
            ok=True
            if (j not in avoid) and j!=start:
                for k in obstacles:
                    if goes_through_obstacle(start, j, k):
                        ok=False
                        break
            else:
                ok=False
            if ok:
                maybe_path=shortest_path(j, end, obstacles, avoid+[start]+[j])
                if maybe_path!=None:
                    possible_paths.append([start]+maybe_path)
    return shortest_from_paths(possible_paths)

if __name__=='__main__':
    try:
        from matplotlib import pyplot as plt
        mpl=True
    except ImportError:
        print('Run in CPython with Matplotlib to show the paths.')
        mpl=False
    def driver(obstacles, start, end):
        global spruns
        spruns=0
        path=shortest_path(start, end, obstacles)
        print('Total shortest_path runs', spruns)
        print('Obstacles', obstacles)
        print('Path', path)
        print()
        if mpl:
            plt.axis('equal')
            for i in obstacles:
                plt.fill(list((j[0] for j in i)), list((j[1] for j in i)), color='#808080', edgecolor='#000000')
            points=[start, end]
            for i in obstacles:
                points+=i
            for i in points:
                for j in points:
                    ok=True
                    for k in obstacles:
                        if goes_through_obstacle(i, j, k):
                            ok=False
                            break
                    if ok:
                        plt.plot([i[0], j[0]], [i[1], j[1]], color='#0000ff')
            plt.plot(list(i[0] for i in path), list(i[1] for i in path), marker='o', color='#ff0000')
            plt.show()
    driver([[[1, 1], [1, 2], [2, 2], [2, 1]]], [0, 0], [3, 3])
    driver([[[1, 1], [1, 2], [2, 2], [2, 1]], [[3, 1], [3, 2], [4, 2], [4, 1]]], [0, 0], [5, 3])
    driver([[[0, 1], [2, 2], [0, 3]], [[2, 3], [0, 4], [2, 5]], [[0, 5], [2, 6], [0, 7]]], [1, 0], [1, 8])
