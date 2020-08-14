// Remove Dups: Write code to remove duplicates from an unsorted linked list.
// Follow Up: How would you solve this problem if a temporary buffer is not allowed?

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

const compareLinkedLists = (A, B) => {
  if (!A && !B) return true;
  if (!A || !B) return false;

  while (A !== null && B !== null) {
    if (A.val !== B.val) return false;
    A = A.next;
    B = B.next;
  }
  return true;
};

/**
 * Removes duplicates from a linked list
 * @param  {LinkedListNode} list input linked list to mutate
 * @return {null}
 *
 * Keep a temporary set for storing values we pass through, of maximum size N where N is the number of nodes in the
 * input linked list in the worst case. This requires an additional O(N) space. We store two pointers as we traverse
 * through the linked list, skipping nodes with values already in our set.
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const removeDups1 = (list) => {
  if (!list) return;
  const seen = new Set();
  let currNode = list;
  seen.add(currNode.val);
  for (let nextNode = currNode.next; nextNode.next !== null; nextNode = nextNode.next) {
    if (seen.has(nextNode.val)) continue;

    seen.add(nextNode.val);
    currNode.next = nextNode;
    currNode = currNode.next;
  }

  currNode.next = null;
};

/**
 * Removes duplicates from a linked list
 * @param  {LinkedListNode} list input linked list to mutate
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
const removeDups2 = (list) => {
  if (!list) return;
  let currNode = list;
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

const removeDups = [removeDups1, removeDups2];
removeDups.forEach((removeDup) => {
  describe(removeDup.name, () => {
    it("should return the linked list without duplicates", () => {
      const arr = [2, 2, 3, 4, 2, 4];
      let ll1 = arrayToLinkedList(arr);
      const expectedArr = [2, 3, 4];
      let expectedLL1 = arrayToLinkedList(expectedArr);

      removeDup(ll1);
      assert.ok(compareLinkedLists(ll1, expectedLL1));
    });
    it("should return an empty linked list", () => {
      const arr = [];
      let ll1 = arrayToLinkedList(arr);
      const expectedArr = [];
      let expectedLL1 = arrayToLinkedList(expectedArr);

      removeDup(ll1);
      assert.ok(compareLinkedLists(ll1, expectedLL1));
    });
    it("should return an empty linked list", () => {
      assert.ok(
        !compareLinkedLists(arrayToLinkedList([]), arrayToLinkedList(["hi!"]))
      );
    });
  });
});
