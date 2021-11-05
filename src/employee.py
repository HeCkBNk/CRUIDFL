class Employee:

    count = 1

    def __init__(self, name, email, phone):
        self.id = Employee.count
        self.name = name
        self.email = email
        self.phone = phone

        Employee.count += 1
