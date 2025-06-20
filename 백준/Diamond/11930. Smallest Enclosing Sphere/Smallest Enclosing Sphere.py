import sys; input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split(' '))) for _ in range(n)]

# Temporary center point for a sphere
mean_x = sum(x for x, y, z in points) / n
mean_y = sum(y for x, y, z in points) / n
mean_z = sum(z for x, y, z in points) / n

# Hyper-parameters
EPOCH = 2500
ALPHA = 0.1
DECAY = 0.99

radius = 0 # Answer: Smallest radius of a sphere that contains all points
for _ in range(EPOCH): # Iterate to find the optimal center point
    radius = -1 # Init radius for this epoch
    idx = -1 # Index of the point that is farthest from the center
    for i, (x, y, z) in enumerate(points):
        dist = (x - mean_x) ** 2 + (y - mean_y) ** 2 + (z - mean_z) ** 2

        # Update if larger than the current radius
        if (radius < dist):
            radius = dist
            idx = i
    
    # Update the center point towards the farthest point
    mean_x += (points[idx][0] - mean_x) * ALPHA
    mean_y += (points[idx][1] - mean_y) * ALPHA
    mean_z += (points[idx][2] - mean_z) * ALPHA
    ALPHA *= DECAY # Decay the learning rate

print(f"{radius ** 0.5:.2f}")