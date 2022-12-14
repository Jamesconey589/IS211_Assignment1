def listDivide(numbers, divide=2):
    count = 0
    for number in numbers:
        if number % divide == 0:
            count += 1
    return count

class ListDivideException(Exception):
    pass

def testListDivide():
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException()

    if listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException()

    if listDivide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException()

    if listDivide([]) != 0:
        raise ListDivideException()

    if listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException()

testListDivide()