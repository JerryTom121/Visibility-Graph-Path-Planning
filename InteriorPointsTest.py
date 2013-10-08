from Planner import Point
from Planner import Edge
from Planner import Polygon
from Planner import find_interior_points
from Planner import point_string

p1 = Point(0.0, 0.0)
p2 = Point(0.0, 1.0)
p3 = Point(1.0, 1.0)
p4 = Point(1.0, 0.0)
p5 = Point(0.5, 0.5)
ps = set([p1, p2, p3, p4, p5])

e1 = Edge(p1, p2)
e2 = Edge(p2, p3)
e3 = Edge(p3, p4)
e4 = Edge(p4, p5)
e5 = Edge(p5, p1)
es = set([e1, e2, e3, e4, e5])

poly = Polygon(ps, es)

i1 = Point(0.2, 0.5)
i2 = Point(0.4, 0.5)
i3 = Point(1.5, 0.5)
i4 = Point(0.5, 0.3)
i5 = Point(0.5, 0.7)
ins = set([i1, i2, i3, i4, i5])

for point in find_interior_points([ins], [poly]):
	print point_string(point)
print

p1 = Point(0.0, 0.0)
p2 = Point(0.0, 1.0)
p3 = Point(1.0, 1.0)
p4 = Point(1.0, 0.0)
p5 = Point(0.6, 0.5)
p6 = Point(0.4, 0.5)
ps = set([p1, p2, p3, p4, p5, p6])

e1 = Edge(p1, p2)
e2 = Edge(p2, p3)
e3 = Edge(p3, p4)
e4 = Edge(p4, p5)
e5 = Edge(p5, p6)
e6 = Edge(p6, p1)
es = set([e1, e2, e3, e4, e5, e6])

poly = Polygon(ps, es)

i1 = Point(0.2, 0.5)
i2 = Point(0.7, 0.5)
i3 = Point(1.5, 0.5)
i4 = Point(0.5, 0.3)
i5 = Point(0.5, 0.7)
i6 = Point(-0.1, 1.0)
ins = set([i1, i2, i3, i4, i5, i6])

for point in find_interior_points([ins], [poly]):
	print point_string(point)