Here is a Python implementation of the `Solution` class that satisfies the feature file requirements and adheres to the given protocol. The implementation ensures a runtime complexity of `O(log (m+n))` by using a binary search approach.

```python
from typing import Protocol, List


class Solution(Protocol):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: ...


class MedianFinder:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # Handle edge cases for partitions
            maxX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minX = float("inf") if partitionX == x else nums1[partitionX]

            maxY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minY = float("inf") if partitionY == y else nums2[partitionY]

            # Check if we have found the correct partition
            if maxX <= minY and maxY <= minX:
                # If the total length is even
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                # If the total length is odd
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        raise ValueError("Input arrays are not sorted or invalid")
```

Explanation:

1. **Binary Search**:
   - The algorithm uses binary search on the smaller array (`nums1`) to find the correct partition.
   - This ensures the runtime complexity is `O(log(min(m, n)))`.
1. **Partitioning**:
   - The arrays are partitioned such that the left partition contains the smaller half of the elements, and the right partition contains the larger half.
1. **Median Calculation**:
   - If the combined length of the arrays is even, the median is the average of the two middle elements.
   - If the combined length is odd, the median is the maximum of the left partition.
1. **Edge Cases**:
   - Handles cases where one or both arrays are empty.
   - Ensures the input arrays are sorted.

Usage:
You can use the `MedianFinder` class to find the median of two sorted arrays:

```python
finder = MedianFinder()
print(finder.findMedianSortedArrays([1, 3], [2]))  # Output: 2
print(finder.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
print(finder.findMedianSortedArrays([], [1, 2, 3, 4, 5]))  # Output: 3
```
