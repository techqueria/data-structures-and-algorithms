const assert = require("assert");

class Stack {
  constructor() {
    this.top;
  }
  pop() {
    if (!this.top) return;
    const poppedVal = this.top.val;
    this.top = this.top.next;
    return poppedVal;
  }
  push(val) {
    const newNode = new StackNode(val);
    if (this.top) {
      newNode.next = this.top;
      this.top = newNode;
    } else {
      this.top = newNode;
    }
  }
  peek() {
    if (!this.top) return;
    return this.top.val;
  }
  isEmpty() {
    return !this.top;
  }
}

class StackNode {
  constructor(val, next) {
    this.val = val === undefined ? null : val;
    this.next = next === undefined ? null : next;
  }
}

const arrayToStack = (arr) => {
  const stack = new Stack();
  for (const el of arr) {
    stack.push(el);
  }
  return stack;
};

class Queue {
  constructor() {
    this.start;
    this.end;
  }
  add(val) {
    const newNode = new QueueNode(val);
    if (this.end) {
      this.end.next = newNode;
    }
    this.end = newNode;
    if (!this.start) {
      this.start = this.end;
    }
  }
  remove() {
    if (!this.start) return;
    const removedVal = this.start.val;
    this.start = this.start.next;
    if (!this.start) {
      this.end = null;
    }
    return removedVal;
  }
  peek() {
    return this.start.val;
  }
  isEmpty() {
    return !this.start;
  }
}

class QueueNode {
  constructor(val, next) {
    this.val = val === undefined ? null : val;
    this.next = next === undefined ? null : next;
  }
}

const arrayToQueue = (arr) => {
  const queue = new Queue();
  for (const el of arr) {
    queue.add(el);
  }
  return queue;
};

describe(`${module.filename} - Stack`, () => {
  it("should create a stack and perform stack methods correctly", () => {
    const arr = [1, 2, 3, 4, 5];
    const stack = arrayToStack(arr);
    assert.strictEqual(stack.peek(), 5);
    assert.strictEqual(stack.pop(), 5);
    assert.strictEqual(stack.peek(), 4);
    assert.ok(!stack.isEmpty());
    assert.strictEqual(stack.pop(), 4);
    assert.strictEqual(stack.pop(), 3);
    assert.strictEqual(stack.pop(), 2);
    assert.strictEqual(stack.pop(), 1);
    assert.ok(stack.isEmpty());
    stack.push(10);
    assert.strictEqual(stack.peek(), 10);
  });
  it("should create a queue and perform queue methods correctly", () => {
    const arr = [1, 2, 3, 4, 5];
    const queue = arrayToQueue(arr);
    assert.strictEqual(queue.peek(), 1);
    assert.strictEqual(queue.remove(), 1);
    assert.strictEqual(queue.peek(), 2);
    assert.ok(!queue.isEmpty());
    assert.strictEqual(queue.remove(), 2);
    assert.strictEqual(queue.remove(), 3);
    assert.strictEqual(queue.remove(), 4);
    assert.strictEqual(queue.remove(), 5);
    assert.ok(queue.isEmpty());
    queue.add(10);
    assert.strictEqual(queue.peek(), 10);
  });
});

module.exports = { arrayToQueue, arrayToStack, Queue, Stack };
