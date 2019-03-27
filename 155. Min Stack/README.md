# 155. Min Stack

How to design a stack with getMin in constant time?

Notes:

Keep two stacks s1, s2.

1. s1 for all values
2. s2 for current min values, pop out the min value, if it pops out in s1.
3. There could be multiple same min values in s2. Don't forget.

