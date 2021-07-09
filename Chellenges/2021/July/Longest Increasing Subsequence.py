def lengthOfLIS(nums) -> int:
    """should be O(n**2)"""
    array_size = len(nums)
    li = [1]*array_size

    for i in range(1, array_size):
        for j in range(0, i):
            print(f' i {i}, j {j}; li {li}')
            if nums[i] > nums[j] and li[i] < li[j]+1:
                li[i] = li[j]+1
    return max(li)



if __name__ == '__main__':
    print(lengthOfLIS(
        [0,1,0,3,2,3]
    ))