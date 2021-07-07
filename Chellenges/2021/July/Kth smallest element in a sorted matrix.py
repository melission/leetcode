# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3805/

def kthSmallest(matrix, k):
    flatten_list = []
    for list in matrix:
        for item in list:
            flatten_list.append(item)
    sorted_list = sorted(flatten_list)
    return sorted_list[k-1]


if __name__ == '__main__':
    print(kthSmallest(
        [[1,2],[1,3]], 2
               ))