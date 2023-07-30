class Class:
    class_var = 1
    
    
    def __init__(self):
        self.instance_var = 1
        
        
    def method(self):
        pass
    
object = Class()

print('__dict__' in Class.__dict__)
print(len(object.__dict__) == len(Class.__dict__))
