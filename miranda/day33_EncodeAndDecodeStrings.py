class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, str):
        res = []
        pointer = 0

        while (pointer < len(str)):
            numPointer = pointer
            while str[numPointer] != "#":
                numPointer += 1

            strLen = int(str[pointer:numPointer])
            res.append(str[numPointer + 1 : numPointer + 1 + strLen])
            pointer = numPointer + 1 + strLen
        return res
    
strs = ["lint","code","love","you"]
solution = Solution()
encodedStr = solution.encode(strs)
print(encodedStr)
decodedStr = solution.decode(encodedStr)
print(decodedStr)
