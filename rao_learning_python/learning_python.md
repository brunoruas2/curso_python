# Learning Python by Nagesh Rao

<details>
<summary>
<font size=5> Cap 02 - Python Basics </font>
</summary>

<br />

Goals:
 - [x] Understand how statements make up a Python script
 - [x] Work with the basic data types of Python and operate upon them
 - [x] Understand how to use variables in Python and differentiate between references and objetcs
 - [x] Take input from the user and generate formated output

### 2.1 - Statements and Lines
> **statement** = A unit logical instruction to the interpreter

> **program** = A integral collection of statements

> **line** = sequence of chars ended by newline character

<br />

By default, python uses one line per statement, but with the `;` it's possible to separate more than one statement in a single line.

```python
print('ola') ; print('oi')

>>> ola
>>> oi
```


It's also possible make multiple line statements by using the operator `\`

```python
print('This \
is a \
multiple line \
statement')

>>> This is a multiple line statement
```
### 2.2 - Comments
<br />

### 2.3 - Basic Data Types
> Python does not require a variable to be declared as a specific type before use. All data is considered as objects (classes) which will be seen in most depth in chapter 12.

<br />

The objects in python can be on of theses specific types:
1. Integers (`int`)
1. Real numbers (`float`)
1. Comples numbers (`complex`)
1. Strings (`str`)
1. Boolean (`bool`)

More info in chapter 20. Here the author give A LOT of operations in every type above. 

### 2.4 - Identifiers (the name of things)
For variables names:
- alphabets, digits and underscores
- first digit not a number
- underscore in first digit has a special meaning (more on this later)
- cannot be the same of a keyword

Some good practices in creation of identifiers names ('first' means 'first word'):
- variables names: `first_second`
- class names: `FirstSecond`
- constant names: `FIRST_SECOND`
- rest: same of variables

### 2.5 - Keywords
Special words understood by Python.

Some Examples

|  |  |  |  |
|---------|---------|---------|---------|
|and     |else         | in        |   return      |
|as     |     except    |  is       |    True     |
|assert     | False        |  lambda        |  try       |
|break     |   finally      |  None       |  while       |
|class     |  for       |    nonlocal     |   with      |
|continue     | from        |   not      |   yield      |
|def     |  global       |   or      |         |
|del     |   if      |   pass      |         |
|elif     |   import      |  raise       |         |

### 2.6 - Variables
Some thing about variables:
1. created when and where required
1. the value can change over time
1. the type can change over time
1. it is possible find out what type is 'compatible' with it
1. the possible operations are type-dependent
1. values are objects and variables are references to these objects

### 2.7 - Basic input and output
Some `print()` interesting examples:

```python
'{p} is {a}, {p} is {b}'.format(\
p='Python',a='easy',b='fun')

>>> 'Python is easy, Python is fun'
```


|Combination  |Meaning  |
|---------|---------|
|{0}     |Display argument #0         |
|{age}     |Display argument named `age`         |
|{} |        Display next argument | 
|{0:d}     |Display argument #0 in decimal         |
|{age:d}    |Display argumento named `age` in decimal         |
|{:d}    |Display the next argument in decimal          |

</details>

---

<details open>
<summary>
<font size=5> Cap 03 - Python Control Structures </font>
</summary>

things to learn:
- [ ] Write Python scripts to solve problems and manage the flow of control through it
- [ ] Frame decision constructs to conditionally execute statements
- [ ] Frame loop constructs to repeat instructions as many times as required
- [ ] Learn how to terminate control from a loop, a function, a block and a script

### 3.1 - Getting Started with Programs
<br/>

### 3.2 - Decisions

#### `if` statement
```python
if condition: statement

# or

if condition:
    statement
    ...
```

### `if-else` statement
```python
if condition : statement1
else: statement2

# or

if condition:
  statement1
  ...
else: statement2

# or

if condition: statement1
else: 
  statement2

# or

if condition:
  statement1
else:
  statement2
```

### `if-elif-else` statement
```python
if condition1:
  statement1
  ...
elif condition2:
  statement2
  ...
elif condition3:
  statement3
  ...
...
else:
  statementn  
```

### Empty blocks and the pass keyword
```python
# positive logic approach
if condition_to_do_nothing == True:
  pass
else:
  statement1

# or

# negative logic approach
if condition_to_do_something != False:
  statement1
```

### Nested `if` statements
```python
if blabla == True:
  if bleble == True:
    statement1
  elif bloblo == True:
    statement2
  else:
    statement3
```

## Loops
### `while` loops
```python
while condition: statement

# or

while condition:
  statements
  ...
```

### Using a `break` in `while`
```python
while condition:
  if other_condition:
    break
  statement
```

### The `while` loop with `else` clause
```python
while condition:
  statement
  ...
else:
  statement
```

### The `for` loop + Using `range()` in it + `else`
```python
#syntax
range(end)
range(start,end)
range(start,end,step)

for var in range(0,10):
  statement
  ...
else:
  other_statement
```

### Nested loops
```python
for i in range(0,10,2):
  while i < 5:
    do_something
  else:
    do_other_something
    
```







</details>
