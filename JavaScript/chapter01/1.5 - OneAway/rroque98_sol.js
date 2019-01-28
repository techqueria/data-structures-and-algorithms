/* There are 3 types of edits that can be made on a string:
insert character, remove character, replace a character
Given 2 strings write a function that will check if it is
1 or 0 edits away*/

const isOneAway = (str1, str2) => {
  if (str1.length === str2.length) {
    let errorCount = 0;
    for (let i = 0; i < str1.length; i++) {
      if (str1[i] === str2[i]) {
        continue;
      }
      errorCount++;
      if (errorCount > 1) {
        return false;
      }
    }
  } else {
    let errorCount = 0;
    const longestStr = findLongestStr(str1, str2);
    let x = 0;
    for(let i = 0; i < longestStr.length; i++) {
      let currentChar1 = str1[i];
      let currentChar2 = str2[x]
      let nextChar1 = str1[i + 1];
      let nextChar2 = str2[x + 1];
      if (str1[i] === str2[x]) {
        x++;
        continue;
      }
      errorCount++;
      if (errorCount > 1) {
        return false;
      }
      if (currentChar1 === nextChar2) {
        x++;
        i--;
        continue;
      } else if (currentChar2 === nextChar1) {
        continue;
      }
      errorCount++;
      return false;
    }
    // ***** Helper functions ********
    function findLongestStr(str1, str2) {
      return (str1.length > str2.length ? str1 : str2);
    }
  }
  return true;
}

// TESTS
console.log(isOneAway('pale', 'ple') === true);
console.log(isOneAway('pales', 'pale') === true);
console.log(isOneAway('pale', 'bale') === true);
console.log(isOneAway('pale', 'bake') === false);
console.log(isOneAway('paleo', 'palseo') === true);
console.log(isOneAway('p', 'b') === true);
console.log(isOneAway('', '') === true);
console.log(isOneAway('p', 'p') === true);
console.log(isOneAway('pale', 'ppalpe') === false);

console.log(isOneAway('ple', 'pale') === true);
console.log(isOneAway('pale', 'pales') === true);
console.log(isOneAway('bale', 'pale') === true);
console.log(isOneAway('bake', 'pale') === false);
console.log(isOneAway('palseo', 'paleo') === true);
