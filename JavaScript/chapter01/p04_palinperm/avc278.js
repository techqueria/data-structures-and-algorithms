// Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A
// palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
// The palindrome does not need to be limited to just dictionary words.

const assert = require("assert");

/**
 * Checks if the input string can be rearranged into a palindrome
 * @param  {string} str input string to check against
 * @return {boolean}    whether the input string can be rearranged into a palindrome
 *
 * We don't actually have to rearrange the string to solve this problem; we only need to check its contents.
 * If the string is of odd  length, then each character in the string has to appear an even number of times, except one.
 * If the string is of even length, then each character in the string has to appear an even number of times.
 * We can create a letter frequency map which takes O(N) time to loop through the string, and O(N) space to build.
 * Looping through the object key-value pairs again is an O(N) operation in the worst case where we loop through it all.
 *
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const palindromePerm = (str) => {
  const letterFreqs = {};
  let length = 0;
  for (const letter of str) {
    if (letter === " ") continue;

    letterFreqs[letter.toLowerCase()] =
      (letterFreqs[letter.toLowerCase()] || 0) + 1;
    length += 1;
  }

  let slack = length % 2 == 1;
  for (const letterFreq of Object.values(letterFreqs)) {
    if (letterFreq % 2 === 0) continue;

    if (!slack) return false;

    slack = !slack;
  }

  return true;
};

describe(module.filename, () => {
  it("should return true when the input string can be rearranged in the form of a palindrome.", () => {
    assert.ok(palindromePerm("Tact C o  a     "));
    assert.ok(palindromePerm("RaCeCaR"));
  });
  it("should return false when the input string cannot be rearranged in the form of a palindrome.", () => {
    assert.ok(!palindromePerm("techqueria"));
  });
});
