my_name = input("enter name: ")
my_age = input("enter age: ")
print(f"My name is {my_name} and I am {my_age} years old")

first_number = int(input("Enter number: "))
second_number = int(input("Enter 2nd number: "))
Operation = input("Enter type: ")
if     Operation == "+":
    print(first_number + second_number)
elif  Operation == "-":
    print(first_number - second_number)
elif Operation == "/":
    print(first_number / second_number)
elif Operation == "*":
    print(first_number * second_number)
else:
    print("Operation is not valid.")




bus_capacity = 30
people_in_bus = int(input("How many people are on the bus? "))
people_enter_bus = int(input("Enter amount of people who would like to enter the bus"))
empty_seats = bus_capacity - people_in_bus
if  bus_capacity > people_in_bus:
    print(f"There is {empty_seats} available")
else:  
    print("Bus is full")
