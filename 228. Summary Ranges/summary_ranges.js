/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function (nums) {
  if (nums.length >= 0 && nums.length <= 20) {
    let result = [];
    let startRange = undefined;

    for (let index = 0; index < nums.length; index++) {
      const element = nums[index];

      if (startRange === undefined) {
        startRange = nums[index];
      }

      if (nums[index] + 1 != nums[index + 1]) {
        result.push([startRange, nums[index]])
        startRange = undefined
      }
    }

    return result.map((range) => {
      if (range[0] != range[1]) {
        return range.join("->")
      } else {
        return range[0].toString()
      }
    })
  }
};

console.log(summaryRanges([0, 1, 2, 4, 5, 7]))