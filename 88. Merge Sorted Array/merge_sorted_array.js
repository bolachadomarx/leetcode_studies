/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  const lenght = m + n

  for (let i = 0; i < lenght; i++) {
    if (nums1[i] == 0 && m == n) {
      nums1[i] = nums2[i - n]
    } else if (nums1[i] == 0 && m > n) {
      nums1[i] = nums2[i - (m + n - 1)];
    } else if (nums1[i] == 0 && m < n && m != 0) {
      nums1[i] = nums2[i - 1];
    } else if (nums1[i] == 0) {
      nums1[i] = nums2[i];
    }
  }


  return nums1.sort();
};


// num1 [4,0,0,0,0,0] m = 1
// num2 [1,2,3,5,6] n = 5

// [2, 3, 4, 5, 6, undefined];