// Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

const assert = require("assert");

class LinkedListNode {
  constructor(val, next) {
    this.val = val === undefined ? null : val;
    this.next = next === undefined ? null : next;
  }
}

const arrayToLinkedList = (arr) => {
  let tail = null;
  for (let i = arr.length - 1; i >= 0; i--) {
    tail = new LinkedListNode(arr[i], tail);
  }
  return tail;
};

/**
 * Returns the kth to last node in a linked list
 * @param  {LinkedListNode} list input linked list
 * @param  {number}         K    element index from the right which we wish to return
 * @return {null}
 *
 * In this approach, we utilize two pointers, `fast` and `slow` to keep track of how far we've traveled through the
 * linked list. We make `fast` travel K steps, before `slow` can start traveling. Then we iterate through both lists
 * until `fast` reaches the end. At that point, we know that the `slow` traversal is the kth to last value.
 *
 * Runtime: O(N)
 * Space:   O(1)
 *
 */
const returnKthToLast = (list, K) => {
  let fast = list;
  let slow = list;

  while (K > 0) {
    if (!fast) return null;
    fast = fast.next;
    K -= 1;
  }
  while (fast !== null) {
    fast = fast.next;
    slow = slow.next;
  }
  return slow.val;
};

describe(module.filename, () => {
  const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const linkedList = arrayToLinkedList(arr);
  for (let i = 1; i < arr.length + 1; i++) {
    it(`should return the ${i}th to last element in the linked list`, () => {
      const kthElement = returnKthToLast(linkedList, i);
      const expectedKthElement = arr[arr.length - i];
      assert.equal(kthElement, expectedKthElement);
    });
  }
  it("should return null when K is out of bounds", () => {
    const smallArr = [1, 2];
    const smallLinkedList = arrayToLinkedList(smallArr);
    const bigK = 5;

    const kthElement = returnKthToLast(smallLinkedList, bigK);
    const expectedKthElement = null;
    assert.equal(kthElement, expectedKthElement);
  });
});
