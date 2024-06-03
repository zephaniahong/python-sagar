# Day 1

## Running Python Code

1. Repl (Read, Evaluate, Print, Loop)

## Operators:

- +, -, \*, /, %, \*\*, //

## Declaring Variables

```py
pi = 3.14
radius = 5
area = pi * radius ** 2
```

## Mental Model for Varialbes

## Expressions vs Statements

- Expressions give values whereas statements do not

```py
x = 5 # statement
5 # expression
5 * 5 # expression
```

## **_QUIZ_**

```py
x = 5
y = x + 3
x = 8
# What is y?
```

## Data Types

### Strings

s = "hello"
c = "h"

### Integers

i = 5

### Floats

j = 5.0

## Functions

- Encapsulate reusable code together
- Two step process
  1. Declare
  2. Call

### Declaration

- Declaration: f(x) = x + 3
- Declaration: g(y) = y \* 2

### Calling

- Calling: f(1) = 4
- Calling: f(5) = 8
- Calling: g(2) = 4
- Calling: g(3) = 6

### Example

```py
def f(x):
    return x + 3

chicken = f(1) # chicken = 4
```

## **_QUIZ_**

- Create a function that takes in a radius and returns the area of a circle

### Taking Multiple Arguments

```py
def sum_of_two_numbers(x, y):
    return x + y
```
