# 412 - Fizz Buzz

[leetcode](https://leetcode.com/problems/fizz-buzz/)

## Problem

    Write a program that outputs the string representation of numbers from 1 to n.
    
    But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
    
    Example:
    
    n = 15,
    
    Return:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]

## Solution

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n+1):

            if not i % 3 and not i % 5:
                ans.append("FizzBuzz")
            elif not i % 5:
                ans.append("Buzz")
            elif not i % 3:
                ans.append("Fizz")
            else:
                ans.append(str(i))

        return ans
```
