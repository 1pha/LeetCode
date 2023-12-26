class Solution:
    def reverse(self, x: int) -> int:
        if (x < - (2 ** 31)) or (x > (2 ** 31 - 1)):
            return 0
        x = str(x)
        if x.startswith("-"):
            x = x[1:][::-1]
            x = "-" + x
        else:
            x = x[::-1]
        x = int(x)
        if (x < - (2 ** 31)) or (x > (2 ** 31 - 1)):
            return 0
        return x
