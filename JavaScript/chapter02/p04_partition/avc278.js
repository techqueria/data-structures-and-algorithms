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
 * A destructive function, `partition`, splits a linked list based on the input `partitionValue`, with lesser values to
 * the left and greater values to the right.
 * @param   {LinkedListNode} head input linked list to be partitioned
 * @return  {LinkedListNode}      partitioned linked list
 *
 * For this problem, we need to store pointers to four linked list nodes:
 * `lessHead` - pointing to the head of the linked list containing values less than the partition value
 * `lessTail` - pointing to the tail of the linked list containing values less than the partition value
 * `moreHead` - pointing to the head of the linked list containing values more than the partition value
 * `moreTail` - pointing to the tail of the linked list containing values more than the partition value
 * Iterating once through the original linked list makes it so the runtime is O(N), where N is the length of the input
 * linked list. Since we only store four pointers to nodes at one time, our additional space required is O(1).
 * Runtime: O(N)
 * Space:   O(1)
 *
 */
const partition = (head, partitionValue) => {
  let lessHead;
  let lessTail;
  let moreHead;
  let moreTail;

  while (head !== null) {
    if (head.val < partitionValue) {
      if (!lessTail) {
        lessTail = head;
        lessHead = head;
      } else {
        lessTail.next = head;
        lessTail = lessTail.next;
      }
    } else {
      if (!moreTail) {
        moreTail = head;
        moreHead = head;
      } else {
        moreTail.next = head;
        moreTail = moreTail.next;
      }
    }
    head = head.next;
  }

  if (!lessHead && moreHead) {
    head = moreHead;
  } else if (lessHead && !moreHead) {
    head = lessHead;
  } else {
    lessTail.next = moreHead;
    moreTail.next = null;
  }
};

describe(module.filename, () => {
  it("should return the partitioned linked list when the partition value exists in the linked list", () => {
    const arr = [3, 5, 8, 5, 10, 2, 1];
    const ll = arrayToLinkedList(arr);
    const expectedArr = [3, 2, 1, 5, 8, 5, 10];
    const expectedPartition = arrayToLinkedList(expectedArr);

    partition(ll, 5);

    assert.ok(compareLinkedLists(ll, expectedPartition));
  });
  it("should return the partitioned linked list when the partition value does not exist in the linked list", () => {
    const arr = [1, 9, 3, 8, 6, 7, 4, 2, 10];
    const ll = arrayToLinkedList(arr);
    const expectedArr = [1, 3, 4, 2, 9, 8, 6, 7, 10];
    const expectedPartition = arrayToLinkedList(expectedArr);

    partition(ll, 5);

    assert.ok(compareLinkedLists(ll, expectedPartition));
  });
  it("should return the partitioned linked list when the partition value is less than all values in the array", () => {
    const arr = [10];
    const ll = arrayToLinkedList(arr);
    const expectedArr = [10];
    const expectedPartition = arrayToLinkedList(expectedArr);

    partition(ll, 5);

    assert.ok(compareLinkedLists(ll, expectedPartition));
  });
  it("should return the partitioned linked list when the partition value is more than all values in the array", () => {
    const arr = [1];
    const ll = arrayToLinkedList(arr);
    const expectedArr = [1];
    const expectedPartition = arrayToLinkedList(expectedArr);

    partition(ll, 5);

    assert.ok(compareLinkedLists(ll, expectedPartition));
  });
});
