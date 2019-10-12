class Node:
    def __init__(self,val,nxt):
        self.val = val
        self.nxt = nxt  

def reverce(node):
    if not node.nxt:
        print(node.val)
        return 
    reverce(node.nxt)
    print(node.val)

n0 = Node(4,None)
n1 = Node(3,n0)
n2 = Node(2,n1)
n3 = Node(1,n2)

reverce(n3)