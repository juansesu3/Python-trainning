print("Access verification")

edad_usuario= int(input("Enter your age\n"))

if edad_usuario<18:
    print("Access denied")
elif edad_usuario>100:
    print("Invalid age")
else:
    print("Acces aproved\n")
print("The program has ended")