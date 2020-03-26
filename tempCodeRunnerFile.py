class Student:

    def __init__(self, first_name, last_name, hobbies, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies
        self.subject = subject


john = Student(first_name='John', last_name='Doe', hobbies='reading', subject='Computer Science')
budi = Student(first_name='Budi', last_name= 'Smith', hobbies='programming', subject='Math')

print(john)
print(budi)

