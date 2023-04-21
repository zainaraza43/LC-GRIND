def containsDuplicate(self, nums: List[int]) -> bool:
    passed = set()
    for n in nums:
        if n in passed:
            return True
        passed.add(n)
    return False
