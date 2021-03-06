# Mit Chan
# UC Innovation Take Home
# Question 1

import sys
import unittest

class TestArray(unittest.TestCase):

    def test_constructor(self):
        temp = Array()
        self.assertEqual(temp.max_size, 100)
        self.assertEqual(temp.arr, [None] * 100)

    def test_push(self):
        temp = Array()
        temp.push(50)
        temp.push(40)
        self.assertEqual(temp.arr[0], 50)
        self.assertEqual(temp.arr[1], 40)

    def test_pop(self):
        temp = Array()
        temp.push(1000)
        temp.push(500)
        self.assertEqual(temp.pop(), 500)
        self.assertEqual(temp.pop(), 1000)

    def test_empty_pop(self):
        temp = Array()
        with self.assertRaises(SystemExit):
            temp.pop()

    def test_stack_overflow(self):
        temp = Array()
        with self.assertRaises(SystemExit):
            for i in range(101):
                temp.push(i)

    def test_enqueue(self):
        temp = Array()
        temp.enqueue(1)
        temp.enqueue(2)
        self.assertEqual(temp.arr[99], 1)
        self.assertEqual(temp.arr[98], 2)

    def test_empty_dequeue(self):
        temp = Array()
        with self.assertRaises(SystemExit):
            temp.dequeue()

    def test_dequeue(self):
        temp = Array()
        temp.enqueue(500)
        temp.enqueue(1000)
        self.assertEqual(temp.dequeue(), 500)
        self.assertEqual(temp.dequeue(), 1000)

    def test_queue_underflow(self):
        temp = Array()
        with self.assertRaises(SystemExit):
            for i in range(101):
                temp.enqueue(i)

class Array:
    """
    Assume that an array stores integers and has a maximum size of 100. One array is
    used to store two distinct data structures, BOTH a queue and a stack.
    - Write a function that pushes an integer into the stack.
    - Write a function that pops an integer from the stack.
    - Write a function that enqueues an integer into the queue.
    - Write a function that dequeues an integer from the queue.

    Assumptions: 
    - the stack / queue data structure focus on pop/push and enqueue/dequeue operations
    - n = 100, n = len(array) 
    - Extra memory can be used to use another stack to implement efficient queue operations.
    - The assumption above led to me using the variable self._queue, which uses extra memory 
    in order to efficiently implement the queue function dequeue() in an amoritized constant time complexity.
    """

    def __init__(self, max_size = 100):
        self.arr = [None] * max_size
        self._queue = []

        self.max_size = 100
        self._top = -1
        self._front = max_size

    def push(self, val):
        """
        type val : int
        rtype : None
        Stack function: Pushes an integer into the stack.
        """

        # Check for overflow into queue
        if self._top == self._front-1:
            print("Stack overflow into queue data structure.")
            sys.exit(0)

        # Update stack pointer position
        # Update last inputted value into stack
        else:
            self._top += 1
            self.arr[self._top] = val

    def pop(self):
        """
        rtype : int
        Stack function: Pops an integer from the stack and returns it.
        """

        retval = None

        # Check if stack contains elements
        if self._top == -1:
            print("No elements found in the stack.")
            sys.exit(0)
        
        # Set return value equal to current stack pointer element
        # Set current stack point element to None
        else:
           retval = self.arr[self._top]
           self._top -= 1 

        # Return stack's top element.
        return retval

    def enqueue(self, val):
       """
       type val : int
       rtype : None
       Queue function: Enqueues an integer into the queue.
       """ 

       # Check for overflow into stack
       if self._front == self._top + 1:
           print("Queue overflow into stack data structure.")
           sys.exit(0)

       else:
           self._front -= 1
           self.arr[self._front] = val

    def dequeue(self):
        """
        rtype : int
        Queue function: Dequeues an integer from the queue.
        Uses another array to achieve an amoritized time complexity of O(1)
        """

        retval = None

        # Check if there's any elements remaining in the pseudo queue
        # Then check if the queue pointer is at the initial point.
        if len(self._queue) == 0 and self._front == self.max_size:
            print("No elements found in the queue.")
            sys.exit(0)

        # If the pseudo queue is empty,
        # Dequeue every element from the array data structure and append it to the 
        # pseudo queue (which functions as a stack)

        # Use the temp stack as a pseudo queue anytime dequeue() is called.
        else:
            if len(self._queue) == 0:
                while self._front < self.max_size:
                    # print(self.arr[self._front])
                    self._queue.append(self.arr[self._front])
                    self.arr[self._front] = None
                    self._front += 1

            # print(self._queue)
            
            retval = self._queue.pop()
            return retval
            


if __name__ == "__main__":
    unittest.main()