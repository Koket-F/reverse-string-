
class stack:
    def __init__(self):
       
       self.items=[]
    def push(self,item):
     return self.items.append(item)  
    def pop(self):
       return self.items.pop()
    def is_empty(self):
     return not self.items
    def size(self):
       return len(self.items)
    def top(self):
       return self.items[-1]
    def __str__(self):
       return str(self.items)
if __name__== '__main__':
   s= stack()
def reverse_string(string):
    
   normal = stack()
   reverse = ''
   for char in string:
       normal.push(char)
    
    
    
   while normal.size()>0:
     reverse+= normal.pop()
     
     
     
    
   return reverse  
    


print(reverse_string('abiy'))
