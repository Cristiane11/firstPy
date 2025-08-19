def calculator( choice, first_num, second_num):
    if choice == "1":
        return first_num + second_num
    elif choice == "2":
        return first_num - second_num
    elif choice == "3":
        return first_num * second_num
    elif choice == "4":
        if second_num == 0:
            return "Cannot divide by zero"
        return first_num / second_num
    elif choice == "5":
        if second_num == 0:
            return "Cannot divide by zero"
        return first_num // second_num
    else:
        return "Invalid choice"


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Floor Divide")

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
choice = input("Enter choice: ")

result = calculator(choice, first_num, second_num)
print("Result:", result)