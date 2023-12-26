from palindrome_number.solution import Solution

def test_case():
    sol = Solution()
    
    x = 121
    assert sol.isPalindrome(x=x) == True
    x = -121
    assert sol.isPalindrome(x=x) == False
    x = 10
    assert sol.isPalindrome(x=x) == False
