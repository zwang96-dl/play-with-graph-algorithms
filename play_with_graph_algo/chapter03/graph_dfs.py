from play_with_graph_algo.chapter02.adj_set import AdjSet as Graph


class GraphDFS:

    def __init__(self, G):
        self._pre_order = []
        self._post_order = []
        self._G = G
        self._visited = [False] * G.V

        # 遍历所有的点，相当于遍历图中所有可能存在的联通块
        for v in range(G.V):
            if not self._visited[v]:
                self._dfs(v)

    def _dfs(self, v):
        self._visited[v] = True
        self._pre_order.append(v)
        for w in self._G.adj(v):
            if not self._visited[w]:
                self._dfs(w)
        self._post_order.append(v)
    
    @property
    def pre_order(self):
        return self._pre_order

    @property
    def post_order(self):
        return self._post_order


if __name__ == '__main__':
    # 一个联通块的图
    filename = 'play_with_graph_algo/chapter03/g1.txt'
    g = Graph(filename)
    graph_dfs = GraphDFS(g)
    print(graph_dfs.pre_order)
    print(graph_dfs.post_order)

    print('*' * 40)

    # 两个联通块的图
    filename = 'play_with_graph_algo/chapter03/g2.txt'
    g = Graph(filename)
    graph_dfs = GraphDFS(g)
    print(graph_dfs.pre_order)
    print(graph_dfs.post_order)
