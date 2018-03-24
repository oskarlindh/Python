class Node:
        
    element = None
        
    parent  = None 
    right   = None 
    left    = None

    def __init__(self, element):
            
        self.element = element


    def isEmpty():
        return self.element == None




class Tree:
    
    root = None
    elementCount = 0
        
        
    
    def isEmpty(self):
        return self.root == None

    def getRoot(self):
        return self.root

    def insertTree(self,node,element):
        
        comp = cmp(element,node.element)
        
        if(comp == 0): 
            return

        elif(comp < 0):
            if(node.left == None):
                
                node.left = Node(element)
                self.elementCount += 1
                node.left.parent = node
            
            else:
                self.insertTree(node.left,element)
        
        elif(comp > 0):
            if(node.right == None):
                self.elementCount += 1
                node.right = Node(element)
            else:
                self.insertTree(node.right,element)

    def insertElement(self,element):

        if(self.root == None):
            self.root = Node(element)
            self.elementCount += 1 
        else:
            self.insertTree(self.root,element)

    def treeContains(self, lookUp):

        currentNode = self.root
        comp = cmp(lookUp,currentNode.element)
      
        while(comp != 0):
        
            if(currentNode == None):
                return False


            comp = cmp(lookUp,currentNode.element)
        
            if(comp < 0):
                currentNode = currentNode.left
            
            if(comp > 0):
                currentNode = currentNode.right
        return True
    
    def treeDepth(self,node):
        
        if(node == None):
            return 0;
        else:
            return 1 + max(self.treeDepth(node.left),self.treeDepth(node.right))
    
    def depth(self):
        
        return self.treeDepth(self.root)


#Test Functions#
tree = Tree()
print(tree.isEmpty())

tree.insertElement(7)
tree.insertElement(8)
tree.insertElement(9)
tree.insertElement(10)

print(tree.treeContains(1))
print(tree.treeContains(2))
print(tree.treeContains(5))
print(tree.treeContains(0))
print("number of elements: " + str(tree.elementCount))
print(tree.depth())













