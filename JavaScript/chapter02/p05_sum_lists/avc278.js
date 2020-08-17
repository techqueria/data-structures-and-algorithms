// Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are
// stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two
// numbers and returns the sum as a linked list.
// Example
// Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
// Output: 2 -> 1 -> 9. That is, 912.
//
// Follow up: Suppose the digits are stored in forward order. Repeat the above problem.
// Example
// Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
// Output: 9 -> 1 -> 2. That is, 912.

const assert = require("assert");
const {
  arrayToLinkedList,
  compareLinkedLists,
  LinkedListNode,
} = require("../../lib/avc278/linkedlist");

/**
 * Sums two linked lists, where the linked lists are displayed in reverse order
 * @param   {LinkedListNode} listOne input linked list 1 to be added
 * @param   {LinkedListNode} listTwo input linked list 2 to be added
 * @return  {LinkedListNode}         ouput sum of input linked lists
 *
 * For this problem, we need to keep a carry in case two node values, when summed, are greater than 10. We also need to
 * keep track of the sum linked list head, as well as the previous and current nodes of the sum linked list.
 * We traverse through our two linked lists, adding their node values together, storing them into a temp sum, then
 * creating a new node based on that sum value, noting whether the sum is greater than 10 or not, and adding it on to
 * the sumHead linked list. Traversing through listOne requires a runtime of O(N) where N is the length of the list,
 * and similarly, traversing through listTwo requires a runtime of O(M) where M is the length of the list. Since they
 * travel at the same pace, this will require a runtime of of max(M, N). Since we need to construct an answer based on
 * the sum of the two lists, we will construct a linked list whose length is the maximum of M and N, plus 1, which
 * consequently also requires max(M, N) space.
 * Runtime: O(max(M, N))
 * Space:   O(max(M, N))
 *
 */
const sumLists = (listOne, listTwo) => {
  let carry = 0;
  let sumHead;
  let prevNode;

  while (carry > 0 || listOne !== null || listTwo !== null) {
    let sum = carry;
    if (listOne !== null) {
      sum += listOne.val;
      listOne = listOne.next;
    }
    if (listTwo !== null) {
      sum += listTwo.val;
      listTwo = listTwo.next;
    }

    carry = 0;
    if (sum >= 10) {
      carry = 1;
    }
    const currNode = new LinkedListNode(sum % 10);
    if (!sumHead) {
      sumHead = currNode;
    }

    if (prevNode) prevNode.next = currNode;
    prevNode = currNode;
  }

  return sumHead;
};

describe(module.filename, () => {
  it("should return the sum of two linked lists of the same length", () => {
    const arr1 = [7, 1, 6];
    const ll1 = arrayToLinkedList(arr1);
    const arr2 = [5, 9, 2];
    const ll2 = arrayToLinkedList(arr2);
    const expectedArrSum = [2, 1, 9];
    const expectedListSum = arrayToLinkedList(expectedArrSum);

    const sum = sumLists(ll1, ll2);

    assert.ok(compareLinkedLists(sum, expectedListSum));
  });
  it("should return the sum of two linked lists of different lengths", () => {
    const arr1 = [0, 1];
    const ll1 = arrayToLinkedList(arr1);
    const arr2 = [9, 9, 9];
    const ll2 = arrayToLinkedList(arr2);
    const expectedArrSum = [9, 0, 0, 1];
    const expectedListSum = arrayToLinkedList(expectedArrSum);

    const sum = sumLists(ll1, ll2);

    assert.ok(compareLinkedLists(sum, expectedListSum));
  });
  it("should return the sum of two linked lists when one is empty", () => {
    const arr1 = [0];
    const ll1 = arrayToLinkedList(arr1);
    const arr2 = [9, 9, 9];
    const ll2 = arrayToLinkedList(arr2);

    const sum = sumLists(ll1, ll2);

    assert.ok(compareLinkedLists(sum, ll2));
  });
});
