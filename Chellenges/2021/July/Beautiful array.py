def isBeautiful(num: int) -> list:
    if num == 1:
        return [1]
    if num == 2:
        return [2, 1]
    even = [x*2 for x in isBeautiful(num//2)]
    odd = [x*2-1 for x in isBeautiful(num//2 + num%2)]
    print(even, odd)
    return odd+even


if __name__ == '__main__':
    print(isBeautiful(
        4
    ))
