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
        print(t.data)
        if t.left!=None:
            print(t.left.data)
        if t.right!=None:
            print(t.right.data)
            
    def inorder(self,t):
        if t.left!=None:
            print(t.left.data)
        print(t.data)
        if t.right!=None:
            print(t.right.data)
            
    def postorder(self,t):
        if t.left!=None:
            print(t.left.data)
        if t.right!=None:
            print(t.right.data)
        print(t.data)
    
t=root()

n1=Node(10)
n2=Node(20)
n3=Node(30)

t.root=n1
n1.left=n2
n1.right=n3

t.preorder(n1)
t.inorder(n1)



    
