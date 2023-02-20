import datetime


class Employee:

    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, company, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.pay = pay
        self.email = first_name + '.' + last_name + '@' + company + '.com'

        # incrementing the number of employee globally
        Employee.num_of_emps += 1

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def form_string(cls, emp_str):
        first_name, last_name, pay, company = emp_str.split('-')
        return cls(first_name, last_name, company, pay)

    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False

        return True


'''
As we know that
1. Regular method under the automatically Class pass the 'class -instance' as first argument. which is called 'self'
2. class method automatically pass the 'class' itself (cls) as first argument.
3. Static method don't pass anything automatically so they behave like normal function

'''

# create the object of Employee class
emp_1 = Employee("Jitesh", "Kumar", 'zomato', 50000)
emp_2 = Employee("Rahul", "Sharma", 'twitter', 60000)
emp_3 = Employee("Rajnish", "Pandey", 'ola', 80000)


my_date = datetime.date(2023, 1, 22)
print(Employee.is_working_day(my_date))


'''
Summary:
In this video, Corey distinguishes between a regular method, class method, and a static method.


Firstly, a regular method is the type of method that we are used to seeing since the start of OOP tutorials. It is accessible through both the class and the instance, which means that we can call for the method in both
Employee.method()
and
emp_1.method()
they automatically have the instance as the first positional argument, as self.


Secondly, class methods are the type of method used when a method is not really about an instance of a class, but the class itself. To create a class method, just add '@classmethod' a line before creating the class method. The class is automatically the first argument to be passed in, and is represented as 'cls' instead of 'class'. This is because 'class' is already assigned to be something else in Python. There are 2 ways of using the class method as far as Corey has shown.


First is modifying the class variable. Corey modified the 'raise_amount' class variable using a class method. Just remember that to access a class variable, we have to write 'cls.' before specifying the actual name. For example, as 'cls.raise_amount' as in the video.


Second is making an alternative constructor. Sometimes people have information of their specific instances of the class available in a specific format. Corey shows an example of this where first and last names and pay are separated by a hyphen. Corey creates a class method that returns the class with the specific values passed in that are obtained by using split() method to the string passed in. User of the script can now automatically create a new instance without having to parse the string at '-'.


Corey then moves on to cover static methods. Static methods are different from regular methods an class methods in that it doesn't have a class or instance that is automatically passed in as a firs positional argument. They can be created by adding '@staticmethod' a line before defining the method. These are methods that have a logical connection to the Class, but does not need a class or instance as an argument. Corey says that it is better to make sure we create a static method rather then class or regular method when we are sure that we don't make use of the class or instance within the method.

'''
