// Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all
// nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the
// elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not
// need to appear between the left and right partitions.
// EXAMPLE
// Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5]
// Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

const assert = require("assert");
const {
  arrayToLinkedList,
  compareLinkedLists,
} = require("../../lib/avc278/linkedlist");

/**
 * Partitions a linked list based on the input partition, with lesser values to the left and greater values to the right
 * @param   {LinkedListNode} head input linked list to be partitioned
 * @return  {LinkedListNode}      partitioned linked list
 *
 * For this problem, we need to store two linked lists: one for values lesser than `partitionValue`, and one for values
 * greater than `partitionValue`. We also need to store pointers for the heads of these linked lists as we need to merge
 * them at the end. Iterating once through the original linked list makes it so the runtime is O(N). We connect nodes
 * together in the less and more lists until we exhaust the original list. At this point, we connect the end of less to
 * the head of more, set `more`'s next to null and return the head of less.
 * Runtime: O(N)
 * Space:   O(N)
 *
 */
const partition = (head, partitionValue) => {
  let less;
  let lessHead;
  let more;
  let moreHead;

  while (head !== null) {
    if (head.val < partitionValue) {
      if (!less) {
        less = head;
        lessHead = head;
      } else {
        less.next = head;
        less = less.next;
      }
    } else {
      if (!more) {
        more = head;
        moreHead = head;
      } else {
        more.next = head;
        more = more.next;
      }
    }
    head = head.next;
  }
  less.next = moreHead;
  more.next = null;
  return lessHead;
};

describe(module.filename, () => {
  it("should return the partitioned linked list when the partition value exists in the linked list", () => {
    const arr = [3, 5, 8, 5, 10, 2, 1];
    const ll1 = arrayToLinkedList(arr);
    const expectedArr = [3, 2, 1, 5, 8, 5, 10];
    const expectedLL1 = arrayToLinkedList(expectedArr);

    partition(ll1, 5);

    assert.ok(compareLinkedLists(ll1, expectedLL1));
  });
  it("should return the partitioned linked list when the partition value does not exist in the linked list", () => {
    const arr = [1, 9, 3, 8, 6, 7, 4, 2, 10];
    const ll1 = arrayToLinkedList(arr);
    const expectedArr = [1, 3, 4, 2, 9, 8, 6, 7, 10];
    const expectedLL1 = arrayToLinkedList(expectedArr);

    partition(ll1, 5);

    assert.ok(compareLinkedLists(ll1, expectedLL1));
  });
});
