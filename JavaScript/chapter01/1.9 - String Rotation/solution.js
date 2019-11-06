/* Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat") */

var StringRotate = function(string1, string2) {
    if (string1.length !== string2.length ){
        return false;
    }
    return ( string2 + string1 ).includes(string1); // one call of Substring
};

//Test
const assert = require('assert');

describe(module.filename, () => {
  it('should detect rotated substrings', () => {
    assert.equal(StringRotate('waterbottle', 'erbottlewat'), true);
  });
});
