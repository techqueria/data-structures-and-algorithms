/* There are 3 types of edits that can be made on a string:
insert character, remove character, replace a character
Given 2 strings write a function that will check if it is
1 or 0 edits away*/

const isOneAway = (str1, str2) => {
  const diffInLen = Math.abs(str1.length - str2.length);
  if (diffInLen > 1) {
    return false;
  }

  let errorCount = 0;
  if (str1.length === str2.length) {
    for (let i = 0; i < str1.length; i++) {
      if (str1[i] !== str2[i]) {
        errorCount++;
        if (errorCount > 1) {
          return false;
        }
      }
    }
    return true;
  }
  const longStr = str1.length > str2.length ? str1 : str2;
  const shortStr = str1.length <= str2.length ? str1 : str2;
  for (let i = 0; i + errorCount < longStr.length; i++) {
    if (longStr[i + errorCount] === shortStr[i]) {
      continue;
    }
    errorCount++;
    if (errorCount > 1) {
      return false;
    }
  }
  return true;
};

const assert = require('assert');

function runTests(cases, expected) {
  for (const [str1, str2] of cases) {
    assert.equal(isOneAway(str1, str2), expected);
    assert.equal(isOneAway(str2, str1), expected);
  }
}

describe(module.filename, () => {
  it('should handle positive cases', () => {
    runTests(
      [
        ['pale', 'ple'], // deletion
        ['pale', 'opale'], // insertion in beginning
        ['pale', 'palse'], // insertion in middle
        ['pale', 'pales'], // insertion at end
        ['pale', 'bale'], // replacement
        ['p', 'b'],
        ['p', 'p'],
        ['p', ''],
        ['', '']
      ],
      true
    );
  });

  it('should handle negative cases', () => {
    runTests(
      [
        ['pale', 'ae'], // greater than 1 deletions
        ['pale', 'ppalpe'], // greater than 1 insertions
        ['pale', 'bake'], // greater than 1 replacements
        ['pale', 'balpe'], // 1 insertion, 1 replacement
        ['pale', 'plo'], // 1 deletion, 1 replacement
        ['pale', 'ales'] // 1 deletion, 1 insertion
      ],
      false
    );
  });
});
