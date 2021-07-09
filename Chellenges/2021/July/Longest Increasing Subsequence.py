# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3808/
def lengthOfLIS(nums) -> int:
    """should be O(n**2)"""
    array_size = len(nums)
    li = [1]*array_size

    for i in range(1, array_size):
        for j in range(0, i):
            print(f"nums[i] {nums[i]}, nums[j] {nums[j]};\n "
                  f"li[i] {li[i]}, li[j] {li[j]}, and li[j]+1 {li[j]+1}\n "
                  f"full nums list {nums}, li list {li}\n")
            if nums[i] > nums[j] and li[i] < li[j]+1:
                li[i] = li[j]+1
    return max(li)


if __name__ == '__main__':
    print(lengthOfLIS(
        [7,7,7,7,7,7,7]
    ))