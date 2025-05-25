from src.geometry_io import extract_csv_file
from src.utils import find_centroid, find_closest_point, get_random_points

coordinates = extract_csv_file("test.csv")
k = 3
k_points = get_random_points(coordinates, k)
clusters = [[] for _ in range(k)]
point_assignments = {}

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

    for i in range(k):
        if clusters[i]:
            k_points[i] = find_centroid(clusters[i])

for i, cluster in enumerate(clusters):
    print(f"Cluster {i}: {cluster}")