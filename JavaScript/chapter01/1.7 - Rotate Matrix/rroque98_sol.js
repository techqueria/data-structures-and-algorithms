/*Given an image represented by an N*N matrix where
each pixel in the image is 4 bytes, write a method
to rotate the image by 90 degrees. Can you do this
in place?*/

const rotateImage = nestedArr => {
  const n = nestedArr.length;
  if (n === 0 || n === 1) {
    return nestedArr;
  }
  var rotatedArr = [];
  for (let col = 0; col < n; col++) {
    let newRow = [];
    for (let row = n - 1; row >= 0; row--) {
      newRow.push(nestedArr[row][col]);
    }
    rotatedArr.push(newRow);
  }
  return rotatedArr;
};

// TESTS:
console.log(
  JSON.stringify(rotateImage([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) ===
    JSON.stringify([[7, 4, 1], [8, 5, 2], [9, 6, 3]])
);
console.log(JSON.stringify(rotateImage([[1]])) === JSON.stringify([[1]]));
console.log(JSON.stringify(rotateImage([[]])) === JSON.stringify([[]]));
console.log(JSON.stringify(rotateImage([])) === JSON.stringify([]));
