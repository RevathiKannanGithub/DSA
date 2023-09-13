#########################################
# Declaring Node of a Singly LinkedList #
#########################################

class Node:
  def __init__(self):
    self.data = None
    self.next = None
  def setData(self, data):
    self.data = data
  def getData(data):
    return self.data
  def setNext(self, next):
    self.next = next
  def getNext(next):
    return self.next
  def hasNext(self):
    return self.next != None
  
class Linkedlist(object):
  def __init__(self):
    self.length = 0
    self.head = None


###########################
# Traversing a Linkedlist #
###########################

def length(self):
  count = 0
  current = self.head
  while current != None:
    current = current.next
    count += 1
  return count


############################################################
# Insert a newNode in a Singly Linkedlist at the Beginning #
############################################################

def insertAtBeginning(self, data):
  newNode = Node()
  newNode.data = data
  if self.length == 0:
    self.head = newNode
  else:
    newNode.next = self.head
    self.head = newNode
  self.length += 1


###############################################################
# Insert a newNode in a Singly Linkedlist at a given position #
###############################################################

def insertNodeAtPosition(self, data, pos):
  if pos == 0 or pos > self.length:
    return None
  else:
    if pos == 0:
      insertAtBeginning(data)
    else:
      if pos == self.length:
          insertAtEnd(data)
        else:
          newNode = Node()
          newNode.data = data
          count = 1
          current = self.head
          while count < pos - 1:
            count += 1
            current = current.next
          newNode.next = current.next
          current.next = newNode
          self.length += 1


##################################################
# Deleting the first node in a Singly Linkedlist #
##################################################

def deleteFirstNode(self):
  if self.length == 0:
    print('The list is empty!')
  else:
    self.head = self.head.next
    self.length -= 1


#################################################
# Deleting the last node in a Singly Linkedlist #
#################################################

def deleteLastNode(self):
  if self.length == 0:
    print("The List is Empty")
  else:
    previousNode = self.head
    currentNode = self.head
    while currentNode.next != None:
      previousNode = currentNode
      currentNode = currentNode.next
    previousNode.next = None
    self.length += 1


#################################################
#    Deleting a Node at a particular position   #
#################################################

def deleteAtPosition(self, pos):
  count = 0
  currentNode = self.head
  previousNode = self.head
  if pos > self.length or pos > 0:
    print("The position does not exist. Please enter a valid position")
  else:
    while currentNode.next != None or count < pos:
      count += 1
      if count == pos:
        previousNode.next = currentNode.next
        self.length -= 1
        return
      else:
        previousNode = currentNode
        currentNode = currentNode.next


################################
# Deleting a Singly Linkedlist #
################################

def clear(self):
  self.head = None
