/* Deletes a node in the middle (not necessarily the exact middle. 
Any node except for the first and last nodeof a singly linked list,
 given access only to that node*/

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
  deleteMiddleNode(node) {
    var currentNode = this.head.next;
    var prev = this.head;
    for (let i = 1; i < this.length - 1; i++) {
      if (currentNode.val === node.val) {
        prev.next = currentNode.next;
        this.length--;
        return;
      }
      prev = currentNode;
      currentNode = currentNode.next;
    }
  }
}

//TESTS:

var linkedList = new SinglyLinkedList();
linkedList.push('2');
linkedList.push('4');
linkedList.push('4');
linkedList.push('3');
linkedList.push('1'); // 2-4-4-3-1

let node7 = {val: '2'};
linkedList.deleteMiddleNode(node7);
var actual = linkedList.convertToArray();
var expected = ['Head: 2', '4', '4', '3', 'Tail: 1'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));

let node1 = {val: '4'};
linkedList.deleteMiddleNode(node1);
var actual = linkedList.convertToArray();
var expected = ['Head: 2', '4', '3', 'Tail: 1'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));

let node2 = {val: '3'};
linkedList.deleteMiddleNode(node2);
actual = linkedList.convertToArray();
expected = ['Head: 2', '4', 'Tail: 1'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));

let node3 = {val: '5'};
linkedList.deleteMiddleNode(node3);
actual = linkedList.convertToArray();
expected = ['Head: 2', '4', 'Tail: 1'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));

let node4 = {val: '4'};
linkedList.deleteMiddleNode(node4);
actual = linkedList.convertToArray();
expected = ['Head: 2', 'Tail: 1'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));

let node5 = {val: '2'};
linkedList.deleteMiddleNode(node5);
actual = linkedList.convertToArray();
expected = ['Head: 2', 'Tail: 1'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));

let node6 = {val: '1'};
linkedList.deleteMiddleNode(node6);
actual = linkedList.convertToArray();
expected = ['Head: 2', 'Tail: 1'];
console.log(JSON.stringify(actual) === JSON.stringify(expected));
