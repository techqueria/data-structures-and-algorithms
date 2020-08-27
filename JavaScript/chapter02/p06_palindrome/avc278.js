// Palindrome: Implement a function to check if a linked list is a palindrome.

const assert = require("assert");
const { arrayToLinkedList } = require("../../lib/avc278/linkedlist");

/**
 * Checks whether the input linked list is a palindrome
 * @param   {LinkedListNode} list input linked list to check against
 * @return  {boolean}             whether the input linked list is a palindrome
 *
 * For this problem, we start by finding the midpoint idx of the linked list. This traversal takes O(N) runtime and O(1)
 * space as we only store a counter, and a pointer to the location within the linked list. We then perform another
 * traversal to point to the midpoint, and reverse the linked list from that point onwards. From this point onwards, we
 * only need to compare the two linked lists from the midpoint to the end, and from the start to the midpoint.
 * All in all, since we only perform traversals without any inner traversals, the runtime at any traversal is O(N),
 * where N is the length of the linked list, and O(1) space as we store pointers.
 * Runtime: O(N)
 * Space:   O(1)
 *
 */
const reverse = (node) => {
  let prev;
  while (node !== null) {
    const next = node.next;
    node.next = prev;
    prev = node;
    node = next;
  }
  return prev;
};

const isPalindrome = (list) => {
  let fast = list;
  let slow = list;
  let counter = 0;
  while (fast !== null) {
    fast = fast.next;
    counter += 1;
  }

  for (let i = 0; i < counter / 2; i++) {
    slow = slow.next;
  }

  slow = reverse(slow);
  while (!!slow && !!slow.next) {
    if (slow.val !== list.val) return false;
    slow = slow.next;
    list = list.next;
  }

  return true;
};

describe(module.filename, () => {
  it("should return true when the linked list of even length is a palindrome", () => {
    const arr = [1, 2, 3, 4, 4, 3, 2, 1];
    const ll = arrayToLinkedList(arr);

    assert.ok(isPalindrome(ll));
  });
  it("should return true when the linked list of odd length is a palindrome", () => {
    const arr = [1, 2, 3, 4, 3, 2, 1];
    const ll = arrayToLinkedList(arr);

    assert.ok(isPalindrome(ll));
  });
  it("should return false when the linked list is not a palindrome", () => {
    const arr = [1, 2, 3, 4, 3, 2, 1, 0];
    const ll = arrayToLinkedList(arr);

    assert.ok(!isPalindrome(ll));
  });
  it("should return true for a linked list with a single node", () => {
    const arr = [2];
    const ll = arrayToLinkedList(arr);

    assert.ok(isPalindrome(ll));
  });
  it("should return true for an empty linked list", () => {
    const arr = [];
    const ll = arrayToLinkedList(arr);

    assert.ok(isPalindrome(ll));
  });
});
