class Employee:

    def __init__(self, first_name, last_name, company, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.pay = pay
        self.email = first_name + '.' + last_name + '@' + company + '.com'

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.pay})"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee("Jitesh", "Kumar", 'zomato', 50000)
emp_2 = Employee("Rahul", "Sharma", 'twitter', 60000)
# let print emp_1 then what we get
# print(emp_1)
'''
<__main__.Employee object at 0x000001F86C76BFA0>

above is the output of code line 19, so this is the builtin behavior of the pyhton
that it will return the object addres whenever we print the obejct of the class

so to change this behavier we have overloading things python oop , with the help of special methods (__method__) which is known as 'dunder'
'''
# print(emp_1)
# o/p --->  Employee(Jitesh, Kumar, 50000)

# we can also use
print(str(emp_1))
print(repr(emp_1))
'''
output -->
Jitesh Kumar - Jitesh.Kumar@zomato.com
Employee(Jitesh, Kumar, 50000)
'''

# we can directly call dunder methoda and output would be same as the above code output
print(emp_1.__repr__())
print(emp_1.__str__())

# ADD dunder method
print(2+3)  # 5
# this 2 + 3 is calling dunder method __add__() internallay
print(int.__add__(2, 5))  # o/p 7
print(str.__add__("Jit", "esh"))  # o/p Jitesh

# let add the pay of two employee using dunder __add__() method
total_pay = emp_1 + emp_2
print(total_pay)  # o/p -> 110000


# LENGTH DUNDER METHOD ON OBJECT

test_str = 'I am learning oop conecpt'
print(len(test_str))  # o/p --->> 25
print(test_str.__len__())  # o/p-->> 25

# we can also use this __len__ dunder method in class object
print(len(emp_1))  # o/p --> TypeError: object of type 'Employee' has no len()

# so there is no builtin method to get the len of object so lets create it
print(len(emp_1))  # o/p -->> 12
