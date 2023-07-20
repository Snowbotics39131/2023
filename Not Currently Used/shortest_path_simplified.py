def line_intersects_polygon(line, polygon):
    print(line,polygon)
    x1, y1 = line[0]
    x2, y2 = line[1]
    
    for i in range(len(polygon)):
        x3, y3 = polygon[i]
        x4, y4 = polygon[(i + 1) % len(polygon)]
        
        dx1, dy1 = x2 - x1, y2 - y1
        dx2, dy2 = x4 - x3, y4 - y3

        denominator = dx1*dy2 - dy1*dx2

        if denominator == 0:
            # Lines are parallel or coincident
            continue

        t1 = ( (x1-x3)*dy2 + (y3-y1)*dx2 ) / denominator
        t2 = ( (x3-x1)*dy1 + (y1-y3)*dx1 ) / -denominator
        print(t1,t2)
        if 0 <= t1 <= 1 and 0 <= t2 <= 1:
            # Lines intersect within their segments
            print(True)
            return True
            
        #if (t1 < 0 or t1 > 1) and (t2 < 0 or t2 > 1):
            # Check if the line separates the two points in the polygon
            #return True
    
    # Line does not intersect the polygon
    print(False)
    return False
    
'''def shortest_path(start, end, obstacles):
    path = [start]  # Start path with the starting point
    
    def find_path(current, remaining, path):
        if current == end:
            # Reached the end point, return the path
            path.append(end)
            return path
        
        shortest = None
        for next_point in remaining:
            if not line_intersects_polygon((current, next_point), obstacles):
                # Check if the line between current and next_point intersects with any obstacles
                next_remaining = remaining.copy()
                next_remaining.remove(next_point)
                next_path = find_path(next_point, next_remaining, path + [next_point])
                
                if shortest is None or len(next_path) < len(shortest):
                    # Update the shortest path found so far
                    shortest = next_path
        
        return shortest
    
    remaining_points = [point for point in obstacles] + [end]
    return find_path(start, remaining_points, path)

if __name__=='__main__':
    from matplotlib import pyplot as plt
    obstacles =[[[2, 3], [0, 4], [2, 5]]]
    path = shortest_path([1, 0], [1, 8],obstacles)
    print(path)
    for i in obstacles:
        plt.fill(list((j[0] for j in i)), list((j[1] for j in i)), color='#808080', edgecolor='#000000')
    plt.plot(list(i[0] for i in path), list(i[1] for i in path), marker='o', color='#ff0000')
    plt.show()
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
                        if line_intersects_polygon(i, j, k):
                            ok=False
                            break
                    if ok:
                        plt.plot([i[0], j[0]], [i[1], j[1]], color='#0000ff')
            plt.plot(list(i[0] for i in path), list(i[1] for i in path), marker='o', color='#ff0000')
            plt.show()
    driver([[[1, 1], [1, 2], [2, 2], [2, 1]]], [0, 0], [3, 3])
    driver([[[1, 1], [1, 2], [2, 2], [2, 1]], [[3, 1], [3, 2], [4, 2], [4, 1]]], [0, 0], [5, 3])
    driver([[[0, 1], [2, 2], [0, 3]], [[2, 3], [0, 4], [2, 5]], [[0, 5], [2, 6], [0, 7]]], [1, 0], [1, 8])'''
print(line_intersects_polygon([[0, 0], [3, 3]],[[1, 1], [1, 2], [2, 2], [2, 1]]))
print(line_intersects_polygon([[0, 1], [3, 4]],[[1, 1], [1, 2], [2, 2], [2, 1]]))
print(line_intersects_polygon([[0, 1], [3, 4]],[[1, 1], [1, 2], [2, 2], [2, 1]]))

'''
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

def shortest_path(start, end, obstacles, avoid=[]):
    global spruns
    spruns+=1
    straight=True
    for i in obstacles:
        if line_intersects_polygon((start, end), i):
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
                    if line_intersects_polygon((start, j), k):
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
                        if line_intersects_polygon((i, j), k):
                            ok=False
                            break
                    if ok:
                        plt.plot([i[0], j[0]], [i[1], j[1]], color='#0000ff')
            plt.plot(list(i[0] for i in path), list(i[1] for i in path), marker='o', color='#ff0000')
            plt.show()
    driver([[[1, 1], [1, 2], [2, 2], [2, 1]]], [0, 0], [3, 3])
    driver([[[1, 1], [1, 2], [2, 2], [2, 1]], [[3, 1], [3, 2], [4, 2], [4, 1]]], [0, 0], [5, 3])
    driver([[[0, 1], [2, 2], [0, 3]], [[2, 3], [0, 4], [2, 5]], [[0, 5], [2, 6], [0, 7]]], [1, 0], [1, 8])'''