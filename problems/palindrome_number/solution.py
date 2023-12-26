from math import log10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        def count_digits(num):
            if num == 0:
                return 1
            num_digits = int(log10(abs(num))) + 1
            return num_digits

        def get_digit(num, pos):
            digit = (abs(num) // 10**pos) % 10
            return digit
        
        num_digits = count_digits(x)
        for i in range(num_digits // 2):
            first, last = get_digit(x, i), get_digit(x, num_digits - 1 - i)
            if first != last:
                return False
        return True
