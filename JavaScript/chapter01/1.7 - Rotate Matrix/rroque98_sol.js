/*Given an image represented by an N*N matrix where
each pixel in the image is 4 bytes, write a method
to rotate the image by 90 degrees. Can you do this
in place?*/

const rotateImage = (nestedArr) => {
  if (nestedArr.length === 0) {
    return [];
  }
  var rotatedArr = [];
  var numOfRows = nestedArr[0].length;
  for (let x = 0; x < numOfRows; x++) {
    let newRow = [];
    for (let i = nestedArr.length - 1; i >= 0; i--) {
      newRow.push(nestedArr[i][x]);
    }
    rotatedArr.push(newRow);
  }
  return rotatedArr;
}

// TESTS:
console.log(JSON.stringify(rotateImage([[1,2,3],[4,5,6]])) === JSON.stringify([[4,1],[5,2],[6,3]]));
console.log(JSON.stringify(rotateImage([])) === JSON.stringify([]));

// input: array of array
// output: array of array rotated
// constraits: Do it in place
// edge cases: rotate clockwise? is this represented by an array of arrays of numbers?
