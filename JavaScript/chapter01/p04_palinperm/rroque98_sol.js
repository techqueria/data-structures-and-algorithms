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

const assert = require('assert');

describe(module.filename, () => {
  it('should handle positive cases', () => {
    assert.equal(isPalindromePermutation('tact coa'), true);
    assert.equal(isPalindromePermutation('tact cooa'), true);
  });

  it('should handle negative cases', () => {
    assert.equal(isPalindromePermutation('tacr coa'), false);
    assert.equal(isPalindromePermutation('tactr coa'), false);
  });
});
