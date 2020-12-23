

 /* Write a function isUnique that:
Input: takes an array of integers
Output: returns a deduped array of integers
*/

 //Solution using Object
const isUnique = (arr)=>{
 let obj = {}
 for (let elem of arr){
   if(obj.hasOwnProperty(elem)) obj[elem]++
   else obj[elem] = 1
 }

 return Object.keys(obj)
 }

//test cases
const assert = require('assert');
  describe(module.filename, () => {
    it("should return true on an input string with unique characters", () => {
      assert.equal(isUnique1("tech"), true);
      assert.equal(isUnique2("tech"), true);
    });
    it("should return false on an input string with non-unique characters", () => {
      assert.equal(isUnique1("techqueria"), false);
      assert.equal(isUnique2("techqueria"), false);
    });
  });
