### Definition:

Map ejecuta una funcion a cada item de una iteración.

### Syntax:
```
map(function, iterable, ...)
```
where:

* function - a function that perform some action to each element of an iterable
* iterable - an iterable like sets, lists, tuples, etc

### Example 1
```
def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
```
Output example 1
```
<map object at 0x7f7cb25c9040>
{16, 1, 4, 9}
```

### Example 2
```
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
```
Output example 2
```
<map object at 0x7fdb6a825040>
{16, 1, 4, 9}
```
### Example 3
```
num1 = [1, 2, 3]
num2 = [4, 5, 6]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))

```
Output example 3
```
[5, 7, 9]
```
