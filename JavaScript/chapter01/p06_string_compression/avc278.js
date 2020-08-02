// String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
// For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than
// the original string, your method should return the origin string. You can assume the string has only uppercase and
// lowercase letters (a-z).

const assert = require("assert");

/**
 * Returns the compressed version of the string if applicable
 * @param  {string}  str input string to compress
 * @return {string}      either the compressed string, or the string
 *
 * Storing the outputStrArr is at worst size 2N for an input string whose size is N (still O(N) additional space).
 * Storing and updating the pointers `idx`, `next`, and `freq` take O(1) additional space and O(1) time.
 * As we iterate through the str in the outer while loop, in one extreme, assuming no repeating letters in a sequence,
 * idx increments by 1 each iteration, and so it's O(N) runtime. On the other extreme, assuming all repeating letters,
 * this would be O(N) on the outer loop, and O(N) in the inner while loop. The trick to knowing this is still O(N)
 * and not O(N^2) is the fact that we don't visit any one index pointer more than once in our two while loops.
 * Both loops are still just part of the same loop, which results in O(N).
 *
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const compress = (str) => {
  let outputStrArr = [];
  let idx = 0;

  while (idx < str.length) {
    const currLetter = str[idx];
    let freq = 1;

    let next = idx + 1;
    while (next < str.length && currLetter === str[next]) {
      next += 1;
      freq += 1;
    }

    outputStrArr.push(currLetter);
    outputStrArr.push(freq);
    idx = next;
  }

  return outputStrArr.length < str.length ? outputStrArr.join("") : str;
};

describe(module.filename, () => {
  it("should compress a string with repeated characters.", () => {
    assert.ok(compress("aabcccccaaa", "a2b1c5a3"));
    assert.ok(compress("aaaaaaaaaaa", "a11"));
  });
  it("should not compress a string whose str length is less than the compressed version.", () => {
    assert.equal(compress("tech"), "tech");
    assert.equal(compress("abcdefg"), "abcdefg");
    assert.equal(compress(""), "");
  });
});
