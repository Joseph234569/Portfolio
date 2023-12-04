# Define a class named 'employee'

class employee:
    def __init__(self, name, email, pay):
        self.make = name
        self.email = email
        self.pay = pay
    def get_info(self):
        return f"{self.name} {self.email} {self.pay}"




