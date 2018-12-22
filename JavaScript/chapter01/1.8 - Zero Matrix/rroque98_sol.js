/*Write an algorithm such that if an element
 in an M*N matrix is 0,it's entire row and column
  are set to 0*/

const zeroMatrix = (nestedArr) => {
  var rowsAndColsWithZeros = checkForZeroIndex(nestedArr);
  let rowLength = nestedArr[0].length;
  let columnLength = nestedArr.length;
  for (let i = 0; i < rowsAndColsWithZeros['rows'].length; i++) {
    let rowIndex = rowsAndColsWithZeros['rows'][i];
    for (let x = 0; x < rowLength; x++) {
      nestedArr[rowIndex][x] = 0;
    }
  }
  for (let i = 0; i < rowsAndColsWithZeros['columns'].length; i++) {
    let colIndex = rowsAndColsWithZeros['columns'][i];
    for (let x = 0; x < columnLength; x++) {
      nestedArr[x][colIndex] = 0;
    }
  }
  return nestedArr;

  // **** Helper functions ****
  function checkForZeroIndex(nestArr) {
    let zeroIndices = {rows: [], columns: []};
    for (let i = 0; i < nestArr.length; i++) {
      for (let x = 0; x < nestArr[i].length; x++) {
        if (nestArr[i][x] === 0) {
          zeroIndices['rows'].push(i);
          zeroIndices['columns'].push(x);
        }
      }
    }
    return zeroIndices;
  }
}

// **** TESTS ****:

var testArr1 = [
  [3, 5, 6],
  [1, 0, 2],
  [4, 4, 5],
  [2, 2, 2],
]

var resultArr1 = [
  [3, 0, 6],
  [0, 0, 0],
  [4, 0, 5],
  [2, 0, 2],
]

var testArr2 = [
  [3, 5, 6],
  [1, 0, 2],
  [4, 4, 0],
  [2, 0, 2],
]

var resultArr2 = [
  [3, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
]

var testArr3 = [
  [3, 5, 6],
  [0, 0, 2],
  [4, 4, 0],
  [2, 0, 2],
]

var resultArr3 = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
]
console.log(JSON.stringify(zeroMatrix(testArr1)) === JSON.stringify(resultArr1));
console.log(JSON.stringify(zeroMatrix(testArr2)) === JSON.stringify(resultArr2));
console.log(JSON.stringify(zeroMatrix(testArr3)) === JSON.stringify(resultArr3));
console.log(JSON.stringify(zeroMatrix([[]])) === JSON.stringify([[]]));
