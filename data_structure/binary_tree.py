class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def getData(self):
        return self.data

class root:
    def __init__(self):
        self.root=None
        
    def preorder(self,t):
        if t!=None:
            print(t.data)
            if t.left!=None:
                self.preorder(t.left)
            if t.right!=None:
                self.preorder(t.right)
            
    def inorder(self,t):
        if t!=None:
            if t.left!=None:
                self.preorder(t.left)
            print(t.data)
            if t.right!=None:
                self.preorder(t.right)
            
    def postorder(self,t):
        if t!=None:
            print(t.data)
            if t.left!=None:
                self.preorder(t.left)
            if t.right!=None:
                self.preorder(t.right)
            print(t.data)
    
t=root()

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

t.root=n1
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5


t.preorder(n1)
