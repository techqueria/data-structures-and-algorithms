// Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method
// to rotate the image by 90 degrees. Can you do this in place?

const assert = require("assert");

/**
 * Rotates the inputted 2d array by 90 degrees
 * @param  {Array.<number[]>} matrix input 2d array to rotate
 * @return {null}
 *
 * rotateMatrix is a void function since we don't actually return anything, but rather mutate the input array.
 * The trick here is to take the same knowledge of swapping two elements in an array with a temp to do it in place,
 *
 *      const swap = (arr, i, j) => {
 *        const temp = arr[i];
 *        arr[i] = arr[j];
 *        arr[j] = temp;
 *      }
 *
 * and apply that to a 2d array. Instead of tracking i and j in one array, we keep track of i, j, M-1-i, and M-1-j.
 * As we iterate through the array, the positions that we swap shift by one until we finish rotating elements, layer by
 * layer.
 *
 * Runtime: O(N^2)
 * Space:   O(1)
 *
 */
const rotateMatrix = (matrix) => {
  if (matrix.length < 2) return;

  const M = matrix.length;
  for (let i = 0; i < M / 2; i++) {
    for (let j = i; j < M - i - 1; j++) {
      const temp = matrix[i][j];
      // swap i, j, M-1-i, M-1-j
      matrix[i][j] = matrix[j][M - 1 - i];
      matrix[j][M - 1 - i] = matrix[M - 1 - i][M - 1 - j];
      matrix[M - 1 - i][M - 1 - j] = matrix[M - 1 - j][i];
      matrix[M - 1 - j][i] = temp;
    }
  }

  return;
};

describe(module.filename, () => {
  it("should not affect a matrix of size 0", () => {
    const matrix = [];

    rotateMatrix(matrix);
    assert.deepEqual(matrix, []);
  });
  it("should not affect a matrix of size 1", () => {
    const matrix = [5];

    rotateMatrix(matrix);
    assert.deepEqual(matrix, [5]);
  });
  it("should rotate a 2x2 matrix 90 degrees", () => {
    const matrix = [
      [1, 2],
      [3, 4],
    ];

    rotateMatrix(matrix);
    assert.deepEqual(matrix, [
      [2, 4],
      [1, 3],
    ]);
  });
  it("should rotate a 3x3 matrix 90 degrees", () => {
    const matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ];

    rotateMatrix(matrix);
    assert.deepEqual(matrix, [
      [3, 6, 9],
      [2, 5, 8],
      [1, 4, 7],
    ]);
  });
  it("should rotate a 4x4 matrix 90 degrees", () => {
    const matrix = [
      [11, 12, 13, 14],
      [15, 16, 17, 18],
      [19, 20, 21, 22],
      [23, 24, 25, 26],
    ];

    rotateMatrix(matrix);
    assert.deepEqual(matrix, [
      [14, 18, 22, 26],
      [13, 17, 21, 25],
      [12, 16, 20, 24],
      [11, 15, 19, 23],
    ]);
  });
  it("should bring the matrix to its original position after rotating 4 times.", () => {
    const matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ];

    rotateMatrix(matrix);
    rotateMatrix(matrix);
    rotateMatrix(matrix);
    rotateMatrix(matrix);
    assert.deepEqual(matrix, [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ]);
  });
});
