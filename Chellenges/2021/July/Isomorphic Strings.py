# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3811/

def isIsomorphic(s: str, t: str) -> bool:
    # t.length == s.length and len>1
    mapping_dict = {}
    mapped_set = ()
    length = len(s)

    for i in range(length):
        test_s = s[i]
        test_t = t[i]

        if test_s in mapping_dict:
            # print('inside')
            if mapping_dict[test_s] != test_t:
                return False
        else:
            if test_t in mapped_set:
                return False
            mapping_dict[test_s] = test_t
            mapped_set += tuple(test_t)
    # print(f'test_s {test_s}, mapping_dict {mapping_dict}, tuple {mapped_set}')
    return True


if __name__ == '__main__':
    print(isIsomorphic(
        s="badc", t="baba"
    ))
