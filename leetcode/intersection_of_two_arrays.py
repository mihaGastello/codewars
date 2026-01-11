# https://leetcode.com/problems/intersection-of-two-arrays/
from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    for num in set(nums1):
        if num in nums2:
            result.append(num)
    return result


def intersection2(nums1: List[int], nums2: List[int]) -> List[int]:
    return [ num for num in set(nums1) if num in nums2]


print(intersection([1, 2, 3, 7, 9, 15], [15, 2, 8, 0, 3]))
print(intersection2([1, 2, 3, 7, 9, 15], [15, 2, 8, 0, 3]))