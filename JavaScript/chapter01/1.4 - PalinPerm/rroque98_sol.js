// Given a string, write a function to check if it is a permutation of a palindrome

const isPalindromePermutation = (str) => {
  const strNoSpaces = str.split(' ').join('');
  const obj = {};
  var oddCount = 0;
  for (let char of strNoSpaces) {
    if (obj[char] !== undefined) {
      obj[char]++;
    } else {
      obj[char] = 1;
    }
  }
  for (let key in obj) {
    if (obj[key] % 2) {
      oddCount++;
    }
    if (oddCount > 1) {
      return false;
    }
  }
  return true;
}

console.log(isPalindromePermutation('tact coa') === true);
console.log(isPalindromePermutation('tact cooa') === true);
console.log(isPalindromePermutation('tacr coa') === false);
console.log(isPalindromePermutation('tactr coa') === false);
