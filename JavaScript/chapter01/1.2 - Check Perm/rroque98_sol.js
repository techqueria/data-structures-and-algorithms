/*Given two strings, write a method to decide
if one is apermutation of the other permutation:*/

const isPermutation = (str1, str2) => {
  if (str1.length !== str2.length) {
    return false;
  }
  const freq1 = determineCharCount(str1);
  const freq2 = determineCharCount(str2);
  for (const [char, count] of freq1) {
    if (count !== freq2.get(char)) {
      return false;
    }
  }
  return true;
  //******** helper function ******
  function determineCharCount(string) {
    return string
      .split('')
      .reduce(
        (acc, char) => acc.set(char, (acc.get(char) || 0) + 1),
        new Map()
      );
  }
};

// Tests:
console.log(isPermutation('abc', 'abb') === false);
console.log(isPermutation('abb', 'abc') === false);
console.log(isPermutation('aaa', 'abc') === false);
console.log(isPermutation('abc', 'abcd') === false);
console.log(isPermutation('abc', 'bac') === true);
console.log(isPermutation('', '') === true);
console.log(isPermutation('12', '21') === true);
