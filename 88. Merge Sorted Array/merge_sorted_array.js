/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  for (let i = 0; i < m + n; i++) {
    if (nums1[i] == 0) {
      nums1[i] = nums2[i - m] || 0;
    }
  }

  nums1.sort((a, b) => a - b);
};
