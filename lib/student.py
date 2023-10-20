#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [] #Initialize empty list
    
    def learn(self,expand_knowledge):
        pass
        self.knowledge.append(expand_knowledge)
        

student = Student("Robert","Green")
student.learn("Python is a versatile programming language")
print(student.knowledge)