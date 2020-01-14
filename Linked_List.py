class Node(object) :
    def __init__(self, value) :
        self.value = value
        self.next = None
    
    def getData(self) :
        return self.value
    
    def setData(self, value) :
        self.value = value
        
    def getNext(self) :
        return self.next
    
    def setNext(self, next) :
        self.next = next

class LinkedList(object) :
    def __init__(self, head = None) :
        self.head = head
        self.count = 0
        
    def getCount(self) :
        return self.count
    
    def insertNode(self, data) :
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
        self.count += 1
        
    def findNode(self, value) :
        item = self.head
        while (item != None) :
            if item.getData == value :
                return item
            else :
                item = item.getNext()
                
    def deleteIndex(self, index):
        if index > self.count - 1 :
            return
        if index == 0 :
            self.head = self.head.getNext()
        else :
            tempIndex = 0
            node = self.head
            while tempIndex < index - 1 :
                node = node.getNext()
                tempIndex += 1
            node.setNext(node.getNext().getNext())
            self.count -= 1
    
    def printSelf(self) :
        tempNode = self.head
        index = 0
        while (tempNode != None) :
            print("Node at Index",index," : ",tempNode.getData())
            tempNode = tempNode.getNext()
            index += 1
            
itemList = LinkedList()
itemList.insertNode(38)
itemList.insertNode(18)
itemList.insertNode(32)
itemList.insertNode(24)
itemList.insertNode(6)
itemList.insertNode(12)
itemList.printSelf()
print("Item count: ",itemList.getCount())
print(" \n")
itemList.deleteIndex(3)
itemList.printSelf()
print("Item count: ",itemList.getCount())
print(" \n")