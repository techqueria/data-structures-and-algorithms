// Write a method to replace all spaces within a string with '%20'

const encodeSpaces = (string) => string.replace(/ /g, '%20');

// Tests:
const assert = require('assert');

describe(module.filename, () => {
  it('should replace spaces with %20', () => {
    assert.equal(encodeSpaces('Hello World'), 'Hello%20World');
    assert.equal(encodeSpaces(''), '');
    assert.equal(encodeSpaces('This is an example'), 'This%20is%20an%20example');
  });
});
