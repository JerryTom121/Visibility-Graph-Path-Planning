from Planner import Point
from Planner import Edge
from Planner import Polygon
from Planner import visibility_graph
from Planner import point_string
from Planner import edge_string


start = Point(0.0, 5.0)
goal = Point(15.0, 7.5)

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

point_1_b = Point(10.0, 5.0)
point_2_b = Point(12.5, 5.0)
point_3_b = Point(10.0, 10.0)
point_4_b = Point(12.5, 10.0)
point_list_b = [ point_1_b, point_2_b, point_3_b, point_4_b ]

edge_1_b = Edge(point_1_b, point_2_b)
edge_2_b = Edge(point_2_b, point_4_b)
edge_3_b = Edge(point_3_b, point_4_b)
edge_4_b = Edge(point_3_b, point_1_b)
edge_list_b = [ edge_1_b, edge_2_b, edge_3_b, edge_4_b ]

rect = Polygon(point_list, edge_list)
rect_b = Polygon(point_list_b, edge_list_b)

graph = visibility_graph([rect, rect_b], start, goal)

for vertex in graph[0]:
    print point_string(vertex)

for edge in graph[1]:
    print edge_string(edge)