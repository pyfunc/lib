from pyfunc2.function.differenceElementsInArrays import differenceElementsInArrays

# Przykład 1: podstawowa różnica
result1 = differenceElementsInArrays([1, 2, 3], [2, 3, 4])
print(f"Różnica między [1, 2, 3] i [2, 3, 4]: {result1}")

# Przykład 2: brak różnicy
result2 = differenceElementsInArrays([1, 2], [1, 2])
print(f"Różnica między [1, 2] i [1, 2]: {result2}")
