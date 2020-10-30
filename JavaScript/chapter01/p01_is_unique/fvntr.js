/* Write a function isUnique that:
Input: takes an array of integers
Output: returns a deduped array of integers
*/

// Solution using Set
const isUnique = (arr) => [...new Set(arr)];

// Test Cases
const assert = require('assert');

describe(module.filename, () => {
  it('should deduplicate array', () => {
    assert.deepEqual(isUnique([1,1,1,2,2,2,2,3,3,3,3]), [1,2,3]);
  });
});

//Solution using Object
const isUnique2=(arr)=>{
let obj = {}
for (let elem of arr){
  if(obj.hasOwnProperty(elem)) obj[elem]++
  else obj[elem] = 1
}

return Object.keys(obj)
}
//isUnique2([1,1,1,2,2,2,2,3,3,3,3]) //returns[1,2,3]
