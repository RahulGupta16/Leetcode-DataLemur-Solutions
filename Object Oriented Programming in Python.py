
"""  Python Object-Oriented Programming

Source:- https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2


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

print(employee.fullname(empl1)) # IN THIS WAY ALSO WE CAN ACCESS THE METHOD. IN THIS, WE HAVE USED CLASS NAME AND THE METHOD TO BE EXECUTED AND WITHIN THE ARGUMENT OF THAT METHOD
                                # WE HAVE PROVIDED INSTANCE NAME (like 'empl1' here).



###________________________________________________________________________________________________________________________________

""" INSTANCE VARIABLES VS CLASS VARIABLES

## Instance variables are used for data that is unique to each instance. These are set using 'self' argument. For eg. self.first_name, self.last_name these are set for each instance of each employee we create.

## Class variables are variables that are shared among all instances of a class. Class variables are same foe each instance."""

## Eg.

class employee:

    raise_amount = 1.04   # Created a class variable
    num_of_emps = 0       # Created another class variable for counting the number of instances

    def __init__(self,pay):
        self.pay = pay
        employee.num_of_emps += 1  ## Since everytime this __init__() method gets executed as we create new instances.
        ## Therefore, for each instance num_of_emps attribute must be incremented by 1 

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount   ## or we can apply "employee.raise_amount"
        ## Whenever we access the class variable,we need to access them either from class itself or an instance of the class
e1 = employee(50000)
e2 = employee(60000)

        ## Now if we print the raise_amount as:
print(employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)

## Then we'll be getting the output as:-
#> 1.04
#> 1.04
#> 1.04

## Now if we modify the raise_amount variable to 1.05 as :-

employee.raise_amount = 1.05
# and now if I again print raise_amount :-
print(employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)

## Then we'll be getting the output as:-
#> 1.05
#> 1.05
#> 1.05

## So we found that it changed the value of raise_amount variable for class and all of the instance.

## If we set the value of raise_amount variable by using instance instead of using a class. This will be done as:-

e1.raise_amount = 1.05
# and now if I again print raise_amount :-
print(employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)

## Then we'll be getting the output as:-
#> 1.04
#> 1.05
#> 1.04     ## Since we didn't set the raise_amount value equal to 1.05 to instance e2 therefore it is 1.04 by default

## Now lets display the no. of instances created
print(employee.num_of_emps)

###__________________________________________________________________________________________________________________________________

""" Regular methods, Class methods and Static methods

Regular methods automatically take instance as its first argument and by convention we call it 'self'.

In order to take class as its first argument, we use class methods. This begins by adding a DECORATOR '@classmethod' on top of any method to work as a class method."""

## For example:-

class Employee:
    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  ## Created one decorator '@classmethod' and making below method as class method. This alters the method as it will receive class as first argument
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount    # this is same as we assign Employee.raise_amount = 1.05


emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Test','Employee',60000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

## This will give us output as:-
# 1.04
# 1.04
# 1.04

## for modifying the class variable 'raise_amount', either we can do :-
Employee.set_raise_amount(1.05)
# and now if we execute print(Employee.raise_amount), print(emp1.raise_amount) and print(emp2.raise_amount), we'll get the output as :-
# 1.05
# 1.05
# 1.05

### RUNNING CLASS METHODS FROM INSTANCES

## If i do :-
emp1.set_raise_amount(1.05)

#And now if I execute :-
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# Then we'll get the output as:-
# 1.05
# 1.05
# 1.05

"""Class methods can be used as an alternative constuctor"""

# For examplve, we have one string consisting of name and pay separated with '-' as 'Corey-Schafer-50000', then either we can separate them 
# using .split() method outside the class while creating instances.
# 
# But here we are focussing on using class methods to work as an alternative constructor or 
# we can say it will allow us to create instances using class methods without declaring instaces outside the class:-
class Employee:
    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

#________________________________________________________________________________________________________________
# Declaring static method
#       
# Static method don't pass instance or class in their argument automatically. They behave just like a regular method
# except we include them in classes because they have some logical connection with the class.
# 
# The decorator used for static method is '@staticmethod'
# For eg. lets say we want to get check whether the weekday is Sunday (0) or Saturday(6)                                                                                                          |
    
    @staticmethod
    def is_weekday(day):
        if(day.weekday()==0 or day.weekday()==6):
            return True
        return False
#___________________________________________________________________________________________________________________                                                                                                                |

    @classmethod  
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount    

    @classmethod
    def from_string(cls, strings):
        first, last, pay = strings.split('-')
        return cls(first, last, pay)        # This line create a new instance (or object) and will return values so that this instance get received


## Now we can simply run it as :-

emp1 = Employee.from_string('Corey-Schafer-50000')

## And now if I print email and pay
print(emp1.email)
print(emp1.pay)

## We'll get the output as:- 
# Corey.Schafer@email.com
# 50000

## Executing static method

import datetime
my_date = datetime.date(2016,7,10)
print(Employee.is_weekday(my_date))

# We'll get the output as:-
True