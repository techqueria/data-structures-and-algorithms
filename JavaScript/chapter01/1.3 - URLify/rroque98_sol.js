// Write a method to replace all spaces within a string with '%20'

const encodeSpaces = (string) => string.replace(/ /g, '%20');

// Tests:
console.log(encodeSpaces('Hello World') === 'Hello%20World');
console.log(encodeSpaces('') === '');
console.log(encodeSpaces('This is an example') === 'This%20is%20an%20example');
