from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        is_odd = intLength % 2
        check_index = intLength // 2
        if not is_odd:
            check_index -= 1
        offset = 10 ** check_index
        threshold = 10 ** (check_index + 1)
        answers = [str(offset + (q - 1)) if (offset + q - 1) < threshold else -1 for q in queries]
        if is_odd:
            answers = [int(a + a[:-1][::-1]) if a != -1 else a for a in answers]
        else:
            answers = [int(a + a[::-1]) if a != -1 else a for a in answers]
        return answers
