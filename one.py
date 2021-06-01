#one.py
operation = ""
print(chr(27) + "[2J")

while operation != "5": 

   # print(chr(27) + "[2J")
   
    print("1. Addition")
    print("2. Subtraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Exit ")
    operation = input("Enter your option: ")
    
    if operation != "5":
        first_number=float(input("First Number:  "))
        second_number=float(input("Second Number:  "))
        
        if operation == "1":
            sum = first_number + second_number
            print (str(first_number) + " + " + str(second_number) + " = " + str(sum))
        elif operation == "2":
            diff = first_number - second_number
            print (str(first_number) + " - " + str(second_number) + " = " + str(diff))
        elif operation == "3":
            multi = first_number * second_number
            print (str(first_number) + " * " + str(second_number) + " = " + str(multi))
        elif operation == "4":

            if second_number == 0:
                print ("Cannot divide by zero.")
            else: 
                divi = first_number / second_number
                print (str(first_number) + " / " + str(second_number) + " = " + str(divi))
        else:
            print ("Invalid operation ")