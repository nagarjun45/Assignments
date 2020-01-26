def square_list():
    squareList = map(lambda n: n*n ,range(1,21))
    return list(squareList)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
print(square_list())