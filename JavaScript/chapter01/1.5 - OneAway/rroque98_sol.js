/* There are 3 types of edits that can be made on a string:
insert character, remove character, replace a character
Given 2 strings write a function that will check if it is
1 or 0 edits away*/

const isOneAway = (str1, str2) => {
  const diffInLen = Math.abs(str1.length - str2.length);
  if (diffInLen > 1) {
    return false;
  }

  let errorCount = 0;
  if (str1.length === str2.length) {
    for (let i = 0; i < str1.length; i++) {
      if (str1[i] !== str2[i]) {
        errorCount++;
        if (errorCount > 1) {
          return false;
        }
      }
    }
    return true;
  }
  const longStr = str1.length > str2.length ? str1 : str2;
  const shortStr = str1.length <= str2.length ? str1 : str2;
  for (let i = 0; i + errorCount < longStr.length; i++) {
    if (longStr[i + errorCount] === shortStr[i]) {
      continue;
    }
    errorCount++;
    if (errorCount > 1) {
      return false;
    }
  }
  return true;
};

// TESTS
console.log(isOneAway('pale', 'ple') === true); // deletion
console.log(isOneAway('pale', 'opale') === true); // insertion in beginning
console.log(isOneAway('pale', 'palse') === true); // insertion in middle
console.log(isOneAway('pale', 'pales') === true); // insertion at end
console.log(isOneAway('pale', 'bale') === true); // replacement
console.log(isOneAway('pale', 'ae') === false); // greater than 1 deletions
console.log(isOneAway('pale', 'ppalpe') === false); // greater than 1 insertions
console.log(isOneAway('pale', 'bake') === false); // greater than 1 replacements
console.log(isOneAway('pale', 'balpe') === false); // 1 insertion, 1 replacement
console.log(isOneAway('pale', 'plo') === false); // 1 deletion, 1 replacement
console.log(isOneAway('pale', 'ales') === false); // 1 deletion, 1 insertion
// swap str1 with str2
console.log(isOneAway('ple', 'pale') === true); // deletion
console.log(isOneAway('opale', 'pale') === true); // insertion in beginning
console.log(isOneAway('palse', 'pale') === true); // insertion in middle
console.log(isOneAway('pales', 'pale') === true); // insertion at end
console.log(isOneAway('bale', 'pale') === true); // replacement
console.log(isOneAway('ae', 'pale') === false); // greater than 1 deletions
console.log(isOneAway('ppalpe', 'pale') === false); // greater than 1 insertions
console.log(isOneAway('bake', 'pale') === false); // greater than 1 replacements
console.log(isOneAway('balpe', 'pale') === false); // 1 insertion, 1 replacement
console.log(isOneAway('plo', 'pale') === false); // 1 deletion, 1 replacement
console.log(isOneAway('ales', 'pale') === false); // 1 deletion, 1 insertion
console.log(isOneAway('p', 'b') === true);
console.log(isOneAway('', '') === true);
console.log(isOneAway('p', 'p') === true);
