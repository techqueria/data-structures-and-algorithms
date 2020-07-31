// Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

const assert = require("assert");

/**
 * Checks if a string is a permutation of another
 * @param  {string} A source input string to check against
 * @param  {string} B target input string to compare with source string
 * @return {bool}     Whether the input strings are permutations of one another
 *
 * Throughout the problem, we set up a couple ways to early exit. At the start, if both strings are not of the same
 * length, we already know they cannot be permutations of each other, so we return false.
 * Otherwise, we can continue and set up a mapping between the elements in A and B, and their frequencies.
 * This is an O(N) operation with respect to time and space where N is the length of the string A.
 * At this point, we can get the keys from the frequency objects we created, which is an O(N) operation for space.
 * If the lengths of `aKeys` and `bKeys` are not the same, we know they cannot be permutations and we exit early.
 * Otherwise, we can continue to iterate through the keys. We need to make sure that the frequencies of aKeys exist in
 * both aFreq and bFreq AND that the frequencies of bKeys exist in aFreq and bFreq. It is not enough to check that one
 * exists in both and not check the other set of keys. If at any point, they do not match, we can return false.
 *
 * If we haven't returned false up to this point, it's safe to return true.
 *
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const checkPermutation = (A, B) => {
  if (A.length !== B.length) return false;
  const aFreq = {};
  const bFreq = {};
  for (let i = 0; i < A.length; i++) {
    aFreq[A[i]] = aFreq[A[i]] || 0;
    aFreq[A[i]] += 1;

    bFreq[B[i]] = bFreq[B[i]] || 0;
    bFreq[B[i]] += 1;
  }

  const aKeys = Object.keys(aFreq);
  const bKeys = Object.keys(bFreq);
  if (aKeys.length !== bKeys.length) return false;
  for (let i = 0; i < aKeys.length; i++) {
    if (aFreq[aKeys[i]] !== bFreq[aKeys[i]]) return false;
    if (aFreq[bKeys[i]] !== bFreq[bKeys[i]]) return false;
  }

  return true;
};

describe(module.filename, () => {
  it("should return false on input strings not of the same size", () => {
    const A = "hello";
    const B = "hi";
    assert.equal(checkPermutation(A, B), false);
  });
  it("should return false on input strings whose key lengths do not match", () => {
    const A = "abcd";
    const B = "abcc";
    assert.equal(checkPermutation(A, B), false);
  });
  it("should return false on input strings whose key frequencies do not match", () => {
    const A = "abccd";
    const B = "abcce";
    assert.equal(checkPermutation(A, B), false);
  });
  it("should return true on input strings whose letter frequencies match", () => {
    const A = "racecar";
    const B = "aaccerr";
    assert.equal(checkPermutation(A, B), true);
  });
});
