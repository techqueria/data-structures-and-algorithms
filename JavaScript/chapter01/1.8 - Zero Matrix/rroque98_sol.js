/*Write an algorithm such that if an element
 in an M*N matrix is 0,it's entire row and column
  are set to 0*/

const zeroMatrix = nestedArr => {
  const rowsAndColsWithZeros = checkForZeroIndex(nestedArr);
  const rowLength = nestedArr[0].length;
  const columnLength = nestedArr.length;
  for (const row in rowsAndColsWithZeros['rows']) {
    for (let col = 0; col < rowLength; col++) {
      nestedArr[row][col] = 0;
    }
  }
  for (const col in rowsAndColsWithZeros['columns']) {
    for (let row = 0; row < columnLength; row++) {
      nestedArr[row][col] = 0;
    }
  }
  return nestedArr;
};

// **** Helper function ****
function checkForZeroIndex(nestArr) {
  let zeroIndices = { rows: {}, columns: {} };
  for (let row = 0; row < nestArr.length; row++) {
    for (let col = 0; col < nestArr[row].length; col++) {
      if (nestArr[row][col] === 0) {
        zeroIndices['rows'][row] = true;
        zeroIndices['columns'][col] = true;
      }
    }
  }
  return zeroIndices;
}

// **** TESTS ****:
let actual = zeroMatrix([[]]);
let expected = [[]];
isEqual(actual, expected);

actual = zeroMatrix([[3, 5, 6], [1, 0, 2], [4, 4, 5], [2, 2, 2]]);
expected = [[3, 0, 6], [0, 0, 0], [4, 0, 5], [2, 0, 2]];
isEqual(actual, expected);

actual = zeroMatrix([[3, 5, 6], [1, 0, 2], [4, 4, 0], [2, 0, 2]]);
expected = [[3, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]];
isEqual(actual, expected);

actual = zeroMatrix([[3, 5, 6], [0, 0, 2], [4, 4, 0], [2, 0, 2]]);
expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]];
isEqual(actual, expected);

function isEqual(actual, expected) {
  console.log(JSON.stringify(actual) === JSON.stringify(expected));
}

// ****HELPER FUNCTION TESTS ****:
actual = checkForZeroIndex([[1, 2, 0]]);
expected = { rows: { 0: true }, columns: { 2: true } };
testCheckForZeroIndex(actual, expected);

actual = checkForZeroIndex([[0]]);
expected = { rows: { 0: true }, columns: { 0: true } };
testCheckForZeroIndex(actual, expected);

actual = checkForZeroIndex([[1, 2, 3], [4, 0, 5], [6, 0, 8]]);
expected = { rows: { 1: true, 2: true }, columns: { 1: true } };
testCheckForZeroIndex(actual, expected);

function testCheckForZeroIndex(actual, expected) {
  let rows = JSON.stringify(actual.rows);
  let cols = JSON.stringify(actual.columns);
  let expRows = JSON.stringify(expected.rows);
  let expCols = JSON.stringify(expected.columns);
  console.log(rows === expRows && cols === expCols);
}
