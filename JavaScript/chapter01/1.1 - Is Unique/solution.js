/* Write a function isUnique that:
Input: takes an array of integers
Output: returns a deduped array of integers
*/

// Solution using Set 
const isUnique = (arr) => [...new Set(arr)];

// Test Cases
console.log(isUnique([1,1,1,2,2,2,2,3,3,3,3]) === [1,2,3]); 