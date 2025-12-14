# This class represents a single node of the linked list
class Node:
    def __init__(self, data):
        # Store the data value of the node
        self.data = data
        
        # Pointer to the next node (initially None)
        self.next = None


# This class represents the Linked List
class LinkedList:
    def __init__(self):
        # Head points to the first node of the linked list
        # Initially, the list is empty
        self.head = None

    # Function to insert a new node at the beginning
    def insert_at_beginning(self, data):
        # Create a new node with given data
        new_node = Node(data)

        # Link new node to the current head
        new_node.next = self.head

        # Move head to point to the new node
        self.head = new_node

    # Function to insert a new node at the end
    def insert_at_end(self, data):
        # Create a new node with given data
        new_node = Node(data)

        # If the linked list is empty
        if self.head is None:
            # Make the new node as head
            self.head = new_node
            return

        # Temporary pointer to traverse the list
        temp = self.head

        # Traverse till the last node
        while temp.next:
            temp = temp.next

        # Link the last node to the new node
        temp.next = new_node

    # Function to delete a node with a specific value
    def delete(self, key):
        # Start from the head node
        temp = self.head

        # If the node to be deleted is the head node
        if temp and temp.data == key:
            # Move head to the next node
            self.head = temp.next
            return

        # Store the previous node
        prev = None

        # Traverse the list to find the key
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If key is not present in the list
        if temp is None:
            print("Element not found")
            return

        # Unlink the node from the list
        prev.next = temp.next

    # Function to search an element in the linked list
    def search(self, key):
        # Start from the head
        temp = self.head

        # Traverse the list
        while temp:
            # If data matches the key
            if temp.data == key:
                return True
            temp = temp.next

        # Return False if element not found
        return False

    # Function to display the linked list
    def display(self):
        # Temporary pointer to traverse the list
        temp = self.head

        # Traverse until the end of the list
        while temp:
            # Print the data of the current node
            print(temp.data, end=" -> ")
            temp = temp.next

        # Indicate the end of the linked list
        print("None")


# ---------------- DRIVER CODE ----------------

# Create an empty linked list object
ll = LinkedList()

# Insert elements at the beginning
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)

# Insert elements at the end
ll.insert_at_end(30)
ll.insert_at_end(40)

# Display the linked list
ll.display()

# Search for an element
print("Search 30:", ll.search(30))

# Delete an element
ll.delete(20)

# Display the linked list after deletion
ll.display()
