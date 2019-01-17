/* Write code to remove duplicates from an unsorted linked list */

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  push(val) {
    var node = new Node(val);
    if (!this.length) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.length++;
    return this;
  }
  convertToArray() {
    var array = [];
    if (!this.length) {
      array.push(`Head: ${this.head}`)
      array.push(`Tail: ${this.tail}`)
      return array;
    }
    array.push(`Head: ${this.head.val}`);
    var currentNode = this.head.next;
    for (let i = 1; i < this.length - 1; i++) {
      array.push(currentNode.val);
      currentNode = currentNode.next;
    }
    array.push(`Tail: ${this.tail.val}`);
    return array;
  }
}

const removeDupFromLinkList = (linkedList) => {
  if (!linkedList.length) return linkedList;
  const uniqueVals = {};
  var currentNode = linkedList.head;
  var prev = null;
  while (currentNode) {
    if (!uniqueVals[currentNode.val]) {
      uniqueVals[currentNode.val] = true;
      prev = currentNode;
    } else {
      // this is a duplicate so remove this node
      if (currentNode === linkedList.tail) {
        linkedList.tail = prev;
      }
      prev.next = currentNode.next;
      linkedList.length--;
    }
    currentNode = currentNode.next;
  }
  return linkedList;
}

//TESTS:

var linkedList = new SinglyLinkedList();
linkedList.push('2');
linkedList.push('4');
linkedList.push('4');
linkedList.push('3');
linkedList.push('2'); // 2-4-4-3-2
var actual = removeDupFromLinkList(linkedList).convertToArray();
var expected = ['Head: 2', '4', 'Tail: 3'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));

var linkedList2 = new SinglyLinkedList();
linkedList2.push('1');
linkedList2.push('3');
linkedList2.push('5'); // 1-3-5
actual = removeDupFromLinkList(linkedList2).convertToArray();
expected = ['Head: 1', '3', 'Tail: 5'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));

var linkedList3 = new SinglyLinkedList();
actual = removeDupFromLinkList(linkedList3).convertToArray();
expected = ['Head: null', 'Tail: null'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));
