import math

class Edge:
	def __init__(self, point1, point2):
		self.points = (point1, point2)

	def contains(self, point):
		for p in self.points:
			if point == p:
				return True
		return False

	def __eq__(e):
		return set(self.points) == set(e.points)


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, p):
		return self.x == p.x and self.y == p.y


class Polygon:
	def __init__(self, points, edges):
		self.points = points
		self.edges = edges


# Returns a list of vertices and edges forming a visibility graph
def visibility_graph(polygons, start, goal):
	vertices = set([])
	edges = set([])

	for polygon in polygons:
		for vertex in polygon.points:
			vertices.add(vertex)

	vertices.add(start)
	vertices.add(goal)

	for vertex in vertices:
		for other in visible_vertices(vertex, polygons, start, goal):
			edges.add(Edge(vertex, other))

	return (vertices, edges)


# Returns a list of edges from point to other visible points
def visible_vertices(point, polygons, start, goal):
	# Compute angles for each point in polygons
	# Sort points by angle from x-axis, closer points first in ties
	# Create edge list E
	# Create point list W
	# Start with first point, add all intersected edges to E
	# For each point in order:
	# 	If point is on the nearest edge:
	# 		Add point to W
	# 	Remove edges from E that are clockwise from point
	# 		(These are equivalent to edges that touch point and are in E)
	# 	Add edges to E that are counterclockwise from point
	# 		(These are equivalent to edges that touch point and are not in E)
	# Return W

	points = set([])
	for polygon in polygons:
		for vertex in polygon.points:
			points.add(vertex)
	points.add(start)
	points.add(end)
	points.remove(point)
	points = list(points)
	points.sort(key = lambda p: angle(point, p))

	edges = set([])

	return []


# Computes the angle from the x-axis to point in radians [0, 2*pi) with center as the origin
def angle(center, point):
	dx = point.x - center.x
	dy = point.y - center.y

	if dx == 0:
		if dy < 0:
			return math.pi * 3 / 2
		else:
			return math.pi / 2

	if dy == 0:
		if dx < 0:
			return math.pi
		else:
			return 0

	if dx < 0:
		return math.pi + math.atan(dy / dx)

	if dy < 0:
		return 2 * math.pi + math.atan(dy / dx)

	return math.atan(dy / dx)


# Returns true if edge is intersected by the line passing through the given points
def edge_intersect(point1, point2, edge):
	slope = (point1.y - point2.y) / (point1.x - point2.x)

	y1_ex = slope * (edge.points[0].x - point1.x) + point1.y
	y2_ex = slope * (edge.points[1].x - point1.x) + point1.y

	if y1_ex == edge.points[0].y or y2_ex == edge.points[1].y:
		return False

	y1_below = (y1_ex > edge.points[0].y)
	y2_below = (y2_ex > edge.points[1].y)

	return not (y1_below == y2_below)


# We also need to account for edges not cutting accross the interior of shapes