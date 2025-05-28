class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    

class LinkedList:
    def __init__(self):  
        self.head=None
    
    def listprint(self):
        printaval=self.head
        while printaval is not None:
            print(printaval.data)
            printaval = printaval.next
    def _inset_at_Begining_(self,newdata):
        newNode= Node(newdata)
        newNode.next=self.head
        self.head=newNode
    


l1=LinkedList()
l1.head=Node("Toyota")
l2=Node("BMW")
l3=Node("Audi")
l4=Node("Lambogini")
l1.head.next=l2
l2.next=l3
l3.next=l4

l1.listprint()
print("")
l1._inset_at_Begining("benz")
l1.listprint()
l1._inset_at_Begining("chr")
print("")
l1.listprint()