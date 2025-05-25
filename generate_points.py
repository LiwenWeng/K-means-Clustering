import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(random.randint(0, 100))

# Generate cluster 1 (100 points)
cluster1 = np.random.normal(loc=[2, 2], scale=0.5, size=(100, 2))

# Generate cluster 2 (100 points)
cluster2 = np.random.normal(loc=[6, 6], scale=0.7, size=(100, 2))

# Generate cluster 3 (100 points)
cluster3 = np.random.normal(loc=[2, 6], scale=0.4, size=(100, 2))

# Combine all clusters
data = np.vstack([cluster1, cluster2, cluster3])
np.savetxt("test.csv", data, delimiter=",")