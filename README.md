# Understanding Python's `range()` Function

## Overview
This Python script demonstrates various ways to use the `range()` function. It covers range creation with different step values, comparisons, accessing range attributes, and iterating over ranges using loops.

## Features
- Demonstrates basic `range(start, stop, step)` usage.
- Uses `range()` in loops to iterate over sequences.
- Compares two range objects.
- Checks for membership using `in` and `not in`.
- Utilizes `len()`, `min()`, and `max()` with ranges.
- Accesses individual elements using `.count()`, `.index()`, and slicing.

## File Structure
- `main.py`: Contains the implementation demonstrating Python `range()` functionality.
- `README.md`: Documentation for the project.

## How to Run
### Prerequisites
- Python 3.x installed on your system.

### Steps to Execute
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the script using:
   ```bash
   python main.py
   ```

## Key Code Snippets
### Creating and Printing Ranges
```python
print(list(range(0, 5, 1)))  # [0, 1, 2, 3, 4]
print(list(range(2, 13, 2)))  # [2, 4, 6, 8, 10, 12]
```

### Looping with `range()`
```python
for i in range(10):
    print(i)
```

### Checking Membership in a Range
```python
if 1 in range(0, 4):
    print("1 is in the range")
```

### Using Range Attributes
```python
my_range = range(2, 10, 2)
print("Start:", my_range.start)
print("Stop:", my_range.stop)
print("Step:", my_range.step)
```

## Example Output
```
[0, 1, 2, 3, 4]
[2, 4, 6, 8, 10, 12]
range 1: [0, 6]
range 2: [0, 6]
range 1 = range 2
1 is in the range
10 in not in the range
len: 4
min: 0
max: 3
```

## Author
This script serves as an educational tool to understand Python's `range()` function.

## License
This project is open-source and available for use under the MIT License.
