# -*- coding: utf-8 -*-

 
import json
import os
import  pdb

import shutil
from glob import glob

def mymovefile(srcfile,dstpath):                      
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)           
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       
        shutil.copyfile(srcfile, dstpath + fname)       
        print ("move %s -> %s"%(srcfile, dstpath + fname))

path='11953248/transforms.json'

path2='11953248/'

with open(path, 'r') as f:
    data_original = json.load(f)

num=100

camera_groups = [data_original['frames'][i:i+num] for i in range(0, len(data_original['frames']), num)]


if len(camera_groups[-1]) < num/2:
    #pdb.set_trace()
    camera_groups[-2]+=camera_groups[-1]

    camera_groups.remove(camera_groups[-1])
split_files = path2+'split_files'


if not os.path.exists(split_files):
    os.mkdir(path2)
    os.mkdir(split_files)


for i, group in enumerate(camera_groups):
    data = {}
    data["camera_model"] ="OPENCV"
    data["camera_angle_x"] =data_original['camera_angle_x']
    data["camera_angle_y"] =data_original['camera_angle_y']
    data["fl_x"] =data_original['fl_x']
    data["fl_y"] =data_original['fl_y']
    data["k1"] =data_original['k1']
    data["k2"] =data_original['k2']
    data["p1"] =data_original['p1']
    data["p2"] =data_original['p2']
    data["cx"] =data_original['cx']
    data["cy"] =data_original['cy']
    data["w"] =data_original['w']
    data["h"] =data_original['h']

    data["aabb_scale"] ="16"



    data["frames"] = group



    file_name = split_files + f'/transforms{i+1}.json'

    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
        #json.dump({'frames': group}, f, indent=4)
 
    src_dir = path[:-16]
    dst_dir = path2+"images_undistorted/"                                 

    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    src_file_list = glob(src_dir + '/images_undistorted/*')                    
    for srcfile in src_file_list:
        mymovefile(srcfile, dst_dir)                     










