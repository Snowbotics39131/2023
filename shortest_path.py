from graph import Graph, dijkstra
def point_of_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    return [(x2*(x3-x4)*y1+x1*(x4-x3)*y2+(x2-x1)*(x4*y3-x3*y4))/((x3-x4)*y1+(x4-x3)*y2+(x2-x1)*(y3-y4)), (x1*y2*(y4-y3)+x2*y1*(y3-y4)+(y1-y2)*(x3*y4-x4*y3))/(x1*(y4-y3)+x2*(y3-y4)+(x3-x4)*(y1-y2))]
def intersect(a, b, c, d, norecurse=False):
    try:
        intersection=point_of_intersection(a[0], a[1], b[0], b[1], c[0], c[1], d[0], d[1])
    except ZeroDivisionError:
        if not norecurse:
            return intersect(*([i[1], i[0]] for i in [a, b, c, d]), norecurse=True)
        return 0
    if intersection[0]>min(max(a[0], b[0]), max(c[0], d[0])) or intersection[0]<max(min(a[0], b[0]), min(c[0], d[0])):
        return 0
    if intersection[1]>min(max(a[1], b[1]), max(c[1], d[1])) or intersection[1]<max(min(a[1], b[1]), min(c[1], d[1])):
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
def shortest_path(start, end, obstacles):
    graph=Graph()
    points=[start, end]
    for i in obstacles:
        points+=i
    for i in points:
        graph.add_vertex(*i)
    for i in points:
        for j in points:
            ok=True
            for k in obstacles:
                if goes_through_obstacle(i, j, k):
                    ok=False
                    break
            if ok:
                graph.add_edge(graph.get_id_from_coordinates(*i), graph.get_id_from_coordinates(*j))
    output=dijkstra(graph, graph.get_id_from_coordinates(*start), graph.get_id_from_coordinates(*end))
    output=list(graph.get_coordinates_from_id(i) for i in output)
    return output
if __name__=='__main__':
    try:
        from matplotlib import pyplot as plt
        mpl=True
    except ImportError:
        print('Run in CPython with Matplotlib to show the paths.')
        mpl=False
    try:
        from pybricks.tools import StopWatch
    except ImportError:
        from time import perf_counter
        class StopWatch:
            def time(*args, **kwargs):
                return perf_counter()
    timer=StopWatch()
    def driver(obstacles, start, end):
        tick=timer.time()
        path=shortest_path(start, end, obstacles)
        tock=timer.time()
        print('Time', tock-tick)
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
