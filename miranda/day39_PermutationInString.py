class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        str1Count, str2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            str1Count[ord(s1[i]) - ord('a')] += 1
            str2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
           matches += (1 if str1Count[i] == str2Count[i] else 0)

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[right]) - ord('a')
            str2Count[index] += 1

            if str1Count[index] == str2Count[index]:
                matches += 1
            elif str1Count[index] + 1 == str2Count[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            str2Count[index] -= 1
            if str1Count[index] == str2Count[index]:
                matches += 1
            elif str1Count[index] - 1 == str2Count[index]:
                matches -= 1
            left += 1
        return matches == 26
    
str1 = "ab"
str2 = "eidbaooo"
solution = Solution()
print(solution.checkInclusion(str1, str2))