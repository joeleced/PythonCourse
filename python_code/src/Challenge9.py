def student_discount(price):
    return price - (price * 0.1)

def regular_discount(price):
    return price - (price * 0.05)

def apply_discount(person,price):
    if person == 'student':
        return regular_discount(student_discount(price))

print(apply_discount('student',100))