

def print2DMatrix(arr):
    for row in arr:
        print(' '.join([str(elem) for elem in row]))


# function that display multiplication table
# precondition: m and n are positive ints
# postcondition: mult. table of size m x n is printed 
def multTable(m,n):
    list1= [[i*j for j in range(m)] for i in range(n)]
    for row in list1:
        print(' '.join([str(elem) for elem in row]))
        
multTable(10, 8)

y = [[12,7,3],[4,5,6],[8,1,4]]
    
x =[[1,5,2],
    [5,9,3],
    [6,8,9]]
    
#check
def addMatrices(a,b):
   
    
    c= [[0 for j in range(len(a[0]))] for i in range(len(a))]
    
    for row in range(len(a)):
        for col in range(len(a[0])):
            c=[row][col] = a[row][col] + b[row][col]
      
    print2DMatrix(c)

addMatrices(x, y) 


#prints 2D matrices with it being transposed
def transposeMatrice():
    a= [[1,5,2],
        [3,4,6]]
    
    #c = [[0,0],
         #[0,0],
         #[0,0]]            # the line down below will create the list that looks like this. (47).           
    c = [[0 for j in range(len(a))] for i in range(len(a[0]))]
    for row in range (len(c)):
        for col in range(len(c[0])):
            c[row][col] = a[col][row]
            
    print (c)
            
#transposeMatrice()



def belowLineAbove():
    a = [[0,1,2,3,4],
         [3,4,5,6,7],
         [6,2,5,7,8],
         [2,3,9,1,2],
         [4,6,7,2,9]]
    
    result = [[0 for j in range(len(a))] for i in range(len(a))]
    print(result)
    for row in range(result):
        for col in range(result):
            if(row<col):
                result[row[col]]= 1
            elif(row>col):
                a[row][col] = 2
            else:
                a[row][col]= 0
    print(a)

belowLineAbove()
            