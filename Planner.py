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
	# 	Add edges to E that are counterclockwise from point
	# Return W

	# Set of all points that could potentially be reached
	points = set([])
	for polygon in polygons:
		for vertex in polygon.points:
			points.add(vertex)
	points.add(start)
	points.add(end)
	points.remove(point)
	points = list(points)

	# Sorts points by angle from x-axis with point as origin
	points.sort(key = lambda p: angle(point, p))

	# Finds all edges in polygons
	all_edges = set([])
	for polygon in polygons:
		for edge in polegon.edges:
			all_edges.add(edge)

	# Initializes edge set and adds edges to first point
	# Edges with first point will be removed, no need to account
	open_edges = []
	for edge in all_edges
		if edge_intersect(point, points[0], edge):
			open_edges.add(edge)
	open_edges.sort(key = lambda e: edge_distance(point, points[0], e))


	# Points list for visible vertices
	visible = []

	# Checks each point for visibility
	for next_point in points:
		# OPTIMIZE: Track edges for a given point
		# Would save looking through all edges
		for edge in all_edges:
			if edge.contains(next_point):
				open_edges.remove(edge)
		if euclidean_distance(point, next_point) <= edge_distance(point, next_point, open_edges[0]):
			visible.add(next_point)
		for edge in all_edges:
			if edge.contains(next_point):
				if counterclockwise(point, edge, next_point):
					open_edges.append(edge)
			open_edges.sort(key = lambda e: edge_distance(point, next_point, e))

	return visible


# Computes euclidian distance
def euclidean_distance(point1, point2):
	return math.sqrt(math.pow(point1.x - point2.x, 2) + math.pow(point1.y - point2.y, 2))


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
# Currently does not handle if an endpoint is on the line
def edge_intersect(point1, point2, edge):
	slope = (point1.y - point2.y) / (point1.x - point2.x)

	y1_ex = slope * (edge.points[0].x - point1.x) + point1.y
	y2_ex = slope * (edge.points[1].x - point1.x) + point1.y

	if y1_ex == edge.points[0].y or y2_ex == edge.points[1].y:
		return False

	y1_below = (y1_ex > edge.points[0].y)
	y2_below = (y2_ex > edge.points[1].y)

	return not (y1_below == y2_below)


# Returns the distance from a point to an edge along the line to another point
# If the intersect is not within the edge, won't return a valid distance. So don't do that.
def edge_distance(point, other_point, edge):
	edge_slope = (edge.points[0].y - edge.points[1].y) / (edge.points[0].x - edge.points[1].x)
	points_slope = (point.y - other_point.y) / (point.x - other_point.x)

	intersect_x = (edge_slope * edge.points[0].x - points_slope * point.x + point.y - edge.points[0].y) / (edge_slope - points_slope)
	intersect_y = edge_slope * (intersect_x - edge.points[0].x) + edge.points[0].y

	intersect = Point(intersect_x, intersect_y)

	return euclidean_distance(intersect, point)


# Returns true if the edge goes counterclockwise from the linethrough point and endpoint
# Only use if endpoint is an endpoint in edge
def counterclockwise(point, edge, endpoint):
	if edge.points[0] == endpoint:
		angle_diff = angle(point, edge.points[1]) - angle(point, endpoint)
	else:
		angle_diff = angle(point, edge.points[0]) - angle(point, endpoint)

	if angle_diff < 0:
		angle_diff += 2 * math.pi

	return angle_diff < math.pi


# TODO: We also need to account for edges not cutting accross the interior of shapes