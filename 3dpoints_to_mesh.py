import open3d as o3d
import numpy as np


pcd = o3d.io.read_point_cloud("filtered_aaaaaaaaa.ply")
print("Total number of points:", len(pcd.points))

o3d.visualization.draw_geometries([pcd])

# Estimate normals for the point cloud
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.5, max_nn=30))

# Set an alpha parameter; experiment with different values to get the desired detail
alpha = 0.35  

# Create a mesh using the alpha shape algorithm
mesh_alpha = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)
mesh_alpha.compute_vertex_normals()
print("Alpha shape mesh has", len(mesh_alpha.triangles), "triangles.")

# Visualize the alpha shape reconstructed mesh
o3d.visualization.draw_geometries([mesh_alpha])

# Optionally, save the alpha shape mesh
o3d.io.write_triangle_mesh("filtered_aaaaaaaaa_mesh.stl", mesh_alpha)
print("Mesh saved to filtered_aaaaaaaaa_mesh.stl")
