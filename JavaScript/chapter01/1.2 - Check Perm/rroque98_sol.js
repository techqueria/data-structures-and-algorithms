/*Given two strings, write a method to decide
if one is apermutation of the other permutation:*/

const isPermutation = (str1, str2) =>{
  if (str1.length !== str2.length) {
    return false;
  }
  const obj1 = determineCharCount(str1);
  const obj2 = determineCharCount(str2);
  for (let char of str1) {
    if (obj1[char] !== obj2[char]) {
      return false;
    }
  }
  return true;
  //******** helper function ******
  function determineCharCount(string) {
    return string.split('').reduce((acc, char) => {
      if (acc[char] !== undefined) {
        acc[char]++;
      } else {
        acc[char] = 1;
      }
      return acc;
    }, {});
  }
}

// Tests:
  console.log(isPermutation('abc', 'abb') === false);
  console.log(isPermutation('abb', 'abc') === false);
  console.log(isPermutation('aaa', 'abc') === false);
  console.log(isPermutation('abc', 'abcd') === false);
  console.log(isPermutation('abc', 'bac') === true);
  console.log(isPermutation('', '') === true);
  console.log(isPermutation('12', '21') === true);
