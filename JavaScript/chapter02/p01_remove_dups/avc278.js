// Remove Dups: Write code to remove duplicates from an unsorted linked list.
// Follow Up: How would you solve this problem if a temporary buffer is not allowed?

const assert = require("assert");

class LinkedListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * Removes duplicates from a linked list
 * @param  {LinkedList} LL input linked list to mutate
 * @return {null}
 *
 * Keep a temporary set for storing values we pass through, of maximum size N where N is the number of nodes in the
 * input linked list in the worst case. This requires an additional O(N) space. We store two pointers as we traverse
 * through the linked list, skipping nodes with values already in our set.
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const removeDups1 = (LL) => {
  const seen = new Set();
  let currNode = LL;
  let next = LL.next;
  seen.add(currNode.val);
  while (next !== null) {
    if (!seen.has(next.val)) {
      seen.add(next.val);
      currNode.next = next;
      currNode = currNode.next;
    }
    next = next.next;
  }

  currNode.next = null;
};

/**
 * Removes duplicates from a linked list
 * @param  {LinkedList} LL input linked list to mutate
 * @return {null}
 *
 * Instead of keeping a temporary set, we need another way to remove all future dupes of the current node.
 * One way of doing this, is to skip all future nodes containing the same val as the current one.
 * This nest loop through the linked list increases our run time to O(N^2), but since we don't use any additional space,
 * we reduced the space complexity to O(1).
 *
 * Runtime: O(N^2)
 * Space:   O(1)
 *
 */
const removeDups2 = (LL) => {
  let currNode = LL;
  while (currNode.next !== null) {
    let nextNode = currNode;
    while (nextNode.next !== null) {
      if (nextNode.val === nextNode.next.val) {
        nextNode.next = nextNode.next.next;
      }
      nextNode = nextNode.next;
    }
    currNode = currNode.next;
  }
};

describe(module.filename, () => {
  it("should return the linked list without duplicates", () => {
    const ll6 = new LinkedListNode(4);
    const ll5 = new LinkedListNode(2, ll6);
    const ll4 = new LinkedListNode(4, ll5);
    const ll3 = new LinkedListNode(3, ll4);
    const ll2 = new LinkedListNode(2, ll3);
    let ll1 = new LinkedListNode(2, ll2);
    const head = ll1;

    const expectedLL3 = new LinkedListNode(4);
    const expectedLL2 = new LinkedListNode(3, expectedLL3);
    let expectedLL1 = new LinkedListNode(2, expectedLL2);
    const expectedHead = expectedLL1;

    removeDups1(ll1);
    while (ll1 !== null && expectedLL1 !== null) {
      assert.equal(ll1.val, expectedLL1.val);
      ll1 = ll1.next;
      expectedLL1 = expectedLL1.next;
    }

    ll1 = head;
    expectedLL1 = expectedHead;
    removeDups2(ll1);
    while (ll1 !== null && expectedLL1 !== null) {
      assert.equal(ll1.val, expectedLL1.val);
      ll1 = ll1.next;
      expectedLL1 = expectedLL1.next;
    }
  });
});
