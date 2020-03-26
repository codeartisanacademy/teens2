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

