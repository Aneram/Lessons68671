frutis = ["банан", "барбарис", "яблоко", "кавун", "памела"]

numbers = [2, 5, 7, 67, 89, 10, 32, 23, 11, 4, 6, 9, 70]

def startБ(frutis):
    return frutis.startswith('б')

def is_odd(x):
    if x % 2 == 0:
        return x

new_frutis = list(filter(startБ, frutis))
print(new_frutis)


new_numbers = list(filter(is_odd, numbers))
print(new_numbers)

#-----------------------------------------------------------------------------

#filter
#map
#lambda
fruits = ["banana", "apple", "watermelon", "barbaris", "pamelo", "brokoly"]

numbers = [2, 5, 7, 67, 89, 10, 32, 23, 11, 4, 6]

new_fruits = list(filter(lambda fruit: fruit.startswith("b"), fruits))
print(new_fruits)

new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
