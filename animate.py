import sys
import os
import random
import json

from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import rcParams
from matplotlib import style

from utils import *

# matplotlib style
style.use('ggplot')

# global 
# DATA_SIZE = 64
TITLE = ['Insertion Sort', 'Selection Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort', 
         'Bucket Sort', 'Shell Sort', 'Heap Sort']
FUNCS = [insertion_sort, selection_sort, bubble_sort, merge_sort, quick_sort, bucket_sort, shell_sort, heap_sort]


def draw_chart(data, sort_algo):
    # plot configuration
    fig = plt.figure(1, figsize=(16, 9))
    axs = fig.add_subplot(111)
    axs.set_xticks([])
    axs.set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)
    
    # Sorting Algorithm
    frames = FUNCS[sort_algo](data)

    # Animation function, called sequentially
    # fi := framenumber
    def animate(fi):
        bars = []
        if(len(frames) > fi):
            axs.cla()
            axs.set_title(TITLE[sort_algo], fontsize=25)
            axs.set_xticks([])
            axs.set_yticks([])
            bars += axs.bar(list(range(len(data))),             # X
                            [d[0] for d in frames[fi]],         # data
                            1,                                  # width
                            color=[d[1] for d in frames[fi]],   # color
                            edgecolor = "none"                  # edge
                            ).get_children()
        return bars

    # Call animator
    anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=100)
    return plt, anim

fr = open("random_data.json")
data = json.load(fp=fr)

# sort_algo = 7
# plt, anim = draw_chart(data, sort_algo)
# plt.show()

for i in range(8):
    sort_algo = i
    plt, anim = draw_chart(data, sort_algo)
    # plt.show()
    anim.save('.\\output\\'+TITLE[sort_algo]+' - Random Data.mp4', writer=animation.FFMpegWriter(fps=25, extra_args=['-vcodec', 'libx264']))
