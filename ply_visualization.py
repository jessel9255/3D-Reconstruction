import open3d as o3d
import numpy as np

# Load the point cloud
pcd = o3d.io.read_point_cloud("aaaaaaaaa.ply")
print("Total number of points:", len(pcd.points))

# Convert point cloud to numpy array for analysis
points = np.asarray(pcd.points)

# Check the distribution of the z-values
z_values = points[:, 2]
z_1 = np.percentile(z_values, 1)
z_99 = np.percentile(z_values, 99)
print("1st percentile of z:", z_1)
print("99th percentile of z:", z_99)

# Create a mask to filter out extreme outliers in the z-axis
mask = (z_values >= z_1) & (z_values <= z_99)
filtered_points = points[mask]
print("Number of filtered points (1st to 99th percentile):", len(filtered_points))

# Create a new point cloud with the filtered points
pcd_filtered = o3d.geometry.PointCloud()
pcd_filtered.points = o3d.utility.Vector3dVector(filtered_points)

# Visualize the filtered point cloud
vis = o3d.visualization.Visualizer()
vis.create_window(window_name="Filtered Point Cloud", width=800, height=600)
vis.add_geometry(pcd_filtered)

# Adjust render options (increase point size if needed)
render_option = vis.get_render_option()
render_option.point_size = 3.0

vis.run()
vis.destroy_window()

output_file = "filtered_aaaaaaaaa.ply"
o3d.io.write_point_cloud(output_file, pcd_filtered)
print("Filtered point cloud saved to", output_file)
