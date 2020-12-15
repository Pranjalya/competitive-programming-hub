## Num Triplets

Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

- Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
- Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.


**Input** : nums1 = [7,4], nums2 = [5,2,8,9]

**Output** : 1

**Explanation** : Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8). 