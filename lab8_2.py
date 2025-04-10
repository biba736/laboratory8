class Graph:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, V = None, E = None):
        self.V = set()
        self.E = set()
        self._vertice_labels = {}
        self._edge_labels = {}
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for e in E:
                self.add_edge(e)

    # метод конструирования строкового представления графа
    def __str__(self):
        str_vertices = "vertices:\n" + " ".join(sorted(self.V))
        str_edges = "edges:"
        for e in sorted(self.E):
            str_edges += f"\n{e[0]} -> {e[1]}"
        return str_vertices + "\n" + str_edges

    # метод добавления метки вершине или ребру
    def __setitem__(self, x, d):
        if type(x) is tuple:
            if x in self.E:
                self._edge_labels[x] = d
            else:
                raise KeyError("Данного ребра не существует")
        else:
            if x in self.V:
                self._vertice_labels[x] = d
            else:
                raise KeyError("Данной вершины не существует")

    # метод возврата метки вершины или ребра
    def __getitem__(self, x):
        if type(x) is tuple:
            return self._edge_labels.get(x, None)
        else:
            return self._vertice_labels.get(x, None)

    # Добавляет в граф вершину v. Метка вершины должна быть None.
    def add_vertex(self, v):
        self.V.add(v)
        if v not in self.V:
            self._vertice_labels[v] = None

    # Добавляет в граф ориентированное ребро e. Ребро е представляется кортежем (класс tuple)
    # двух имён рёбер (v, u). Метка ребра устанавливается в None.
    def add_edge(self, e):
        self.E.add(e)
        if e not in self.E:
            self._edge_labels[e] = None

    # генератор или итератор, перечисляющий все рёбра графа
    def edges(self):
        return sorted(self.E)


    # генератор или итератор, перечисляющий все вершины графа
    def vertices(self):
        return sorted(self.V)


    # генератор или итератор, перечисляющий все рёбра, выходящие из вершины v
    def outgoing(self, v):
        return sorted([i for i in self.E if i[0] == v])

# функция, создающая граф де Брёйна
def construct_de_Brujin(patterns):
    g = Graph()
    for pattern in patterns:
        g.add_vertex(pattern[:-1])
        g.add_vertex(pattern[1:])
        g.add_edge((pattern[:-1], pattern[1:]))

    return g

# считываем строки в patterns, пока не кончатся
patterns = []
while True:
    try:
        line = input()
        patterns.append(line)
    except EOFError:
        break

G = construct_de_Brujin(patterns)
print(G)