from pyfunc2.function.arrayElementsAreIncluded import arrayElementsAreIncluded

# Przykład 1: elementy są zawarte
result1 = arrayElementsAreIncluded([1, 2], [1, 2, 3])
print(f"Czy [1, 2] jest podzbiorem [1, 2, 3]? {result1}")

# Przykład 2: elementy nie są zawarte
result2 = arrayElementsAreIncluded([1, 4], [1, 2, 3])
print(f"Czy [1, 4] jest podzbiorem [1, 2, 3]? {result2}")
