# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3805/
import numpy as np
from timeit import default_timer as timer

def kthSmallest(matrix, k):
    start1st = timer()
    flatten_list = []
    for list in matrix:
        for item in list:
            flatten_list.append(item)
    sorted_list = sorted(flatten_list)
    end1st = timer()
    return f'{sorted_list[k - 1]} with {end1st-start1st}'


def kthSmallestNumpy(matrix, k):
    start2nd = timer()
    matrix = np.array(matrix)
    flatted_list = sorted(matrix.flatten().tolist())
    end2nd = timer()
    return f'{flatted_list[k - 1]} with {end2nd-start2nd}'


if __name__ == '__main__':
    print(kthSmallest(
        [[1,5,9],[10,11,13],[12,13,15]], k = 8
               ), kthSmallestNumpy(
        [[1,5,9],[10,11,13],[12,13,15]], k = 8
    ))