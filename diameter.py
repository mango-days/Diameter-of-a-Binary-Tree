class Node :
    def __init__ ( self , data ) :
        self.left = None
        self.data = data
        self.right = None
        self.maxHeightNode = None

class BinaryTree :
    def __init__ ( self ) : self.root = None
    
    def insert ( self , data ) :
        if self.root == None :
            self.root = Node ( data )
            return
        
        parent = self.root
        temp = self.root
        while temp :
            parent = temp
            
            if temp == None : 
                temp = Node ( data )
                return
        
            if temp.data == data : return # data exists
        
            elif temp.data < data : 
                temp = temp.right
                if temp == None : 
                    parent.right = Node ( data )
                    return
            elif temp.data > data : 
                temp = temp.left
                if temp == None :
                    parent.left = Node ( data )
                    return

    def printList ( self , node ) :
        if node == None : return
        if node.data : print ( node.data ) #data exists
        if node.left : 
            print ( " --- L of" , node.data , ":")
            self.printList ( node.left )
        if node.right : 
            print ( " --- R of" , node.data )
            self.printList ( node.right )
        if node.maxHeightNode : print ( " --- height of" , node.data , ":" , node.maxHeightNode )
        return
    
    def height ( self , node ) :
        if node == None : return 0
        x = y = 1
        if node.left : x = x + self.height ( node.left )
        if node.right : y = y + self.height ( node.right )
        return max ( x , y )
    
    def setMaxHeightNode ( self , node ) :
        if node == None : return { "node" : 0 }
        x = y = 0
        if node.left : x += self.height ( node.left )
        if node.right : y += self.height ( node.right )
        if x > y : return { "left" : x }
        if x == y : return { "both" : x }
        else : return { "right" : y }

    def diameter ( self ) :
        if self.root == None : return
        
        temp = self.root
        while ( temp ) :
            if temp == None : return
            if temp.data : temp.maxHeightNode = self.setMaxHeightNode ( temp )
            if temp.left : temp.left.maxHeightNode = self.setMaxHeightNode ( temp.left )
            if temp.right : temp.right.maxHeightNode = self.setMaxHeightNode ( temp.right )
            if temp.maxHeightNode != None : temp = temp.right
        
        temp = self.root
        while ( temp ) :
            if temp == None : return
            if temp.data : temp.maxHeightNode = self.setMaxHeightNode ( temp )
            if temp.left : temp.left.maxHeightNode = self.setMaxHeightNode ( temp.left )
            if temp.right : temp.right.maxHeightNode = self.setMaxHeightNode ( temp.right )
            if temp.maxHeightNode != None : temp = temp.left
        return
    
    def getDiameter ( self , node ) :
        if node == None : return 0
        
        ansBoth = node.maxHeightNode.get ("both")
        ansLeft = node.maxHeightNode.get ("left")
        ansRight = node.maxHeightNode.get ("right")
        
        if ansBoth : return ( ( ansBoth * 2 ) + 1 )
        elif ansLeft : return ( ansLeft + self.getDiameter ( node.right ) )
        elif ansRight : return ( ansRight + self.getDiameter ( node.left ) )
        else : return 0
    

Obj = BinaryTree ()
arr = [ 5 , 3 , 8 , 2 , 6 , 4 , 9 , 7 , 1 ]
for index , value in enumerate ( arr ) : Obj.insert ( value )
Obj.diameter ()
#Obj.printList ( Obj.root )
print ( "Diameter of the tree is :" , Obj.getDiameter ( Obj.root ) )
