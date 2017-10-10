def calBMI(w,h):
    bmi = w/pow(h,2)
    return bmi


w = float(input("Enter weight : "))
h = float(input("Enter height : "))
print(calBMI(w,h))

