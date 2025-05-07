# This is a linked based queue, data will be wrapped into node
# Use front and rear pointers

from node import Node

class MyQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    # This method adds to the rear of a Queue
    """# Note: Recall Queue is FIFO, such as a line at the post office or bank etc."""
    def enQueue(self, data):

        # Initializes new data wrapped into Node to enqueue
        n_node = Node(data)

        # If rear pointer is not null (meaning Queue not empty)
        if self.rear:
            self.rear.next = n_node     # Rear next pointer points to new node
            self.rear = n_node          # Rear pointer points to new node
            print(f'Node ({n_node}) added to queue')

        # Else if rear pointer not null (Queue is empty)
        else:
            self.front = n_node     # Both the front & rear pointers direct to the new node
            self.rear = n_node
            print(f'First node ({n_node}) in Queue has been initialized')


    # This method removes the front of a Queue
    """# Note: Recall Queue is FIFO, meaning first come first serve"""
    def deQueue(self):

        # If front pointer is null (meaning Queue is empty)
        if self.front is None:
            # Notify User & return None
            print(f'Error: No node to dequeue')
            return None

        # Else, assign an index identifier to the data in front pointer, using the Node() class getter method
        index = self.front.get_data()
        # Traverse the Queue to next element
        self.front = self.front.next

        # Notify user Node has been removed & return the index
        print(f'Node ({index}) has been removed!')
        return index

    def isEmpty(self):

        # If a front and rear pointer exist for the Queue
        if self.front == self.rear and self.front:
            # Queue is not empty
            print(f'Queue is not empty')
            return False

        # Else list is empty, returns True
        else:
            print(f'Queue is empty')
            return True

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        current = self.front
        print("Queue contents:")
        while current:
            print(current.get_data(), end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":

    # Creates a queue
    queue1 = MyQueue()

    print(f'----------------------Enqueue Test-----------------------------')
    queue1.enQueue(10)
    queue1.enQueue(100)

    print(f'----------------------Display Test------------------------------')
    queue1.display()

    print(f'----------------------Deque Test--------------------------------')
    queue1.deQueue()
    queue1.deQueue()
    queue1.deQueue()

    print(f'----------------------isEmpty Test------------------------------')
    queue1.isEmpty()

    queue1.enQueue('SUCCESS')
    queue1.isEmpty()




