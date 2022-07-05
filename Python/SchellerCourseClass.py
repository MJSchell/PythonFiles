class Course:
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return self.name
    
math= Course('Algebra')
print(math)