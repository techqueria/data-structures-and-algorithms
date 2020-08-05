// String Rotation: Assume you have a method `isSubstring` which checks if one word is a substring of another. Given two
// strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to `isSubstring`.

const assert = require("assert");

/**
 * Checks if one string is a rotation of another string
 * @param  {string} s1 input string to check against
 * @param  {string} s2 input string to check if is a rotation of s1
 * @return {boolean}   whether s2 is a rotation of s1
 *
 * We can use the built-in method String.prototype.includes() to solve the problem for us,
 * checking if s1s1 of size 2N, where N is the length of s1, contains the string s2, also of size N at this point.
 *
 * Runtime: O(N)
 * Space:   O(1)
 *
 */
const isSubstring = (s1, s2) => {
  if (s1.length !== s2.length) return false;
  return `${s1}${s1}`.includes(s2);
};

describe(module.filename, () => {
  it("should return false when both input strings are not of the same length", () => {
    const s1 = "hi";
    const s2 = "hello";
    assert.ok(!isSubstring(s1, s2));
  });
  it("should return true when s2 is a valid rotation of s1", () => {
    const s1 = "waterbottle";
    const s2 = "erbottlewat";
    assert.ok(isSubstring(s1, s2));
  });
});
