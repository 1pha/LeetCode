class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        substr_set = set()
        substr = s[0]
        for _s in s:
            substr_set.add(_s)
            if _s in substr:
                if len(substr) == 1:
                    substr = _s
                else:
                    idx = substr.index(_s) + 1
                    substr = substr[idx:] + _s
            else:
                substr = substr + _s
            substr_set.add(substr)
        answer = max(map(len, substr_set))
        return answer