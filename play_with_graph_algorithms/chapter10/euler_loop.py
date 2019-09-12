from play_with_graph_algorithms.chapter02.adj_set import AdjSet as Graph
from play_with_graph_algorithms.chapter04.cc import CC


class EulerLoop:
    def __init__(self, G):
        self._G = G
    
    def has_euler_loop(self):
        cc = CC(self._G)
        if cc.ccount > 1:
            return False

        for v in range(self._G.V()):
            if self._G.degree(v) % 2 != 0:
                return False

        return True
