# 0x02. Calculus


## Files 1-8 and 11-16

Answers to general calculus questions.

## 9-sum_total.py

Calculates the sum of **_i to the power of 2 from i equals 1 to n_**.


## 10-matisse.py

Calculates the derivate of a polynomial:

- Recieves a list of coefficients representing a polynomial.
  - the index of the list represents the power of **x** that the coefficient belongs to.
  - Example: if **_f(x) = x^3 + 3x +5_**, the list is equal to **[5, 3, 0, 1]**.
- Returns 0 when the list is not valid.
- If the derivative is **0**, returns **[0]**.
- Returns a new list of coefficients representing the derivative of the polynomial.


## 17-integrate.py

Calculates the integral of a polynomial:

- Receives a list of coefficients representing a polynomial.
  - The index of the list represents the power of **x** that the coefficient belongs to.
  - Example: if **_f(x) = x^3 + 3x +5_**, the list is equal to **[5, 3, 0, 1]**.
- Receives an integer representing the integration constant.
- If a coefficient is a whole number, it should be represented as an integer.
- If poly or C are not valid, return None.
- Return a new list of coefficients representing the integral of the polynomial.
- The returned list should be as small as possible.

