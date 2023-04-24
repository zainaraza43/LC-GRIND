class Solution:
    def containsDuplicate(self, numbers: List[int]) -> bool:
        hashset = set()

        #Time complexity: O(|numbers|)
        #Memory complexity: O(|numbers|)

        return any(number in hashset or hashset.add(number) for number in numbers)