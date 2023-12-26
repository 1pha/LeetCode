# [Reverse-Integer](https://leetcode.com/problems/reverse-integer/)

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

```
Example 1:

Input: x = 123
Output: 321
``` 

```
Example 2:

Input: x = -123
Output: -321
```

```
Example 3:

Input: x = 120
Output: 21
```
 

```
Constraints:
-231 <= x <= 231 - 1
```

### Solution

32/64-bit integers 조건이 있어서 어떻게하지 하고 대충 2 ** 31로 부등호 때렸는데 마음에 들지 않음. 다른 사람 솔루션도 찾아봤는데 크게 다르지 않아서 타협.