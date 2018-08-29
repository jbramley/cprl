import random


class GridGraph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.graph = self.init_graph(width, height)
        print(len(self.graph))
        self.permanent_edges = []

    @staticmethod
    def init_graph(width, height):
        graph = []
        for w in range(width):
            for h in range(height):
                if w < width - 1:
                    graph += [((w,h),(w+1, h))]
                if h < height - 1:
                    graph += [((w,h),(w, h+1))]
        return graph

    def is_fully_connected(self):
        n = self.graph[0][0]
        num_edges = len(self.graph)
        checked_edges = []
        check_count = self.count_edges(n, checked_edges)
        return check_count == num_edges

    def count_edges(self, node, checked_edges):
        edges = [e for e in self.graph if node in e]
        cnt = 0
        for e in edges:
            if e in checked_edges:
                continue
            checked_edges.append(e)
            if e[0] == node:
                n = e[1]
            else:
                n = e[0]
            cnt += 1 + self.count_edges(n, checked_edges)
        return cnt

    def generate_map(self, sparseness):
        ideal_len = len(self.graph)*sparseness
        choice_edges = self.graph.copy()
        while len(choice_edges) + len(self.permanent_edges) > ideal_len and len(choice_edges) > 0:
            e = random.choice(choice_edges)
            self.graph.remove(e)
            if not self.is_fully_connected():
                self.graph.append(e)
                self.permanent_edges.append(e)
            choice_edges.remove(e)

    def nodes(self):
        return list(set([node for edge in self.graph for node in edge]))

    def edges(self):
        return self.graph
