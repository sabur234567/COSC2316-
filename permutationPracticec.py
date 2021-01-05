# base cases of permutation: if its size is one element, or empty

#Description: function that returns the permutation of a given list
#pre condition: the function receives a list with size greater than one. and no repeating values
#post-condition: 
def permutation(list):
    if len(list)<=1: 
        return [list]
    
    l=[]
    
    for i in range(len(list)):
        m = list[i]
        remList = list[:i] + list[i+1:]
        
        for p in permutation(remList):
            l.append([m] + p)
            
    return l
    
print(permutation([1,2,3]))