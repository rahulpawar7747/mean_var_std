Mean-Variance-Standard Deviation Calculator

1)Overview:-
   This project we create a Python function `calculate()` that calculate basic statistical values (mean, variance, standard deviation,        maximum, minimum, and sum) for a 3x3 matrix.

2)Features:-
 -Takes a list of 9 numbers as input.
 -Converts the list into a 3x3 NumPy array.
 -Returns a dictionary with:
     -Mean
     -Variance
     -Standard Deviation
     -Maximum
     -Minimum
     -Sum

3)Error Handling:-
   If the input list does not contain exactly 9 elements, the function raises:

```python
ValueError: List must contain nine numbers.
```
4)Installation & Setup:-
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mean-var-std-calculator.git
   cd mean-var-std-calculator
   ```
2. Install dependencies:
   ```bash
   pip install numpy pytest
   ```
3. Run the program:
   ```bash
   python3 main.py
   ```
4. Run the tests:
   ```bash
   pytest
   ```
---

5)Example:-

```python
from mean_var_std import calculate

print(calculate([0,1,2,3,4,5,6,7,8]))
```

6)Output:-

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```
