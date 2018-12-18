/* Implement a method to perform basic string 
compression using the counts of repeated characters
Ex: 'aabcccccaaa' would become a2b1c5a3
*/

const stringCompression = (str) => {
  if (!str.length) {
    return '';
  }
  var compStr = '';
  var count = 1;
  var currentChar = str[0];
  for (let i = 1; i < str.length; i++) {
    let char = str[i];
    if (char === currentChar) {
      count++;
      if (i === str.length - 1) {
        compStr += `${currentChar}${count}`;
      }
    } else {
      compStr += `${currentChar}${count}`;
      currentChar = char;
      count = 1;
    }
  }
  return compStr;
}

// TESTS
console.log(stringCompression('aabcccccaaa') === 'a2b1c5a3');
console.log(stringCompression('cccccccc') === 'c8');
console.log(stringCompression('') === '');
console.log(stringCompression('AabccCccaaa') === 'A1a1b1c2C1c2a3');
