# https://www.geeksforgeeks.org/longest-common-subarray-in-the-given-two-arrays/ first sol

def findLength(nums1, nums2) -> int:
    common_length = 0
    a1 = len(nums1)
    a2 = len(nums2)

    dp = [[0 for i in range(a1+1)] for i in range(a2+1)]
    for i in range(a1 -1, -1, -1):
        for j in range(a2 -1, -1, -1):

            if nums1[i] == nums2[j]:
                dp[j][i] = dp[j+1][i+1] + 1

    for i in dp:
        for j in i:
            common_length = max(common_length, j)
    return common_length


if __name__ == '__main__':
    print(findLength(
        nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]
    ))