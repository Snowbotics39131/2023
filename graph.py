try:
    from matplotlib import pyplot as plt
    mpl=True
except ImportError:
    mpl=False
class Graph:
    def __init__(self):
        self.vertices={}
        self.edges={}
    def add_vertex(self, x, y):
        try:
            id_=max(self.vertices)+1
        except ValueError:
            id_=0
        self.vertices[id_]=(x, y)
        for i in self.edges:
            self.edges[i][id_]=False
        self.edges[id_]={}
        for i in self.edges:
            self.edges[id_][i]=False
        self.edges[id_][id_]=True
        return id_
    def del_vertex(self, id_):
        del(self.vertices[id_])
        del(self.edges[id_])
        for i in self.edges:
            del(self.edges[i][id_])
    def get_id_from_coordinates(self, x, y):
        return list(self.vertices.keys())[list(self.vertices.values()).index((x, y))]
    def get_coordinates_from_id(self, id_):
        return self.vertices[id_]
    def list_vertices(self):
        return list(self.vertices.keys())
    def add_edge(self, vertex1, vertex2):
        self.edges[vertex1][vertex2]=True
        self.edges[vertex2][vertex1]=True
    def del_edge(self, vertex1, vertex2):
        self.edges[vertex1][vertex2]=False
        self.edges[vertex2][vertex1]=False
    def check_connected(self, vertex1, vertex2):
        return self.edges[vertex1][vertex2]
    def list_connected(self, id_):
        output=[]
        for i in self.edges:
            if self.edges[id_][i]:
                output.append(i)
        return output
    def edge_length(self, vertex1, vertex2):
        if self.check_connected(vertex1, vertex2):
            vertex1=self.get_coordinates_from_id(vertex1)
            vertex2=self.get_coordinates_from_id(vertex2)
            return ((vertex1[0]-vertex2[0])**2+(vertex1[1]-vertex2[1])**2)**0.5 #Pythagorean Theorem
        else:
            raise ValueError('vertices not connected')
    def plot(self):
        if mpl:
            plt.axis('equal')
            plt.scatter(list(i[0] for i in list(self.vertices.values())), list(i[1] for i in list(self.vertices.values())), color='#000000')
            for i in self.edges:
                for j in self.edges[i]:
                    if self.edges[i][j]:
                        plt.plot([self.get_coordinates_from_id(i)[0], self.get_coordinates_from_id(j)[0]], [self.get_coordinates_from_id(i)[1], self.get_coordinates_from_id(j)[1]], color='#000000')
            plt.show()
        else:
            print('Run with Matplotlib to plot graphs.')
    connect=add_edge
    disconnect=del_edge
def dijkstra(graph, start, end):
    dist={}
    prev={}
    for v in graph.list_vertices():
        dist[v]=999999999
        prev[v]=None
    dist[start]=0
    explored=[]
    unexplored=graph.list_vertices()
    while end not in explored:
        v=min(unexplored, key=lambda x: dist[x])
        del(unexplored[unexplored.index(v)])
        explored.append(v)
        for w in graph.list_connected(v):
            if dist[v]+graph.edge_length(v, w)<dist[w]:
                dist[w]=dist[v]+graph.edge_length(v, w)
                prev[w]=v
    def path_from_prevs(vertex):
        if vertex==start:
            return [start]
        return path_from_prevs(prev[vertex])+[vertex]
    return path_from_prevs(end)

if __name__=='__main__':
    test=Graph()
    test.add_vertex(1, 0)
    test.add_vertex(1, 1)
    test.add_vertex(0, 2)
    test.add_vertex(2, 2)
    test.add_vertex(1, 3)
    test.add_vertex(1, 4)
    test.add_edge(test.get_id_from_coordinates(1, 0), test.get_id_from_coordinates(1, 1))
    test.add_edge(test.get_id_from_coordinates(1, 1), test.get_id_from_coordinates(0, 2))
    test.add_edge(test.get_id_from_coordinates(1, 1), test.get_id_from_coordinates(2, 2))
    test.add_edge(test.get_id_from_coordinates(0, 2), test.get_id_from_coordinates(2, 2))
    test.add_edge(test.get_id_from_coordinates(0, 2), test.get_id_from_coordinates(1, 3))
    test.add_edge(test.get_id_from_coordinates(2, 2), test.get_id_from_coordinates(1, 3))
    test.add_edge(test.get_id_from_coordinates(1, 3), test.get_id_from_coordinates(1, 4))
    test.plot()
    path=dijkstra(test, test.get_id_from_coordinates(1, 0), test.get_id_from_coordinates(1, 4))
    path=list(test.get_coordinates_from_id(i) for i in path)
    print(path)