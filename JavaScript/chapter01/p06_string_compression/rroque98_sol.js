/* Implement a method to perform basic string
compression using the counts of repeated characters.
If the compressed string length is more than original
string length, return original string.
Ex: 'aabcccccaaa' would become a2b1c5a3
*/

const stringCompression = (str) => {
  if (!str.length) {
    return '';
  }
  let compStr = '';
  let count = 0;
  let currentChar = str[0];
  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    if (char === currentChar) {
      count++;
    } else {
      compStr += `${currentChar}${count}`;
      currentChar = char;
      count = 1;
    }
  }
  compStr += `${currentChar}${count}`;
  if (compStr.length > str.length) {
    return str;
  }
  return compStr;
}

const assert = require('assert');

describe(module.filename, () => {
  it('should correctly compress longer strings', () => {
    assert.equal(stringCompression('aabcccccaaa'), 'a2b1c5a3');
    assert.equal(stringCompression('cccccccc'), 'c8');
  });

  it('should leave uncompressible strings unmodified', () => {
    assert.equal(stringCompression(''), '');
    // Explanation: 'A1a1b1c2C1c2a3' length is longer than original string so returns original string
    assert.equal(stringCompression('AabccCccaaa'), 'AabccCccaaa');
    assert.equal(stringCompression('x'), 'x');
  });
});
