class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  //Function to insert a node in the singlely linkedlist.
  insert(data) {
    var newNode = new Node(data);
    if (this.head == null) {
      this.head = newNode;
    } else {
      var currentNode = this.head;
      while (currentNode.next) {
        currentNode = currentNode.next;
      }

      currentNode.next = newNode;
    }
  }

  //Function to print the singlely linkedlist.
  printList() {
    let currentNode = this.head;
    let list = "";
    while (currentNode) {
      list += currentNode.data + "->";
      currentNode = currentNode.next;
    }
    list += "null";
    console.log(list);
  }

  //Function to remove dupliicate nodes from the singlely linkedlist.
  removeDuplicates() {
    let currentNode1;
    currentNode1 = this.head;
    while (currentNode1 && currentNode1.next) {
      let currentNode2 = currentNode1;
      while (currentNode2.next) {
        if (currentNode1.data == currentNode2.next.data) {
          currentNode2.next = currentNode2.next.next;
        } else {
          currentNode2 = currentNode2.next;
        }
      }
      currentNode1 = currentNode1.next;
    }
  }
}
//main function.
var list1 = new LinkedList();
list1.insert(0);
list1.insert(1);
list1.insert(2);
list1.insert(3);
list1.insert(1);
list1.insert(4);
list1.insert(4);
console.log("Original List with Duplicates:");
list1.printList();
list1.removeDuplicates();
console.log("********************************");
console.log("New List free from Duplicates:");
list1.printList();
