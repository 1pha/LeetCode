from find_palindrome_with_fixed_length.solution import Solution

def test_case():
    sol = Solution()
    
    queries, intLength = [1 ,2, 3, 4, 5, 90], 3
    output = [101, 111, 121, 131, 141, 999]
    assert sol.kthPalindrome(queries=queries, intLength=intLength) == output
    queries, intLength = [2, 4, 6], 4
    output = [1111, 1331, 1551]
    assert sol.kthPalindrome(queries=queries, intLength=intLength) == output
