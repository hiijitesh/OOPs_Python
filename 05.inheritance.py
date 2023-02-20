class Employee:
    '''
1. What is inheritence?
It is a method that allows us to create a new class that shares the same attributes and method with the original function, and add some extra functionality to the new class . It also does not disturb the original class.

2. How to make a class inherit from another class ?
class Developer(Employee):

3. Structure of classes and subclasses.
When we input a function to a subclass, python follows the 'method resolution order', which is the chain of classes that it goes through to find what the method is . All classes have the built-in group of methods and attributes as their primary order.


4. How to initiate the subclass so that it can handle more information than its original class can?
There are 2 ways.
first, using the super method as follows and pass in the arguments in interest.
super.__init__()

Second, call the parent's init method explicitly and pass in the arguments in interest.
Employee.init(self, first, last, )

5. Useful tools when exploring the inheritance system.
.isinstance(instance, class )
This method returns the boolean value of whether an instance belongs to a calss
.issubclass(subclass, class )
This method returns the boolean value of whether a class has inherited from the second class .

6. Example of class inheritance
Whisky library

++ when setting a default value for an ungiven argument, avoid using an empty mutable data type. That's a topic for another video.
'''

    raise_amount = 1.04
    company = 'Twitter'

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@' + self.company + '.com'

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, programming_language):
        super().__init__(first_name, last_name, pay)
        self.programming_language = programming_language


class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employee_list=None):
        super().__init__(first_name, last_name, pay)
        if employee_list is None:
            self.employee_list = []
        else:
            self.employee_list = employee_list

    def add_emp(self, emp=None):
        if emp not in self.employee_list:
            self.employee_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee_list:
            self.employee_list.remove(emp)

    def show_all_emps(self):
        for emp in self.employee_list:
            print('-->>', emp.full_name())


dev_1 = Developer("Jitesh", "Kumar", 50000, "Python")
dev_2 = Developer("Rahul", "Bharti", 60000, "Java")
dev_3 = Developer("Sunny", "Ranjan", 70000, "C++")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_2])
'''mgr_1.add_emp(dev_1)
mgr_1.remove_emp(dev_2)

mgr_1.show_all_emps()'''

# checking subclass and instance
print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Developer))

 
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_2.programming_language)
# print(dev_1.programming_language)


# GET INFO ABOUT ANY CLASS OR METHODS
# print(help(Developer))
'''
Help on class Developer in module __main__:

class Developer(Employee)
 |  Developer(first_name, last_name, pay)
 |
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
 |
 |  Methods inherited from Employee:
 |
 |  __init__(self, first_name, last_name, pay)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  apply_raise(self)
 |
 |  full_name(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Employee:
 |
 |  raise_amount = 1.04

'''
