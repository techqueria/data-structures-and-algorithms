// Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

const assert = require("assert");
const { DH_CHECK_P_NOT_PRIME } = require("constants");

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
 * both aFreq and bFreq. If at any point, they do not match, we can return false.
 *
 * If we haven't returned false up to this point, it's safe to return true.
 *
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const checkPermutation1 = (A, B) => {
  if (A.length !== B.length) return false;
  const aFreq = {};
  const bFreq = {};
  for (const a of A) {
    aFreq[a] = (aFreq[a] || 0) + 1;
  }
  for (const b of B) {
    bFreq[b] = (bFreq[b] || 0) + 1;
  }

  const aKeys = Object.keys(aFreq);
  const bKeys = Object.keys(bFreq);
  if (aKeys.length !== bKeys.length) return false;
  for (let i = 0; i < aKeys.length; i++) {
    if (aFreq[aKeys[i]] !== bFreq[aKeys[i]]) return false;
  }

  return true;
};

/**
 * Checks if a string is a permutation of another
 * @param  {string} A source input string to check against
 * @param  {string} B target input string to compare with source string
 * @return {bool}     Whether the input strings are permutations of one another
 *
 * An alternative to this problem, and significantly more elegant, is to simply split the input strings into arrays,
 * use the built-in sort array method, then join back to a string, and check if A and B are equal.
 * The trade off is since we sort arrays of length N, the runtime becomes slower from O(N) to O(NlogN).
 * As for space, we create arrays of length N, so there is no change to space performance compared to checkPermutation1.
 * Even though this is less performant to checkPermutation1, for production code, this seems to be more maintainable
 * and way easier to read at a glance.
 *
 * Runtime: O(NlogN)
 * Space:   O(N)
 *
 */
const checkPermutation2 = (A, B) => {
  if (A.length !== B.length) return false;

  A = A.split("").sort().join("");
  B = B.split("").sort().join("");

  return A === B;
};

const checkPermutations = [checkPermutation1, checkPermutation2];
checkPermutations.forEach((checkPerm) => {
  describe(checkPerm.name, () => {
    it("should return false on input strings not of the same size", () => {
      const A = "hello";
      const B = "hi";
      assert.ok(!checkPerm(A, B));
    });
    it("should return false on input strings whose key lengths do not match", () => {
      const A = "abcd";
      const B = "abcc";
      assert.ok(!checkPerm(A, B));
    });
    it("should return false on input strings whose key frequencies do not match", () => {
      const A = "abccd";
      const B = "abcce";
      assert.ok(!checkPerm(A, B));
    });
    it("should return true on input strings whose letter frequencies match", () => {
      const A = "racecar";
      const B = "aaccerr";
      assert.ok(checkPerm(A, B));
    });
  })
})
