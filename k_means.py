import matplotlib.pyplot as plt 
import math as m

class cluster:
	center = []
	prev_center = []
	points = []
	def __init__(self, center):
		self.center = center
	#check if the center of the cluster is where it should be
	def clean(self):
		self.points = []
	#check if cluster is where it should be
	def set(self):
		return self.center == self.prev_center
	#recompute the center of the cluster according to its points
	def recenter(self):
		if len(self.points) != 0:
			self.prev_center = self.center
			self.center = mean(self.points)

def distance(a, b):
	return m.sqrt((a[0] - b[0])**2+(a[1] - b[1])**2)

def mean(points):
	x = 0
	y = 0
	for p in points:
		x += p[0]
		y += p[1]
	return [x / len(points), y / len(points)]

def initial_cluster_centers(data, num):
	xmax = max(data, key = lambda p: p[0])[0]
	xmin = min(data, key = lambda p: p[0])[0]
	ymax = max(data, key = lambda p: p[1])[1]
	ymin = min(data, key = lambda p: p[1])[1]
	centers = []
	for i in range(num):
		centers.append([i*(xmax - xmin)/(num-1) + xmin, i*(ymax - ymin)/(num-1) + ymin])
	return centers

def create_clusters(centers):
	clusters = []
	for c in centers:
		clusters.append(cluster(c))
	return clusters

def assign_points(data, clusts):
	for p in data:
		min(clusts, key = lambda c: distance(c.center, p)).points.append(p)

def clean_clusters(clusts):
	for c in clusts:
		c.clean()

def recenter_clusters(clusts):
	for c in clusts:
		c.recenter()

def clustering_complete(clusts):
	for c in clusts:
		if not c.set():
			return False
	return True

def pack_clusters(clusts):
	clusters = []
	for c in clusts:
		clusters.append(c.points)
	return clusters

def clustering(data, numofclusters):
	#create the clusters and the centers
	clusters = create_clusters(initial_cluster_centers(data, numofclusters))

	while True:
		#clear the cluster points
		clean_clusters(clusters)

		#assign each point to the nearest cluster
		assign_points(data, clusters)

		#add all the x's and y's to find the centers of the clusters
		recenter_clusters(clusters)

		#check if done
		if clustering_complete(clusters):
			return pack_clusters(clusters)
