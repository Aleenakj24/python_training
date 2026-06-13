class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
        
    
    def display(self):
        count,s,even=0,0,0
        temp=self.head
        while temp:
            count+=1
            s+=temp.data
            if temp.data%2==0:
                even+=temp.data
            print(temp.data,end="->")
            temp=temp.next
        print("None")
        print(count)
        print(even)
        print(s)

l1=LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.display()


# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)

# temp=head
# while temp:
#     print(temp.data,end="->")
#     temp=temp.next
# print(None)
