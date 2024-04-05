/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  if (s.length >= 1 && s.length <= 2 * (Math.pow(10, 5))) {
    const string_normal = s.toLowerCase().replace(/[^a-z0-9]/g, "");
    const string_ao_contrario = string_normal.split("").reverse().join("");

    return string_normal === string_ao_contrario;
  }

};

console.log(isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))