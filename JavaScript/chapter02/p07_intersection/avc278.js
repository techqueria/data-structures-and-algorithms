// Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter­secting node.
// Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked
// list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

const assert = require("assert");
const { LinkedListNode } = require("../../lib/avc278/linkedlist");

/**
 *
 * @param   {LinkedListNode} A input linked list to check against
 * @param   {LinkedListNode} B input linked list to check against
 * @return  {any}              whether the input linked list is a palindrome
 *
 * For this problem, we need to figure out the length of the two linked lists in order to know where the possible
 * intersection occurs. This is because once the two linked lists intersect, the length from the intersection to the end
 * of the linked list is the same. And so, when we compare the linked lists after finding the size, we can offset the
 * longer linked list by the difference in size. When we first reach the end in the first traversal, we can check
 * immediately if the two tail nodes are the same. If they are not, we can exit early and return false since we know
 * they don't intersect.
 *
 * Otherwise, we offset the longer of the two linked lists, and step one node at a time until we reach nodes that are
 * equal. At this point, we have found our intersecting node, and return the node. In terms of runtime analysis, since
 * we do traverse both linked lists A and B, we require O(A + B) time. Since we only store size counters, and pointers
 * to sections in the linked lists, we only use up O(1) additional space.
 *
 * Runtime: O(A+B)
 * Space:   O(1)
 *
 */
const intersection = (A, B) => {
  if (!A || !B) return false;

  let aSize = 1;
  let currA = A;
  while (currA.next) {
    aSize += 1;
    currA = currA.next;
  }

  let bSize = 1;
  let currB = B;
  while (currB.next) {
    bSize += 1;
    currB = currB.next;
  }

  if (currA !== currB) return false;

  let smaller = aSize < bSize ? A : B;
  let longer = aSize < bSize ? B : A;
  let diff = Math.abs(aSize - bSize);

  while (diff > 0) {
    longer = longer.next;
    diff -= 1;
  }

  while (smaller !== longer) {
    smaller = smaller.next;
    longer = longer.next;
  }

  return smaller;
};

describe(module.filename, () => {
  it("should return false when given an empty linked list", () => {
    const a1 = null;
    const b1 = new LinkedListNode(1, null);

    assert.ok(!intersection(a1, b1));
  });
  it("should return false when the linked lists do not intersect, even though the node values are the same.", () => {
    /*
     *    a1 -> a2 -> a3 -> a4 -> a5 -> a6 -> a7
     *
     *          b1 -> b2 -> b3 -> b4 -> b5 -> b6
     */
    const a7 = new LinkedListNode(7, null);
    const a6 = new LinkedListNode(6, a7);
    const a5 = new LinkedListNode(5, a6);
    const a4 = new LinkedListNode(4, a5);
    const a3 = new LinkedListNode(3, a4);
    const a2 = new LinkedListNode(2, a3);
    const a1 = new LinkedListNode(1, a2);

    const b6 = new LinkedListNode(6, null);
    const b5 = new LinkedListNode(5, b6);
    const b4 = new LinkedListNode(4, b5);
    const b3 = new LinkedListNode(3, b4);
    const b2 = new LinkedListNode(2, b3);
    const b1 = new LinkedListNode(1, b2);

    assert.ok(!intersection(a1, b1));
  });
  it("should return the intersecting node when the two linked lists intersect.", () => {
    /*
     *    a1 -> a2 -> a3 -> a4
     *                        \
     *                          -> c1 -> c2 -> c3
     *                        /
     *          b1 -> b2 -> b3
     */
    const c3 = new LinkedListNode(7, null);
    const c2 = new LinkedListNode(6, c3);
    const c1 = new LinkedListNode(5, c2);

    const a4 = new LinkedListNode(4, c1);
    const a3 = new LinkedListNode(3, a4);
    const a2 = new LinkedListNode(2, a3);
    const a1 = new LinkedListNode(1, a2);

    const b3 = new LinkedListNode(3, c1);
    const b2 = new LinkedListNode(3, b3);
    const b1 = new LinkedListNode(3, b2);

    assert.equal(intersection(a1, b1), c1);
  });
});
