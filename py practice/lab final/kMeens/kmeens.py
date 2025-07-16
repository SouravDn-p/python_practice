import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

class KMeans:
    def __init__(self, points, clusters):
        self.num_points = points
        self.num_clusters = clusters
        self.mat = [[0 for _ in range(points)] for _ in range(points)]
        self.points = []
        self.centroids = []
        self.start()

    def start(self):
        # Step 1: Generate random points
        self.points = [Point(random.randint(0, self.num_points - 1), random.randint(0, self.num_points - 1)) for _ in range(self.num_points)]
        
        # Step 2: Initialize random centroids
        self.centroids = [Point(random.randint(0, self.num_points - 1), random.randint(0, self.num_points - 1)) for _ in range(self.num_clusters)]

        while True:
            # Step 3: Assign each point to the nearest centroid
            for i in range(self.num_points):
                min_dist = float('inf')
                for j in range(self.num_clusters):
                    d = math.sqrt((self.centroids[j].x - self.points[i].x) ** 2 + (self.centroids[j].y - self.points[i].y) ** 2)
                    if d < min_dist:
                        self.points[i].cluster = j
                        min_dist = d

            # Step 4: Store current centroids
            old_centroids = [Point(c.x, c.y) for c in self.centroids]

            # Step 5: Recalculate centroids
            for j in range(self.num_clusters):
                sum_x = sum_y = count = 0
                for p in self.points:
                    if p.cluster == j:
                        sum_x += p.x
                        sum_y += p.y
                        count += 1
                if count > 0:
                    self.centroids[j].x = sum_x // count
                    self.centroids[j].y = sum_y // count

            # Step 6: Check for convergence
            err = 0
            for i in range(self.num_clusters):
                err += abs(self.centroids[i].x - old_centroids[i].x)
                err += abs(self.centroids[i].y - old_centroids[i].y)

            if err == 0:
                break

        # Step 7: Display intra-cluster distances
        for i in range(self.num_clusters):
            intra_distance = sum(
                math.sqrt((self.centroids[i].x - p.x) ** 2 + (self.centroids[i].y - p.y) ** 2)
                for p in self.points if p.cluster == i
            )
            print(f"Cluster {i + 1} Intra-distance = {intra_distance:.2f}")

        # Step 8: Fill matrix with cluster values
        for p in self.points:
            self.mat[p.x][p.y] = p.cluster + 1

        # Step 9: Print points and their clusters
        for i in range(self.num_clusters):
            for p in self.points:
                if p.cluster == i:
                    print(f"Point ({p.x}, {p.y}) -> Cluster {p.cluster + 1}")

        # Step 10: Print final centroids
        for i, c in enumerate(self.centroids):
            print(f"Cluster {i + 1} Center: ({c.x}, {c.y})")

def main():
    points = int(input("Insert number of points: "))
    clusters = int(input("Insert number of clusters: "))
    KMeans(points, clusters)

if __name__ == "__main__":
    main()
