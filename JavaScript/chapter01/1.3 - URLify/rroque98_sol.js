// Write a method to replace all spaces within a string with '%20'

const URLify = (string) => string.split(' ').join('%20');

// Tests:
console.log(URLify('Hello World') === 'Hello%20World');
console.log(URLify('') === '');
console.log(URLify('This is an example') === 'This%20is%20an%20example');
