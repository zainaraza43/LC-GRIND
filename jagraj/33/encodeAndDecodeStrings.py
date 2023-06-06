from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs) -> str:
        if len(strs) <= 1:
            return "" if not strs else f"{strs[0]}"
        r = ""
        for s in strs[:-1]:
            r += s + "8==D"
        return r + strs[-1]
        

    """
    @param: s: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s) -> List[str]:
        if len(s) == 0:
            return []

        words = [""]

        i = 0
        while i < len(s):
            if s[i:i+4] == "8==D":
                words.append("")
                i+=3
            else:
                words[-1] += s[i]
            i += 1

        return words


if __name__ == '__main__':
    s = Solution()

    print(s.encode(["lint","code","love","you"]))
    print(s.decode(s.encode(["lint","code","love","you"])))

    print(s.encode(["we", "say", ":", "yes"]))
    print(s.decode(s.encode(["we", "say", ":", "yes"])))
