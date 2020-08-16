// Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node,
// not necessarily the exact middle) of a singly linked list, given only access to that node.
// EXAMPLE:
// Input: the node c from the linked list a => b => c => d => e => f
// Result: nothing is returned, but the new linked list looks like a => b => d => e => f

const assert = require("assert");
const {
  arrayToLinkedList,
  compareLinkedLists,
} = require("../../library/avc278/linkedlist");

/**
 * Deletes an inputted node somewhere in the middle of the linked list
 * @param  {LinkedListNode} node input node to be removed
 * @return {null}
 *
 * There's no trick to this problem. We know that a linked list, fundamentally, is just a collection of nodes with
 * values that point to another node. We don't need to necessarily delete the selected node. We just need to overwrite
 * what that node represents. In other words, we can overwrite the next node onto the current node, then skip from the
 * current node to the next next node, effectively skipping over the node after the selected node since it's redundant.
 * Runtime: O(1)
 * Space:   O(1)
 *
 */
const deleteMiddleNode = (node) => {
  // It is safe to assume from the prompt that the given node exists in the linked list and is not the head nor tail
  const next = node.next;
  node.val = next.val;
  node.next = next.next;
};

describe(module.filename, () => {
  it("should remove a node in the middle of the linked list", () => {
    const arr = [1, 2, 3, 4, 5];
    let ll1 = arrayToLinkedList(arr);
    const nodeToBeRemoved = ll1.next.next.next;
    const expectedArr = [1, 2, 3, 5];
    let expectedLL1 = arrayToLinkedList(expectedArr);

    deleteMiddleNode(nodeToBeRemoved);

    assert.ok(compareLinkedLists(ll1, expectedLL1));
  });
});
