from reverse_integer.solution import Solution

def test_case():
    sol = Solution()
    
    x = 123
    assert sol.reverse(x=x) == 321
    x = -123
    assert sol.reverse(x=x) == -321
    x = 120
    assert sol.reverse(x=x) == 21
    x = 9646324351
    assert sol.reverse(x=x) == 0
