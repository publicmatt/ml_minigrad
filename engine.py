import numpy as np
import seaborn.objects as so
from graphviz import Digraph

x = np.arange(-50, 50)
y = x ** 2

plot = so.Plot(x=x, y=y).add(so.Line())

plot.show()

class Value:
    def __init__(self, data, _children=(), _opt='', label=''):
        self.data = data
        self._opt = _opt
        self._prev = set(_children)
        self.label = label
    def __repr__(self):
        return f"<Value {self.label}: {{data : {self.data:.2f}}}>"
    def __add__(self, other):
        return Value(self.data + other.data, (self, other), '+')
    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), '*')

class Graph
    def __init__(self, root):
        self.root = root
    def _build(self):
        nodes, edges = set(), set()
        def accumulate(v):
            if v is not in nodes:
                nodes.add(v)
                for u in v._prev:
                    edges.add((u, v))
                    build(u)
        accumulate(self.root)
        return nodes, edges
    def draw():
        dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})
        nodes, edges = self._build()
        for n in nodes:
            uid = str(id(n))
            dot.node(name=uid, label=f"{n.data:.4f}", shape="record")
            if n._op:
                dot.node(name=uid+n._opt, label=n._opt)
                dot.edge(uid+n._opt, uid) 
        for u, v in edges:
            dot.edge(str(id(u)), str(id(v)) + v._opt)


a = Value(5, 'a')
b = Value(2, 'b')
c = a + b; c.label = 'c'
d = a * c; d.label = 'd'
print(a)
print(b)
print(c)
print(d)

