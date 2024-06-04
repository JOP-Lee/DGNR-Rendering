import open3d as o3d
import numpy as np
import os
import pdb
import json

ply_file="/point_cloud"
checkpoint="/11953248-block900"
root_path="outputs/11953248/nerfacto" +checkpoint


point_cloud = o3d.io.read_point_cloud(root_path+ ply_file+".ply")


with open(os.path.join(root_path, 'dataparser_transforms.json'), 'r') as f:
    transform = json.load(f)


transform_matrix= transform['transform']
transform_matrix.append([0,0,0,1])

blender2opencv = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])

scale=transform['scale']
point_cloud.scale(1 / scale, center=(0,0,0))
point_cloud = point_cloud.transform(np.linalg.inv(transform_matrix))
o3d.io.write_point_cloud(root_path+ ply_file+ "_scale.ply", point_cloud)