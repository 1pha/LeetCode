from longest_substring_without_repeating_characters.solution import Solution

def test_case():
    sol = Solution()
    
    s = "abcabcbb"
    assert sol.lengthOfLongestSubstring(s=s) == 3
    s = "bbbbb"
    assert sol.lengthOfLongestSubstring(s=s) == 1
    s = "pwwkew"
    assert sol.lengthOfLongestSubstring(s=s) == 3
    s = "dvdf"
    assert sol.lengthOfLongestSubstring(s=s) == 3