def minSetSize(arr):
    int_freq = {}
    min_lenght = len(arr)//2
    cur_lenght = 0
    min_size = 0
    for i in arr:
        if i in int_freq.keys():
            int_freq[i] += 1
        else:
            int_freq[i] = 1
    # print(int_freq, min_lenght)
    sortedDict = dict(sorted(int_freq.items(), key=lambda x: x[1], reverse=True))
    # print(sortedDict)
    for i in sortedDict.keys():
        # print(i)
        if cur_lenght < min_lenght:
            # print(cur_lenght, min_lenght)
            cur_lenght = cur_lenght + sortedDict[i]
            # print(f'current {cur_lenght} with i as {i} and the dict as {int_freq}')
            min_size += 1
    # print(f'min {min_size}')
    return min_size



if __name__ == '__main__':
    minSetSize(
        [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]
               )
