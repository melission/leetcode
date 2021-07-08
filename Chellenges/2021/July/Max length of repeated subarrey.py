# https://www.geeksforgeeks.org/longest-common-subarray-in-the-given-two-arrays/ first sol

def findLength(nums1, nums2) -> int:
    a1 = len(nums1)
    a2 = len(nums2)
    dp = [[0 for i in range(a1+1)] for i in range(a2+1)]
    for i in range(a1 -1, -1, -1):
        for j in range(a2 -1, -1, -1):

            if nums1[i] == nums2[j]:
                dp[j][i] = dp[j+1][i+1] + 1

    # for i in dp:
    #     for j in i:
    #         common_length = max(common_length, j)
    return max(max(row) for row in dp)


def findLength2(nums1, nums2) -> int:
    a1, a2 = len(nums1), len(nums2)
    dp = [[0] * (a1+1) for x in range(a2+1)]
    for i in range(a1 -1, -1, -1):
        for j in range(a2 -1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[j][i] = dp[j+1][i+1] + 1
    return max(max(row) for row in dp)


if __name__ == '__main__':
    print(findLength2(
        nums1=[1,2,3,2,1], nums2=[3,2,1,4]
    ))