class Student:
     # first_name, last_name, subject, enrolled
    def __init__(self, first_name, last_name, subject, enrolled):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.enrolled = enrolled
    
    # __str__() represents the object as a string
    def __str__(self):
        return self.first_name + " " + self.last_name

    def enroll(self):
        if self.enrolled:
            print('sudah terdaftar')
        else:
            self.enrolled = True
            print('baru saja terdaftar')

john = Student(first_name='John', last_name='Doe', subject='Politik', enrolled=True)
mike = Student(first_name='Mike', last_name='Smith', subject='Kedokteran', enrolled=False)

print(john)
