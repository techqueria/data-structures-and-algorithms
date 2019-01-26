// Given a string, write a function to check if it is a permutation of a palindrome

const isPalindromePermutation = (str) => {
  const strNoSpaces = str.replace(/ /g, '');
  var oddCount = 0;
  const frequencies = new Map();
  for (let char of strNoSpaces) {
    frequencies.set(char, 1 + (frequencies.get(char) || 0));
  }
  for (let frequency of frequencies.values()) {
    if (frequency % 2 === 0) {
     continue;
    }
    oddCount++;
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
