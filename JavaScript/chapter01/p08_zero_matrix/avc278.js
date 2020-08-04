// Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and columns are set to 0.

const assert = require("assert");

/**
 * Overwrite rows and columns who have at least 1 zero in them with zeros.
 * @param  {Array.<number[]>} matrix input 2d array to mutate
 * @return {null}
 *
 * Okay, so I have a jank solution that assumes no element in the array is currently -999.
 * We iterate through the array, and when we find a 0, we flag its row and column by updating all elements in there to
 * -999. The outer two for loop iterations is O(M * N) time, and each inner for loop is O(M) and O(N), respectively,
 * resulting in a grand total of O((M * N) * (M + N)) time complexity, while updating takes O(1) additional space.
 * When we take a second pass at the matrix, we update all elements that have been flagged -999 to 0, which is O(N^2)
 * time and O(1) additional space.
 *
 * Runtime: O((M * N) * (M + N))
 * Space:   O(1)
 *
 */
const zeroMatrix = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      if (arr[i][j] !== 0) continue;

      for (let k = 0; k < arr.length; k++) {
        if (arr[k][j] !== 0) arr[k][j] = -999;
      }

      for (let l = 0; l < arr[0].length; l++) {
        if (arr[i][l] !== 0) arr[i][l] = -999;
      }
    }
  }

  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      if (arr[i][j] === -999) {
        arr[i][j] = 0;
      }
    }
  }
};

describe(module.filename, () => {
  it("should not affect a matrix of size 0", () => {
    const matrix = [];

    zeroMatrix(matrix);
    assert.deepEqual(matrix, []);
  });
  it("should not affect a matrix without 0s", () => {
    const matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ];

    zeroMatrix(matrix);
    assert.deepEqual(matrix, [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ]);
  });
  it("should update all rows and columns with at least one 0 to all 0s", () => {
    const matrix = [
      [0, 2, 3, 1],
      [4, 5, 6, 1],
      [7, 8, 9, 1],
    ];

    zeroMatrix(matrix);
    assert.deepEqual(matrix, [
      [0, 0, 0, 0],
      [0, 5, 6, 1],
      [0, 8, 9, 1],
    ]);
  });
  it("should update all rows and columns with at least one 0 to all 0s when multiple 0s are present", () => {
    const matrix = [
      [0, 2, 3],
      [4, 5, 0],
      [7, 8, 9],
    ];

    zeroMatrix(matrix);
    assert.deepEqual(matrix, [
      [0, 0, 0],
      [0, 0, 0],
      [0, 8, 0],
    ]);
  });
});
