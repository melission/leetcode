# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3828/


def threeSumClosest(arr: list, target: int) -> int:
    arr.sort()
    nearest = 2**31-1

    for i in range(len(arr)-2):
        start = i+1
        end = len(arr)-1
        while start < end:
            cur_sum = arr[i]+arr[start]+arr[end]
            if abs(target - cur_sum) < abs(target-nearest):
                nearest = cur_sum

            if cur_sum > target:
                end -= 1
            else:
                start += 1
    return nearest


if __name__ == '__main__':
    print(threeSumClosest(
        arr= [-1,2,1,-4], target = 1
    ))