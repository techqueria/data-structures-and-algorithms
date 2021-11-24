
// Is Unique: Implement an algorithm to determine if a string has all unique characters.
// What if you cannot used additional data structures?

const assert = require("assert");

/**
 * Checks if a string is composed of all unique characters
 * @param  {string} str input string to check
 * @return {bool}       Whether the input string contains unique characters
 *
 * We iterate through the input str of length N. Operations within this loop are O(1), so no additional time added.
 * We create an additional data structure, `set` where in the worst case is the same size as the input str, N.
 *
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
// with additional data structures
const isUnique1 = (str) => {
  const strSet = new Set();
  for (const s of str) {
    if (strSet.has(s)) return false;
    strSet.add(s);
  }
  return true;
};

/**
 * Checks if a string is composed of all unique characters
 * @param  {string} str input string to check
 * @return {bool}       Whether the input string contains unique characters
 *
 * We iterate through the input str of length N. Within that, we iterate through the rest of the str of length N-1.
 * Within the nested for loop, we only perform an O(1) operation. This leads to O(N^2) for the runtime complexity.
 * In this implementation, we do not create any additional data structures, so we use constant space.
 *
 * Runtime: O(N^2)
 * Space:   O(1)
 */
// without additional data structures
const isUnique2 = (str) => {
  for (let i = 0; i < str.length - 1; i++) {
    for (let j = i + 1; j < str.length; j++) {
      if (str[i] === str[j]) return false;
    }
  }
  return true;
};

describe(module.filename, () => {
  it("should return true on an input string with unique characters", () => {
    assert.equal(isUnique1("tech"), true);
    assert.equal(isUnique2("tech"), true);
  });
  it("should return false on an input string with non-unique characters", () => {
    assert.equal(isUnique1("techqueria"), false);
    assert.equal(isUnique2("techqueria"), false);
  });
});
