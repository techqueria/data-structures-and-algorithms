/* Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. */

var linkedList = function(value) {
    this.value = value;
    this.next = null;
};

// N.B. this algorithm is wrong, since it does not produce the desired result.
var findKthToLast = function(k, head) {
    //do recursive
    if ( head == null || k < 1 ) {
        return null;
    } else if ( k == 1 ) {
        return head.value;
    } else {
        return findKthToLast(k-1, head.next);
    }
};

/* Tests */
const assert = require('assert');

describe(module.filename, () => {
  it('should find k-th to last entry', () => {
    var a = new linkedList('1');
    var b = new linkedList('2');
    var c = new linkedList('3');
    var d = new linkedList('4');
    var e = new linkedList('5');
    var f = new linkedList('6');
    var g = new linkedList('7');

    a.next = b;
    b.next = c;
    c.next = d;
    d.next = e;
    e.next = f;
    f.next = g;

    assert.equal(findKthToLast(3, a), '3');
    assert.equal(findKthToLast(10, a), null);
    assert.equal(findKthToLast(-1, a), null);
    assert.equal(findKthToLast(0, a), null);
    assert.equal(findKthToLast(1, a), '1');
  });
});
