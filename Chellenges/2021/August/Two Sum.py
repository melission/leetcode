# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3836/

def twoSum(arr: list, target: int) -> list:
    length = len(arr)
    for i in range(length):
        print(i, arr[i:])
        for x in range(i+1, length):
            if arr[i]+arr[x] == target:
                ind = [i, x]
                return ind


def twoSumTwo(arr: list, target: int) -> list:
    guess = 0
    length = len(arr)
    for i in range(length):
        guess = target-arr[i]
        # print(i, guess)
        if guess in arr and arr.index(guess) != i:
            ind = [i, arr.index(guess)]
            return ind


def twoSumThree(arr: list, target: int) -> list:
    hash_map = {}

    for i, num in enumerate(arr):
        att = target - num
        if att not in hash_map:
            hash_map[num] = i
        else:
            return [hash_map[att], i]


if __name__ == '__main__':
    print(twoSumThree(
        arr= [3,2,4], target = 6
    ))