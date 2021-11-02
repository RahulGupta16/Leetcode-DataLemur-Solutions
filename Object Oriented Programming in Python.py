
"""  Python Object-Oriented Programming

1. Why should we even use classes?
Because it allows us to logically group our data and functions in a way that is easy to
reuse and also easy to build upon if need be.

2. Data and functions are called as attributes and methods if they are associated with any class.
"""

## Defining a class :-

class Employee:    ### format for declaring any class
## In case we want to skip a class, then we can leave the class as it is.
## For that, we would be required to write "pass" else system will throw error.
    pass

## Above is a simple class "Employee" without attributes and methods.
""" Our class is basically a blueprint for crearing instances and each employee 
    that we create using "Employee" class will be an instance of that class"""
## For example

emp_1 = Employee()
emp_2 = Employee()
## Each of these is going to be their own unique instances of the "Employee" class.

## Now if I print both these instances then,
#print(emp_1)
#print(emp_2)

## You will find that there are two unique objects and they both are having different memory locations.

""" Now lets understand Instance Variable :-

Instance variable contains data that is unique to each instance"""

## Now we could manually create instance variable for each employee by:-
emp_1.first_name = 'Corey'
emp_1.last_name = 'Schafer'
emp_1.email = 'Corey.Schafer@Company.com'
emp_1.pay = 50000

emp_2.first_name = 'Test'
emp_2.last_name = 'User'
emp_2.email = 'Test.User@Company.com'
emp_2.pay = 60000

## Right now we can see each of these two instances have attributes unique to them,
## so if I print emails of these two instances :-

#print(emp_1.email)
#print(emp_2.email)

## You will be able to see emails of two instances declared previously.
## Lets say we want to set all of these informations (First_name, last_name, email, etc. for each instance when they are created).
## So we would not want to have to manually set these variables everytime as there requires los and lots of code to write and more prone
## to error as we can see above.

""" So here comes __init__ method to fix this issue."""

class employee:

    ## declaing __init__ method
#   def __init__(self, arg1, arg2):      # This method can also be considered as a initialize (or Constructor).
                            # When we create methods within a class, they receive the instance as the firse argument.

    # By convention, we should call the instance 'self' now. After self, we can specify what other arguments that we want to accept. 
    def __init__(self, first_name, last_name, pay):

#       Within the __init__ method, we are going to set all these instance variables as:-
        self.first_name = first_name        ## It is same as "emp_1.first_name = 'Corey'" which we did earlier
        ## self.fname = first_name is also fine. self.first_name is used for easiness only.        
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.'+ last_name + '@Company.com'

    ## Now, lets say we want to perform some action and for tht we can add some methods to our class.
    ## Lets create a method to display the complete name of employee, so this is done as :-
    
    def fullname(self): ### EACH METHOD WITHIN A CLASS AUTOMATICALLY TAKES THE INSTANCE AS A FIRST ARGUMENT AND WE ARE ALWAYS GOING TO CALL THAT 'SELF'
                ## Instance is the only argument we'll need in order to create the method.

                ## IN CASE IF REMOVE 'self' FROM 'fullname(self)' method and then if we run this method then it will throw error depicting 'type error'.
                ## It can be confusing as we are not passing any argument here into 'fullname' method but the instance is getting passed automatically
        
        ## So we have to expect that instance argument is in our method and that is why we added 'self' in fullname() method.

        return ('{} {}'.format(self.first_name,self.last_name))

        ##
        
empl1 = employee('Corey','Schafer',50000)   ## These arguments are automatically passed to the __init__() method.
empl2 = employee('Test','User',60000)       ## Also 'self' argument is not needed to specify as an argument as it gets automatically assiged
#print(empl1.email)
#print(empl2.email)
print(empl1.fullname()) ## Here we accessed the 'fullname()' method...but notice that while accessing method, we are giving parathesis '()' because its not an attribute.
                        ## If we print the method as 'print(fullname)' without parenthesis '()', then it will simply display the method but not the returned value by the method.

print(employee.fullname(empl1))

