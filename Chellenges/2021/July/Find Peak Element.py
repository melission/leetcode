# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3812/
def findPeakElement(nums) -> int:
    start = 0
    end = len(nums)-1

    def peakElement(nums, start, end):
        mid = (start+end) // 2
        if ((mid == 0 or nums[mid-1] <= nums[mid]) and
                (mid == len(nums)-1 or nums[mid+1] <= nums[mid])):
            return mid
        if mid-1 >= 0 and nums[mid-1] > nums[mid]:
            return peakElement(nums, start, mid-1)
        return peakElement(nums, mid+1, end)

    return peakElement(nums, start, end)


def recursivePeakElement(nums):
    start = 0
    end = len(nums)-1
    while start < end:
        mid = (start+end)//2
        if nums[mid] > nums[mid+1]:
            end = mid
        else:
            start = mid+1
    return start


if __name__ == '__main__':
    print(recursivePeakElement(
        [8, 9, 10, 2, 5, 6]
    ))