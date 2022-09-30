# Understanding 'self' in python
# ~/Users/NicholasThompson/python_text_dir/self_test.py

#it is clearly seen that self and obj is referring to the same object
 
class check:
    def __init__(self):
        print("Address of self = ",id(self))
 
obj = check()
print("Address of class object = ",id(obj))
 
# this code is Contributed by Samyak Jain