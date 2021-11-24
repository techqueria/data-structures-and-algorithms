// Three in One: Describe how you could use a single array to implement three stacks.
const assert = require("assert");
const { Stack, arrayToStack } = require("../../lib/avc278/stacksAndQueues");

/**
 * We start off by assuming we cannot use the benefits that dynamic languages like JavaScript bring to the table, so as
 * to provide a language-agnostic solution. Hence, upon creation of an array, we must declare the size, and performing a
 * `push()` on the array does not allocate additional memory.
 *
 * Say we have three stacks of different lengths; we should first start off by storing the length of the longest stack,
 * and creating a pseudo array whose length is 3 times that length, which we'll refer to as N. Then, at indices 0, N/3,
 * and 2N/3, we declare the starting positions of the stacks. At this point, we need to be careful when defining peek,
 * pop, and push stack-like behavior for this pseudo array class we created. We need to make sure that should we ever
 * pop() or push() outside the bounds of the allotted space for the subject stack in the array, we do nothing (ideally,
 * we should raise a verbose exception explaining why the expected behavior never happened).
 *
 * The following is an implementation of the above description:
 */

class _Array {
    constructor(arrLength) {
        this.arr = new Array(arrLength).fill(null);
        this.stackOneStartIdx = 0;
        this.stackOneCurrIdx = 0;
        this.stackTwoStartIdx = arrLength / 3;
        this.stackTwoCurrIdx = arrLength / 3;
        this.stackThreeStartIdx = 2 * arrLength / 3;
        this.stackThreeCurrIdx = 2 * arrLength / 3;
    };

    pop(stackNum) {
        let poppedVal;
        switch (stackNum) {
            case 1:
                if (this.arr[this.stackOneCurrIdx] === null) return;
                poppedVal = this.arr[this.stackOneCurrIdx];
                this.arr[this.stackOneCurrIdx] = null;
                this.stackOneCurrIdx = Math.max(this.stackOneCurrIdx - 1, this.stackOneStartIdx);
                return poppedVal;
            case 2:
                if (this.arr[this.stackTwoCurrIdx] === null) return;
                poppedVal = this.arr[this.stackTwoCurrIdx];
                this.arr[this.stackTwoCurrIdx] = null;
                this.stackTwoCurrIdx = Math.max(this.stackTwoCurrIdx - 1, this.stackTwoStartIdx);
                return poppedVal;
            case 3:
                if (this.arr[this.stackThreeCurrIdx] === null) return;
                poppedVal = this.arr[this.stackThreeCurrIdx];
                this.arr[this.stackThreeCurrIdx] = null;
                this.stackThreeCurrIdx = Math.max(this.stackThreeCurrIdx - 1, this.stackThreeStartIdx);
                return poppedVal;
            default:
                return;
        }
    };
    peek(stackNum) {
        switch (stackNum) {
            case 1:
                return this.arr[this.stackOneCurrIdx];
            case 2:
                return this.arr[this.stackTwoCurrIdx];
            case 3:
                return this.arr[this.stackThreeCurrIdx];
            default:
                return;
        }
    };
    push(stackNum, val) {
        switch (stackNum) {
            case 1:
                if (this.stackOneCurrIdx === this.stackTwoStartIdx - 1) return;
                if (this.arr[this.stackOneCurrIdx] !== null) this.stackOneCurrIdx += 1;
                this.arr[this.stackOneCurrIdx] = val;
                break;
            case 2:
                if (this.stackTwoCurrIdx === this.stackThreeStartIdx) return;
                if (this.arr[this.stackTwoCurrIdx] !== null) this.stackTwoCurrIdx += 1;
                this.arr[this.stackTwoCurrIdx] = val;
                break;
            case 3:
                if (this.stackThreeCurrIdx === this.arr.length) return;
                if (this.arr[this.stackThreeCurrIdx] !== null) this.stackThreeCurrIdx += 1;
                this.arr[this.stackThreeCurrIdx] = val;
                break;
            default:
                return;
        }
    };
};

// Helper function to convert a stack from A -> B -> C to C -> B -> A, and return its length
const invertStackAndGetLength = (stack) => {
    const res = new Stack();
    let length = 0;
    while (!stack.isEmpty()) {
        length += 1;
        res.push(stack.pop())
    }
    return [ res, length ];
}

/**
 * @param   {Stack} A input stack
 * @param   {Stack} B input stack
 * @param   {Stack} C input stack
 * @return  {_Array}  the array containing three stacks, with stack methods
 *
 * In implementing threeInOne, we need to know the longest stack length, which we'll call N, and the others M and P.
 * As we traverse through these stacks, we do so one after the other, which results in O(N + M + P), which is really
 * just O(N) as we can remove smaller terms. Creating the inverse stacks requires a maximum of O(N) space for the same
 * reason.
 * Now, when creating the output array (of type _Array), we require 3 * N additional time and space for traversal.
 * Again, however, this results in O(N) time and O(N) space as we can ignore the leading term.
 * 
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const threeInOne = (A, B, C) => {
    const [ invA, lenA ] = invertStackAndGetLength(A);
    const [ invB, lenB ] = invertStackAndGetLength(B);
    const [ invC, lenC ] = invertStackAndGetLength(C);
    
    const maxSize = Math.max(lenA, lenB, lenC);
    const arr = new _Array(maxSize * 3);
    while (!invA.isEmpty()) {
        arr.push(1, invA.pop());
    }
    while (!invB.isEmpty()) {
        arr.push(2, invB.pop());
    }
    while (!invC.isEmpty()) {
        arr.push(3, invC.pop());
    }

    return arr;
};

describe(module.filename, () => {
  it("should return an array containing the three input stacks.", () => {
    const A = arrayToStack([1,2,3]);
    const B = arrayToStack([4,5]);
    const C = arrayToStack([6,7,8,9,10]);
    const stackArr = threeInOne(A, B, C);

    const expectedStackArr = [1,2,3,null,null,4,5,null,null,null,6,7,8,9,10];
    assert.deepStrictEqual(stackArr.arr, expectedStackArr);
  });
  it("should behave like a stack when pushing, popping, and peeking any of the containing stack", () => {
    const A = arrayToStack([1,2,3]);
    const B = arrayToStack([4,5]);
    const C = arrayToStack([6,7,8,9,10]);
    const stackArr = threeInOne(A, B, C);

    assert.strictEqual(stackArr.pop(1), 3);
    assert.strictEqual(stackArr.pop(1), 2);
    assert.strictEqual(stackArr.peek(1), 1);
    stackArr.push(1, 100);
    assert.strictEqual(stackArr.peek(1), 100);

    assert.strictEqual(stackArr.peek(2), 5);
    assert.strictEqual(stackArr.peek(3), 10);
  })
});
