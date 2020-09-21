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
 * This problem can be solved through an implementation of Floyd's cycle detecting algorithm, which runs in O(N) and has
 * O(1) space complexity. We only keep track of slow/fast pointers in the linked list, so we use O(1) additional space.
 * In terms of runtime complexity, we only iterate through the entire linked list one full time to find out where the
 * slow and fast runners intersect. Knowing the slow and fast runners intersect is the crucial first step in knowing
 * which node begins the looping cycle.Say for example you have two runners in a track, where the slow runner goes 1m/s
 * and the fast runner goes 2m/s, and where the end is the same as the start, or in our case, the "last" node is linked
 * back to the first node in the linked list. We can determine the node that starts the loop by restarting the slow
 * runner to the beginning of the race, then have both the slow and fast runner travel at the same pace of 1m/s. Here,
 * they will both collide on the same node (the starting/finishing line of the track) at the same instance,
 * and that will be the node that starts the cycle. Alternatively, if we modify the track field so the last meter in the
 * race is a never-ending circle, we can apply the same logic as above to find the node the begins the cycle. And lastly
 * if we were to put the cycle start somewhere in the middle of the track, the logic isn't so intuitive. So where is the
 * magic behind this approach? It just boils down to solving a system of equations:
 *
 *  a -> b -> c -> d -> e -> |
 *                 ^         v
 *                 | <- g <- f
 *
 * In the above cycle, we start the slow and fast runners at the head "a". The slow runner travels one node at a time,
 * and the fast runner travels two nodes at a time. Once both runners enter the cycle, whose distance from the head node
 * is of length H, they are guaranteed to intersect at some node in the cycle, whose distance from the cycle start is of
 * length I, after looping through the cycle of length C. The slow runner will loop through the cycle S times, and the
 * fast runner will loop through the cycle F times before they intersect.
 * We can state this as follows:
 *
 * H + SC + I = 2 * (H + FC + I)
 * H + SC + I = 2H + 2FC + 2I
 * SC - 2FC = H + I
 * C(S - 2F) = H + I
 * S - 2F is an integer, C is an integer, and (H + I) is a multiple of C, which is also an integer
 * stating that there exists a node where the slow and fast runners intersect, but also there is a node they must both
 * reach that starts the cycle.
 *
 * The next step here is to acknowledge that if we reset the slow runner to the beginning and make both runners travel
 * H nodes, both nodes will be in the cycle, and that after some multiple of C cycles, this can be reduced to the simple
 * problem from above where two runners are running around a track where the start node proceeds the end node, except
 * the runners are starting at different nodes, but will reach the starting node at the same instance.
 *
 * Runtime: O(N)
 * Space:   O(1)
 *
 */
const loopDetection = (list) => {
  let slow = list;
  let fast = list;

  do {
    slow = slow.next;
    fast = fast.next.next;
  } while (slow !== fast);
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
