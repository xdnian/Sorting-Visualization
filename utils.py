import copy

# Insertion Sort
def insertion_sort(data):
    frames = [data]
    sd = copy.deepcopy(data)
    l = len(data)
    # for each element, find the correct location by comparing to the elements before
    for i in range(1, l):
        j = i
        while j > 0 and sd[j][0] < sd[j-1][0]:
            sd[j], sd[j-1] = sd[j-1], sd[j]
            # add frame
            frames.append(copy.deepcopy(sd))
            frames[-1][j-1][1] = 'r'
            j -= 1
    for _ in range(5):
        frames.append(sd)
    return frames

# Selection Sort
def selection_sort(data):
    frames = [data]
    sd = copy.deepcopy(data)
    l = len(data)
    # for every i < l-1 (1st to 2nd last)
    for i in range(l - 1):
        min_i = i
        # find the smallest one
        for j in range(i + 1, l):
            if sd[min_i][0] > sd[j][0]:
                min_i = j
            
        # put at the front of the current unsorted part
        if min_i != i:
            # add frame
            frames.append(copy.deepcopy(sd))
            frames[-1][i][1] = 'b'
            frames[-1][min_i][1] = 'r'
            
            sd[i], sd[min_i] = sd[min_i], sd[i]
    for _ in range(5):
        frames.append(sd)
    return frames

# Bubble sort
def bubble_sort(data):
    frames = [data]
    sd = copy.deepcopy(data)
    l = len(data)
    # for every i and j>1, compare and swap
    for i in range(l):
        for j in range(l - 1 - i):
            if sd[j][0] > sd[j + 1][0]:
                sd[j], sd[j + 1] = sd[j + 1], sd[j]
                # add frame
                frames.append(copy.deepcopy(sd))
                frames[-1][j+1][1] = 'r'
    for _ in range(5):
        frames.append(sd)
    return frames

# # Recursive Merge Sort
# def merge_sort_r(data):
#     l = len(data)
#     if l <= 1: return data
#     m = l // 2
#     left = merge_sort(data[:m])
#     right = merge_sort(data[m:])
    
#     # Merge two sorted list
#     def merge(left, right):
#         sorted_list = []
#         while left and right:
#             sorted_list += [left.pop(0)] if (left[0][0] < right[0][0]) else [right.pop(0)]
#         if left:
#             sorted_list += left
#         if right: 
#             sorted_list += right
#         return sorted_list
#     return merge(left, right)

# Merge Sort
def merge_sort(data):
    # inner function for merge sort
    def split_merge(sd, l, r, frames):
        m = (l + r) // 2
        # Split.
        if r - l > 2:
            split_merge(sd, l, m, frames)
            split_merge(sd, m, r, frames)
        msd = copy.deepcopy(sd)
        for i in range(l, m):
            msd[i][1] = 'tomato'
        for i in range(m, r):
            msd[i][1] = 'blueviolet'
        frames.append(copy.deepcopy(msd))

        # Merge.
        left = l
        right = m
        tmp_list = []
        for i in range(l, r):
            if right == r or (left < m and sd[left][0] <= sd[right][0]):
                tmp_list.append(sd[left])
                left += 1
            else:
                tmp_list.append(sd[right])
                right += 1
        for i in range(l, r):
            sd[i] = tmp_list[i-l]
        frames.append(copy.deepcopy(sd))
    
    frames = [data]
    sd = copy.deepcopy(data)

    split_merge(sd, 0, len(data), frames)
    for _ in range(5):
        frames.append(sd)
    return frames

# Quick Sort
def quick_sort(data):
    def qsort(sd, l, r, frames):
    # End when l==r
        if l < r:
            q = partition(sd, l, r, frames)
            qsort(sd, l, q - 1, frames)
            qsort(sd, q + 1, r, frames)
        return sd

    # partition
    def partition(sd, l, r, frames):
        psd = copy.deepcopy(sd)
        for k in range(l, r):
            psd[k][1] = 'y'
        psd[r][1] = 'k'
        frames.append(psd)

        pivot = sd[r][0]
        i = l - 1
        for j in range(l, r):
            if sd[j][0] <= pivot:
                i += 1
                if i != j:
                    frames.append(copy.deepcopy(psd))
                    frames[-1][i][1] = 'b'
                    frames[-1][j][1] = 'r'
                    sd[i], sd[j] = sd[j], sd[i]
                    psd[i], psd[j] = psd[j], psd[i]
        sd[i + 1], sd[r] = sd[r], sd[i+1]
        frames.append(copy.deepcopy(sd))
        frames[-1][i+1][1] = 'r'
        frames[-1][r][1] = 'b'
        return i + 1

    frames = [data]
    sd = copy.deepcopy(data)
    qsort(sd, 0, len(data)-1, frames)
    for _ in range(5):
        frames.append(sd)
    return frames

def bucket_sort(data):
    BUCKET_COUNT = 8
    COLORS = ['r','g','c','gold','hotpink','blueviolet','teal','coral']

    frames = [data]
    sd = copy.deepcopy(data)
    l = len(data)
    # Corner case
    if l == 0:
        return frames
    # Find max and min value
    min_value = min([d[0] for d in sd])
    max_value = max([d[0] for d in sd])
    # Initialize bucket
    buckets = []
    for i in range(0, BUCKET_COUNT):
        buckets.append([])
    # Calculate bucket length
    bucket_length = (max_value - min_value) // BUCKET_COUNT + 1
    # Assign value into bucket
    for i in range(0, l):
        k = (sd[i][0] - min_value) // bucket_length
        buckets[k].append(sd[i])
        sd[i][1] = COLORS[k]
        frames.append(copy.deepcopy(sd))

    result = []
    for b in buckets:
        result += b
    frames.append(copy.deepcopy(result))

    # Output
    j = 0
    for i in range(BUCKET_COUNT):
        k = j+len(buckets[i])
        result = result[:j] + sorted(result[j:k], key=lambda data: data[0]) + result[k:]
        # result = sorted(result[:k], key=lambda data: data[0]) + result[k:]
        frames.append(copy.deepcopy(result))
        j = k
    for d in result:
        for d2 in data:
            if d[0] == d2[0]:
                d[1] = d2[1]
    for _ in range(5):
        frames.append(result)
    return frames

def shell_sort(data):
    frames = [data]
    sd = copy.deepcopy(data)
    l = len(data)
    # Division of two pointers.
    div = l // 2
    while div >= 1:
        for i in range(div):
            ysd = copy.deepcopy(sd)
            for j in range(i, l, div):
                ysd[j][1]='y'
            for j in range(i+div, l, div):
                frames.append(copy.deepcopy(ysd))
                frames[-1][j][1]='r'
                for k in range(j, i, -div):
                    if sd[k][0] < sd[k-div][0]:      
                        sd[k], sd[k-div] = sd[k-div], sd[k]
                        ysd[k], ysd[k-div] = ysd[k-div], ysd[k]
                        frames.append(copy.deepcopy(ysd))
                        frames[-1][k-div][1]='r'
                    else:
                        break
        div = div // 2
    for _ in range(5):
        frames.append(sd)
    return frames


def heap_sort(data):
    COLORS = ['r','g','gold','hotpink','blueviolet']

    # adjust max heap
    def sift_down(sd, left, right, frames):
        # left child of left
        child = left * 2 + 1
        while child < right:
            # choose bigger child
            if child + 1 < right and sd[child][0] < sd[child+1][0]:
                child += 1
            csd = color(sd, right)
            frames.append(csd)
            csd[child][1]='k'
            csd[left][1]='r'
            
            # both 2 children < parent, break
            if sd[child][0] <= sd[left][0]:
                break
            sd[left], sd[child] = sd[child], sd[left]
            csd = copy.deepcopy(csd)
            frames.append(csd)
            csd[left], csd[child] = csd[child], csd[left]
            left = child
            child = child * 2 + 1

    def color(sd, n):
        csd = copy.deepcopy(sd)
        left = 0
        right = 1
        step = 0
        count = 1
        while left < n:
            for i in range(left, min(right, n)):
                csd[i][1]=COLORS[step % len(COLORS)]
            left = right
            count *= 2
            right += count
            step += 1
        return csd

    frames = [data]
    sd = copy.deepcopy(data)
    l = len(data)
    # create a max heap
    for left in range(l//2 - 1, -1, -1):
        sift_down(sd, left, l, frames)
    # heap sort
    for right in range(l - 1, 0, -1):
        # put max at end position
        sd[right], sd[0] = sd[0], sd[right]
        sift_down(sd, 0, right, frames)

    for _ in range(5):
        frames.append(sd)
    return frames


