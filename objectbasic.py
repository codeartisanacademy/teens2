class Student:

    # first_name, last_name, subject, enrolled
    def __init__(self, first_name, last_name, subject, enrolled):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.enrolled = enrolled
    
    # string representation of an object
    def __str__(self):
        return self.first_name.title() + " " + self.last_name.title()

    def enroll(self):
        if self.enrolled == True:
            print('You are already enrolled')
        else:
            self.enrolled = True
            print('You are now enrolled')

# create an object of type student
john = Student(first_name='john', last_name='doe', subject='Computer Science', enrolled=False)
budi = Student(first_name='Budi', last_name= 'Smith', subject='Math', enrolled=True)

print(john)
print(budi)

print(john.enrolled)
john.enroll()
print(john.enrolled)

budi.enroll()














































'''
class Student:

    # initialization of the object
    def __init__(self, first_name, last_name, hobbies, subject, enrolled):
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies
        self.subject = subject
        self.enrolled = enrolled

    # string representation of the object
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def enroll(self):
        if not self.enrolled:
            self.enrolled = True
            print('You are enrolled now')
        else:
            print("You are already enrolled")


john = Student(first_name='John', last_name='Doe', hobbies='reading', subject='Computer Science', enrolled=True)
budi = Student(first_name='Budi', last_name= 'Smith', hobbies='programming', subject='Math', enrolled=False)

print(john)
print(budi)

john.enroll()
budi.enroll()
'''
