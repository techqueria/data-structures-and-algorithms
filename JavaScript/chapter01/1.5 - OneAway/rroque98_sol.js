/* There are 3 types of edits that can be made on a string:
insert character, remove character, replace a character
Given 2 strings write a function that will check if it is
1 or 0 edits away*/

const isOneAway = (str1, str2) => {
  if (str1.length === str2.length) {
    let errorCount = 0;
    for (let i = 0; i < str1.length; i++) {
      if (str1[i] !== str2[i]) {
        errorCount++;
      }
      if (errorCount > 1) {
        return false;
      }
    }
  } else {
    let errorCount = 0;
    const longestStr = findLongestStr(str1, str2);
    let x = 0;
    for(let i = 0; i < longestStr; i++) {
      if (str1[i] !== str2[x]) {
        errorCount++;
        x++;
      }
      if (errorCount > 1) {
        return false;
      }
      x++;
    }
    // ***** Helper functions ********
    function findLongestStr(str1, str2) {
      str1 > str2 ? str1 : str2;
    }
  }
  return true;
}

// TESTS
console.log(isOneAway('pale', 'ple') === true);
console.log(isOneAway('pales', 'pale') === true);
console.log(isOneAway('pale', 'bale') === true);
console.log(isOneAway('pale', 'bake') === false);
