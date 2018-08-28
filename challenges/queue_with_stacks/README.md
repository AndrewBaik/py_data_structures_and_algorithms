# Queue with Stacks

## Summary
- Implement the class Queue and define methods `enqueue(value)` and `dequeue()` with only using two stacks and given `pop()` `push(value)`.

## Solution
Enqueue
- Push into stack1 and only stack1
- Reassigned self.front and self.rear
- Increment self._length

Dequeue
- Validated if stack1 or stack2 is empty
- Validated if stack2 is filled, pop out of stack2, return the popped value
- Increment each Node in stack1 and popped out of stack1 and pushed into stack2. Then pop out the last Node in stack1 without pushing back to stack2, but return its value.

## Whiteboard
![Whiteboard 1](../../assets/queue_with_stacks1.jpg)
![Whiteboard 2](../../assets/queue_with_stacks2.jpg)
