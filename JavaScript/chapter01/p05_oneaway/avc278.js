// One Away: There are three types of edits that can be performed on strings: insert a character, remove a character,
// or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

const assert = require("assert");

/**
 * Check if the two strings are zero or one edits away
 * @param  {string}  A input string one to check against
 * @param  {string}  B input string two to check against
 * @return {boolean}   whether the input strings can be edited zero or one ways to be equal
 *
 * There are two cases here: (1) A.length === B.length, and (2) A.length !== B.length.
 * For the first case, all we need to do is iterate through the strings and ensure their elements are equal, allowing
 * room for one misplaced character. Iterating through this takes O(N) time, without any additional space.
 * For the second case, we iterate through the different length strings, and perform almost identical comparisons.
 * Again, we allow a single misplaced character, or lack of character as we iterate through them. This also takes O(N)
 * time. For the sake of keeping things DRY, we find out which string is the shorter one and instantiate a copy of it,
 * as well as a copy of the long string. For this reason, we take additional O(N) space. If we wanted, we could perform
 * two while loops (a < A.length + 1 && b < B.length) as well as (a < A.length && b < B.length + 1), so we don't take
 * any additional space.
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const oneAway = (A, B) => {
  if (Math.abs(A.length - B.lenght) > 1) return false;

  if (A.length === B.length) {
    let slack = true;
    for (let i = 0; i < A.length; i++) {
      if (A[i] === B[i]) continue;

      if (!slack) return false;
      slack = !slack;
    }
    return true;
  }

  const shortStr = A.length < B.length ? A : B;
  const longStr = A.length < B.length ? B : A;
  let sIdx = 0;
  let lIdx = 0;
  let slack = true;
  while (sIdx < shortStr.length + 1 && lIdx < longStr.length) {
    if (shortStr[sIdx] === longStr[lIdx]) {
      sIdx += 1;
      lIdx += 1;
    } else {
      if (!slack) return false;
      slack = !slack;
      lIdx += 1;
    }
  }
  return true;
};

describe(module.filename, () => {
  it("should return true when input strings are equal.", () => {
    assert.ok(oneAway("tech", "tech"));
  });
  it("should return true when input strings are of equal length, and replacing a character makes them equal.", () => {
    // replacing at the start of the string
    assert.ok(oneAway("sech", "tech"));
    assert.ok(oneAway("tech", "sech"));
    // replacing in the middle of the string
    assert.ok(oneAway("tdch", "tech"));
    assert.ok(oneAway("tech", "tdch"));
    // replacing at the end of the string
    assert.ok(oneAway("tecg", "tech"));
    assert.ok(oneAway("tech", "tecg"));
  });
  it("should return true when input strings lengths are one apart and inserting/deleting a character makes them equal.", () => {
    assert.ok(oneAway("tech", "stech"));
    assert.ok(oneAway("tech", "ech"));
  });
  it("should return false when the input string cannot be rearranged in the form of a palindrome.", () => {
    assert.ok(!oneAway("tech", "stack"));
    assert.ok(!oneAway("tech", "techqueria"));
  });
});
