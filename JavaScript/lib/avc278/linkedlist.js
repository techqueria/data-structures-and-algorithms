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

  while (A !== null && B !== null) {
    if (A.val !== B.val) return false;
    A = A.next;
    B = B.next;
  }

  return !A && !B;
};

describe(module.filename, () => {
  it("should return false when comparing unequal linked lists", () => {
    assert.ok(
      !compareLinkedLists(arrayToLinkedList([]), arrayToLinkedList(["hi!"]))
    );
  });
  it("should return false when comparing another pair of unequal linked lists", () => {
    assert.ok(
      !compareLinkedLists(arrayToLinkedList([1, 2]), arrayToLinkedList([1]))
    );
  });
});

module.exports = { arrayToLinkedList, compareLinkedLists };
