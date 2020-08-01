// URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient
// space at the end to hold the additional characters, and that you are given the "true" length of the string.

const assert = require("assert");

/**
 * URLifies an input string by replacing ' ' with '%20' and returning the modified string
 * @param  {string} str        input string to modify
 * @param  {int}    trueLength the "true" length of the str without trailing spaces
 * @return {string}            output URLified string
 *
 * Since we cannot mutate a string in javascript, we need to use an external data structure, like an array.
 * Creating a new data structure takes up O(N) space, where N is the length of the str.
 * We can loop through the array from the end of the true length to the start, while keeping count of two indexes.
 * If we encounter a space within the parameters of the word's true length, we can overwrite the element at that index
 * and the previous two indices with "%20", and decrement the index by 3, all of which are O(1) operations.
 * Alteranatively, we just overwrite the index of the str length counter with the index of the true length counter,
 * and decrement the index by 1, which is also just an O(1) operation.
 * When we're done traversing the array, we can simply return the joined array to return a string.
 *
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const urlify = (str, trueLength) => {
  const strArr = str.split("");
  let idx = str.length - 1;

  for (let i = trueLength - 1; i >= 0; i--) {
    if (strArr[i] === " ") {
        strArr[idx] = "0";
        strArr[idx - 1] = "2";
        strArr[idx - 2] = "%";
      idx -= 3;
    } else {
        strArr[idx] = strArr[i];
      idx -= 1;
    }
  }
  return strArr.join("");
};

describe(module.filename, () => {
  it("should return the modified string with %20 in place of spaces", () => {
    assert.equal(urlify("Mr John Smith    ", 13), "Mr%20John%20Smith");
  });
  it("should not modify a string with no spaces", () => {
    assert.equal(urlify("techqueria", 10), "techqueria");
  });
});
