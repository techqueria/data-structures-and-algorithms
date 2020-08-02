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
 * Runtime: O()
 * Space:   O()
 *
 */
const compress = (str) => {
  let outputStr = "";
  let idx = 0;
  let next = 1;
  while (idx < str.length) {
    const currLetter = str[idx];
    let freq = 1;
    while (true) {
      if (currLetter === str[next]) {
        next += 1;
        freq += 1;
      } else {
        outputStr += `${currLetter}${freq}`;
        idx += freq;
        next = idx + 1;
        break;
      }
    }
  }
  return outputStr.length < str.length ? outputStr : str;
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
