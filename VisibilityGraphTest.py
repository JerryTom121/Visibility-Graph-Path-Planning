from Planner import Point
from Planner import Edge
from Planner import Polygon
from Planner import visibility_graph
from Planner import point_string
from Planner import edge_string


start = Point(0.0, 5.0)
goal = Point(10.0, 5.0)

point_1 = Point(2.5, 2.5)
point_2 = Point(2.5, 7.5)
point_3 = Point(7.5, 7.5)
point_4 = Point(7.5, 2.5)
point_list = [ point_1, point_2, point_3, point_4 ]

edge_1 = Edge(point_1, point_2)
edge_2 = Edge(point_2, point_3)
edge_3 = Edge(point_3, point_4)
edge_4 = Edge(point_4, point_1)
edge_list = [ edge_1, edge_2, edge_3, edge_4 ]

rect = Polygon(point_list, edge_list)

graph = visibility_graph([rect], start, goal)

for vertex in graph[0]:
	print point_string(vertex)

for edge in graph[1]:
	print edge_string(edge)