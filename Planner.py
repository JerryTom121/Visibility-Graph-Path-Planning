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


def VisibilityGraph(polygons):
	vertices = set([])
	edges = set([])

	for polygon in polygons:
		for vertex in polygon.points:
			vertices.add(vertex)

	for vertex in vertices:
		for other in VisibleVertices(vertex, polygons):
			edges.add(Edge(vertex, other))

	return (vertices, edges)


def VisibleVertices(point, polygons):
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
	return []

# We also need to account for edges not cutting accross the interior or shapes