# https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3813/

def customSortString(order: str, str: str) -> str:
    dict = {}

    for letter in str:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    # print(dict)
    customstr = ''

    for i in order:
        for _ in range(dict.get(i, 0)):
            customstr += i
        dict[i] = 0

    for i in range(26):
        for j in range(dict.get(chr(i+97), 0)):
            customstr += chr(i+97)
    return customstr

if __name__ == '__main__':
    print(customSortString(
    order="cba", str = "abcd"
    ))
