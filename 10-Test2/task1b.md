Task Description
In a deck of cards, we have the following values:

A, K, Q, J, and T each have a value of 10.
2 through 9 have values equal to their number.
Special Rule: The cards A, K, and Q each have a special bonus of +5 added to their value if they are the last card in the string.
Your task is to write a program that calculates the total value of a string of cards, including the special bonus for A, K, and Q if they appear as the last card.

Example:
For input "AKQ", the total value should be 35 (A = 10 + 5, K = 10 + 5, Q = 10 + 5).
For input "KQJT", the total value should be 45 (K = 10 + 5, Q = 10 + 5, J = 10, T = 10).
For input "9532", the total value should be 19 (no special bonus, as there are no A, K, or Q at the end).
For input "A8Q", the total value should be 23 (A = 10 + 5, 8 = 8, Q = 10 + 5).