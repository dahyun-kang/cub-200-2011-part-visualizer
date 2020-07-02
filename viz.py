'''
CUB-200-2011 part location visualizer

plot one image:             viz.py --img_path /home/dahyun/dataset/CUB_200_2011/images/012.Yellow_headed_Blackbird/Yellow_Headed_Blackbird_0059_8079.jpg
plot all image {randomly/in order}:    viz.py --plot_order {randomly, in_order}
'''


import os
import argparse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

plt.rcParams["figure.figsize"] = (14, 14)
plt.rcParams["font.size"] = 16

parser = argparse.ArgumentParser()
parser.add_argument("--img_path", default=None, help="image path to visualize", type=str)
parser.add_argument("--dataset_path", default='CUB_200_2011', help="directory of the original CUB dataset you download and extract", type=str)
parser.add_argument("--plot_order", help="plotting order", default='randomly', choices=['randomly', 'in_order'])

args = parser.parse_args()
origin_path = os.path.join(os.getcwd(), args.dataset_path)
image_folder_prefix = 'images'

part_label_dict = ['back', 'beak', 'belly', 'breast', 'crown', 'forehead', 'left eye', 'left leg', 'left wing', 'nape', 'right eye', 'right leg', 'right wing', 'tail', 'throat']
id2path = {}
path2id = {}
with open(os.path.join(origin_path, 'images.txt')) as f:
    lines = f.readlines()
    for line in lines:
        index, path = line.strip().split()
        index = int(index)
        id2path[index] = path
        id2path[path] = index

id2part = {}
with open(os.path.join(origin_path, 'parts', 'part_locs.txt')) as f:
    lines = f.readlines()
    for line in lines:
        index, part_id, x, y, visible = line.strip().split()
        index = int(index)
        x = float(x)
        y = float(y)
        visible = int(visible)
        if index not in id2part:
            id2part[index] = []
        id2part[index].append([x, y, visible])


def img_path_abs(rel_path):
    return os.path.join(origin_path, image_folder_prefix, rel_path)


def plot_one(img_path):
    id = id2path[img_path]
    part_locs = id2part[id]
    print(id)
    print(img_path)
    print(part_locs)
    print('---------------------------------------------------------------------------------------\n')
    abs_path = img_path_abs(img_path)
    p = Image.open(abs_path)

    plt.title(img_path.split(os.path.sep)[-1])
    plt.imshow(p)
    colors_dict = ['b', 'g', 'r', 'c', 'm',
                   'y', 'w', 'tab:orange', 'tab:purple', 'tab:brown',
                   'tab:pink', 'tab:gray', 'lime', 'aqua', 'fuchsia']
    for i, (x, y, visible) in enumerate(part_locs):
        if visible:
            label = '{} (o)'.format(part_label_dict[i])
            plt.scatter(x, y, marker='o', label=label, s=200, edgecolors='black', c=colors_dict[i])
        else:
            label = '{} (x)'.format(part_label_dict[i])
            plt.scatter(None, None, label=label, edgecolors='black', visible=False)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.show()


def plot_all(plot_order):
    if plot_order == 'randomly':
        plot_idx_list = np.random.permutation(range(1, 11789)).tolist()
    elif plot_order == 'in_order':
        plot_idx_list = list(range(1, 11789))
    else:
        assert 'wrong option'

    for plot_idx in plot_idx_list:
        img_path = id2path[plot_idx]
        plot_one(img_path)


if args.img_path is not None:
    path_seperated = args.img_path.split(os.path.sep)
    img_path = os.path.join(path_seperated[-2], path_seperated[-1])
    plot_one(img_path)
else:
    plot_all(plot_order=args.plot_order)

