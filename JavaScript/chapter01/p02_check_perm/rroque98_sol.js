/*Given two strings, write a method to decide
if one is apermutation of the other permutation:*/

const isPermutation = (str1, str2) => {
  if (str1.length !== str2.length) {
    return false;
  }
  const freq1 = determineCharCount(str1);
  const freq2 = determineCharCount(str2);
  for (const [char, count] of freq1) {
    if (count !== freq2.get(char)) {
      return false;
    }
  }
  return true;
  //******** helper function ******
  function determineCharCount(string) {
    return string
      .split('')
      .reduce(
        (acc, char) => acc.set(char, (acc.get(char) || 0) + 1),
        new Map()
      );
  }
};

// Tests:
const assert = require('assert');

describe(module.filename, () => {
  it('should handle positive cases', () => {
    assert.equal(isPermutation('abc', 'bac'), true);
    assert.equal(isPermutation('', ''), true);
    assert.equal(isPermutation('12', '21'), true);
  });

  it('should handle negative cases', () => {
    assert.equal(isPermutation('abc', 'abb'), false);
    assert.equal(isPermutation('abb', 'abc'), false);
    assert.equal(isPermutation('aaa', 'abc'), false);
    assert.equal(isPermutation('abc', 'abcd'), false);
  });
});
