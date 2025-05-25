from src.geometry_io import extract_csv_file
from src.utils import find_centroid, find_closest_point, get_random_points
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy

coordinates = extract_csv_file("test.csv")
k = 3
k_points = get_random_points(coordinates, k)
clusters = [[] for _ in range(k)]
point_assignments = {}
history = []

changed = True
while changed:
    changed = False
    clusters = [[] for _ in range(k)]

    for point in coordinates:
        closer_point = find_closest_point(point, k_points)
        cluster_id = k_points.index(closer_point)

        if point not in point_assignments or point_assignments[point] != cluster_id:
            changed = True
            point_assignments[point] = cluster_id

        clusters[cluster_id].append(point)

    history.append((deepcopy(clusters), deepcopy(k_points)))

    for i in range(k):
        if clusters[i]:
            k_points[i] = find_centroid(clusters[i])

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    clusters, centroids = history[frame]

    for i, cluster in enumerate(clusters):
        if cluster:
            x, y = zip(*cluster)
            ax.scatter(x, y, c=colors[i % len(colors)], label=f'Cluster {i+1}')
    
    if centroids:
        cx, cy = zip(*centroids)
        ax.scatter(cx, cy, c='red', marker='X', s=200, label='Centroids')

    ax.set_title(f"K-Means Clustering - Step {frame + 1}")
    ax.set_xlabel("Latitude")
    ax.set_ylabel("Longitude")
    ax.grid(True)
    ax.legend()
    ax.axis('equal')

ani = animation.FuncAnimation(fig, update, frames=len(history), repeat=False, interval=1000)
plt.show()