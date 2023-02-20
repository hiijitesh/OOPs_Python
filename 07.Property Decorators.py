class Employee:

    def __init__(self, first_name, last_name, company, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.pay = pay

    # making email method using @property decorator
    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@{self.company}.com"

    # make full_name as attributes
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # make setter for full name that will use full_name propert decorator
    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None


emp_1 = Employee('Jitesh', 'Kumar', 'facebook', 90000)

''' I f we change the first name of the object emp_1 then will it get changed but
email will remain same like old first_name,'''

# change the name then print the info like first_name, email etc.
#Get the name
emp_1.first_name = "Sachin"

'''
Sachin
Jitesh.Kumar@facebook.com
Sachin Kumar

so here email same as old first_name

to solve this issue we use @property decorators

one way is we can use make seprate email method but for this we have call this email() method for every object which was created eariler
'''
'''
@proerty decorator allows use to create methods but use it as like attribute(variable)
'''
# SET THE NAME
emp_1.full_name = "John Doe"
# AttributeError: can't set attribute 'full_name'

''' point 2-> here we want to change the full_name of the object so that first_name, last_name & email should also get change accordingly.

for this we have to another decorator call @setter but it will work for property only

after using setter the o/p is
John
John.Doe@facebook.com
John Doe

'''

# DELETE THE ATTRIBUTE

del emp_1.full_name

print(emp_1.first_name)
print(emp_1.email)
# print(emp_1.full_name())
print(emp_1.full_name)
