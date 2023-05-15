class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        
        digits[-1] += 1

        carry = 0

        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry

            if digits[i] > 9:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
                break

        if carry == 1:
            digits.insert(0, 1)
            
        return digits