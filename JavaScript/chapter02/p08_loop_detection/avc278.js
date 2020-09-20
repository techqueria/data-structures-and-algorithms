// Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the
// loop.
// Example: A -> B -> C -> D
//                    ^    |
//                    |    v
//                    | <- E
// Output: C
const assert = require("assert");
const { LinkedListNode } = require("../../lib/avc278/linkedlist");

/**
 *
 * @param   {LinkedListNode} list input linked list in which to find loop
 * @return  {LinkedListNode}      the node in the linked list that starts the loop
 *
 * Overall in this problem, we only keep track of pointers and a boolean, so we use O(1) additional space.
 * In terms of runtime complexity, we only iterate through the entire linked list one full time to find out where the
 * slow and fast runners intersect. After this, we start iterating through the linked list again, which in the worst
 * case, would result in iterating through the entire list again, but still only requires O(N) time, where N is the
 * size of the linked list.
 * Runtime: O(N)
 * Space:   O(1)
 *
 */
const loopDetection = (list) => {
  let slow = list;
  let fast = list;
  let intersect = false;

  while (!intersect) {
    slow = slow.next;
    fast = fast.next.next;

    if (slow !== fast) continue;
    intersect = true;
  }
  slow = list;

  while (slow !== fast) {
    slow = slow.next;
    fast = fast.next;
  }

  return slow;
};

describe(module.filename, () => {
  it("should return the head of the linked list when the tail points to the head.", () => {
    /*
        a1 -> a2 ->  a3 ->  |
        ^                   v
        | a7 <- a6 <- a5 <- a4
    */
    const a7 = new LinkedListNode(7);
    const a6 = new LinkedListNode(6, a7);
    const a5 = new LinkedListNode(5, a6);
    const a4 = new LinkedListNode(4, a5);
    const a3 = new LinkedListNode(3, a4);
    const a2 = new LinkedListNode(2, a3);
    const a1 = new LinkedListNode(1, a2);
    a7.next = a1;

    assert.strictEqual(loopDetection(a1), a1);
  });
  it("should return the tail of the linked list when the tail points to itself.", () => {
    /*
        a1 -> a2 ->  a3 ->  a4 -> a5 -> a6 -> a7 -> |
                                              ^     v
                                              |   < -  
    */
    const a7 = new LinkedListNode(7);
    const a6 = new LinkedListNode(6, a7);
    const a5 = new LinkedListNode(5, a6);
    const a4 = new LinkedListNode(4, a5);
    const a3 = new LinkedListNode(3, a4);
    const a2 = new LinkedListNode(2, a3);
    const a1 = new LinkedListNode(1, a2);
    a7.next = a7;

    assert.strictEqual(loopDetection(a1), a7);
  });
  it("should return some node in the middle that starts the loop.", () => {
    /*
        a1 -> a2 ->  a3 ->  a4 -> a5 -> |
                            ^           v
                            | <- a7 <- a6     
    */

    const a7 = new LinkedListNode(7);
    const a6 = new LinkedListNode(6, a7);
    const a5 = new LinkedListNode(5, a6);
    const a4 = new LinkedListNode(4, a5);
    const a3 = new LinkedListNode(3, a4);
    const a2 = new LinkedListNode(2, a3);
    const a1 = new LinkedListNode(1, a2);
    a7.next = a4;

    assert.strictEqual(loopDetection(a1), a4);
  });
});
