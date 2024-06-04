# -*- coding: utf-8 -*-

 
import numpy as np
import open3d as o3d
import os


def dense_point(scan):
    scan11 = scan.voxel_down_sample(0.001)
    scan12 = scan.voxel_down_sample(0.001)
    for i in range(27):
        temp=scan11
        for j in range(3):
            shift=np.random.uniform(-0.05,0.05,size=1)
            temp.point["positions"][:,j] +=float(shift)
            print(i,j)
        scan12+=temp
    return scan12

if __name__ == '__main__': 
    path='merge_density/bae67a44/'
    if not os.path.exists(path+'merge.ply'):
        map2 = o3d.geometry.PointCloud()
        for file_path in os.listdir(path):

            print(file_path)
            if ".ply" in file_path:
                point_cloud = o3d.io.read_point_cloud(path+file_path)

            map2 += point_cloud

        map3 = map2.voxel_down_sample(0.04)    
        o3d.io.write_point_cloud(path+'merge.ply', map3)

    if True:

        scan = o3d.t.io.read_point_cloud(path+'merge.ply')
        scan12=dense_point(scan)
        scan2 = scan12.voxel_down_sample(0.15) 
        map = scan+scan2
        o3d.t.io.write_point_cloud(path+'merge.ply',map)
        print('ok')






