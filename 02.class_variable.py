class Employee:

    '''class variable are shared among the all instance variable of the class
     while instance varibale or method variables are uniques with each instance of class i.e object of the class
     '''

    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, company, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.pay = pay
        self.email = first_name + '.' + last_name + '@' + company + '.com'

        '''incrementing the number of employee globally so this increment will work for the every instance of the class object, if we would use self.num_of_emps +=1 then it will only increment the number of emp for the particular instance of the class'''
        Employee.num_of_emps += 1

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# create the object of Employee class
emp_1 = Employee("Jitesh", "Kumar", 'zomato', 50000)
emp_2 = Employee("Rahul", "Sharma", 'twitter', 60000)
emp_3 = Employee("Rajnish", "Pandey", 'ola', 80000)

# trying to print pay after applying  apply_raise() method
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# # we cannot find raise_amount here
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
# # 1.04
# # 1.04
# # 1.04


# # printing namespace of every obejct so that we can see all those variable which accessible to all the methods
# print(emp_1.__dict__)
'''
{'first_name': 'Jitesh', 'last_name': 'Kumar', 'company': 'Zomato', 'pay': 50000, 'email': 'Jitesh.Kumar@Zomato.com'}

we can see that there is no 'raise_amount' varibale in emp1 object
'''

# print(Employee.__dict__)
'''
{'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x00000229DE68B1C0>, 'full_name':
<function Employee.full_name at 0x00000229DE68B250>, 'apply_raise': <function Employee.apply_raise at 0x00000229DE68B2E0>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}

# so there is 'raise_amount :1.04 ' attributes in 'Employee' class
'''

# change the raise_amount using class

# Employee.raise_amount = 1.07
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
'''
we changed the raise_amount to 1.07 and it is accesible to the all the object of class as well as 'Employee' class
so the change take place globally in the class
1.07
1.07
1.07
'''

# change the raise_amount using class instance(yeah its actually obejct)
emp_1.raise_amount = 1.09
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
'''
so it only changed the raise_amount of emp_1 obejct
1.09 ->raise_amount of emp_1
1.04
1.04
'''

# print(emp_1.__dict__)
'''
{'first_name': 'Jitesh', 'last_name': 'Kumar', 'company': 'zomato',
    'pay': 50000, 'email': 'Jitesh.Kumar@zomato.com', 'raise_amount': 1.09}
'''
# so now there is 'raise_amount': 1.09 avialable


# Check number of employees
print(Employee.num_of_emps)


# Summary
'''
Summary:

In this video, Corey taught as how to differentiate between a Class variable and instance variable, how they are related to each, other, and when each of them is more useful over the other.

Class variables are variables that we set inside a class , and are shared among all instances. Corey gave a good example where the number of total employs should be the same to every employ, no matter which employee we are referring to. Therefore,

emp_1.num_of_employ = emp_2.num_of_employ = Employee.num_of_employ

Instance variables are variables that are different from each instance. For example, the names and the pay for each employee. They have to be different.

Corey also shows that class variables and instance variables are closely related, and that class variables are kind of 'inherited' to the 'self' variables. To illustrate this, Corey shows an example of 'annual raise of pay'. He initially creates the class variable to show a case where annual raise is equal among all the employees. This variable of 1.04 was accessible through each instance, and also through the class itself(obiviously). That is ,
print(Employee.annual_raise)
print(emp_1.annual_raise)
print(emp_2.anual_rais)
all printed out 1.04.


However, using the ._dict__  thing, Corey shows that the intances, emp_1 and emp_2 does not contain the annual_raise value. Corey explains that if a variable is not found within an instance and programmers try to access the variable, python automatically looks in in the variable of the instance's class, and then the more classes that the instance's class inherits from .


Furthermore, if we access the class variable through an instance and then change it, python creates the variable within the instance. We can check it by using the ._dict_ thing. Corey shows that annual_raise key was created when he manually changed the annual_raise value as 1.05 in the following way.
emp_1.annual_raise = 1.05
however, we know that the class variable remained the same at 1.04, when printing the class variable.
print(Employee.annual_raise)
'''
