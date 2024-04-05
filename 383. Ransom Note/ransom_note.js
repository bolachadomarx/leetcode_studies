/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
// var canConstruct = function (ransomNote, magazine) {
//   let ransom_letters = ransomNote.split("")
//   let magazine_letters = magazine.split("")

//   let new_magazine_string = magazine;

//   let count = 0

//   for (let index = 0; index < ransom_letters.length; index++) {
//     if (magazine_letters.includes(ransom_letters[index])) {
//       new_magazine_string = new_magazine_string.replace(ransom_letters[index], "")
//       magazine_letters = new_magazine_string.split("")
//       count++
//     }
//   }

//   return count == ransom_letters.length;
// };

var canConstruct = function (ransomNote, magazine) {

  let ransom_letters = ransomNote.split("")

  return new Map([1, 2], [1, 2])
};

console.log(canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))