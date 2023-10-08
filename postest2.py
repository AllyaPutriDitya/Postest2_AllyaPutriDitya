from prettytable import PrettyTable

# Data Admin
username_admin = ("Allya Putri Ditya")
password_admin = ("2309116078")

table1 = PrettyTable()
table1.field_names = ["No", "Flowers", "price /bunch"]
table1.add_row([1, "Daisy", "Rp 30.000"])
table1.add_row([2, "Lavender", "Rp 40.000"])
table1.add_row([3, "Edelwiss", "Rp 60.000"])
table1.add_row([4, "Chrysant", "Rp 95.000"])
table1.add_row([5, "Lily", "Rp 90.000"])
table1.add_row([6, "Tulip", "Rp 50.000"])
table1.add_row([7, "Rose", "Rp 50.000"])
table1.add_row([8, "Orchid", "Rp 70.000"])
table1.add_row([9, "Poppy", "Rp 45.000"])
table1.add_row([10, "Peony", "Rp 65.000"])
table_1= str(table1)
Flower_table= table_1

table2 = PrettyTable()
table2.field_names = ["No", "Tools", "price"]
table2.add_row([1, "Shovel", "Rp 40.000"])
table2.add_row([2, "Small Flower Pot", "Rp 10.000"])
table2.add_row([3, "Medium Flower Pot", "Rp 15.000"])
table2.add_row([4, "Big Flower Pot", "Rp 25.000"])
table2.add_row([5, "Gloves", "Rp 20.000"])
table2.add_row([6, "Watering can", "Rp 20.000"])
table2.add_row([7, "Axe", "Rp 45.000"])
table2.add_row([8, "Hoe", "Rp 40.000"])
table2.add_row([9, "Wheelbarrow", "Rp 55.000"])
table2.add_row([10, "Lawn mower", "Rp 100.000"])
table2.add_row([11, "Pruners", "Rp 35.000"])
table2.add_row([12, "Boots", "Rp 30.000"])
table2.add_row([13, "Bucket", "Rp 10.000"])
table2.add_row([14, "Scarecrow", "Rp 40.000"])
table2.add_row([15, "Garden Hose", "Rp 20.000"])
table_2= str(table2)
Tools_table= table2

table3 = PrettyTable()
table3.field_names = ["No", "Seed", "price"]
table3.add_row([1, "Tomato", "Rp 30.000"])
table3.add_row([2, "Carrot", "Rp 30.000"])
table3.add_row([3, "Pumpkin", "Rp 40.000"])
table3.add_row([4, "Corn", "Rp 30.000"])
table3.add_row([5, "Onions", "Rp 30.000"])
table3.add_row([6, "Chili", "Rp 50.000"])
table3.add_row([7, "Cabbage", "Rp 35.000"])
table3.add_row([8, "Long Bean", "Rp 20.000"])
table3.add_row([9, "Potato", "Rp 30.000"])
table3.add_row([10, "Star Fruit", "Rp 55.000"])
table_3= str(table3)
Seed_table= table3

while True :
    print("==========Garden Shop==========")
    print("\n1. Seller\n2. Buyer\n3. Exit")
    enter_option = input("Please enter number option : ")
        
    if enter_option == "1":
        while True:
            print("\n==========LOGIN==========")
            Username = input(f"Name : ")
            Password = input(f"Password: ")

            if Username == username_admin and Password == password_admin:
                break
            else:
                print("Login failed, try again")
            
        while True:
            print(f"\nWelcome, Admin\n")
            print("1. Total Payment (+tax)\n2. Item List\n3. Change menu\n4. Delete\n5. Back")
            option = input("Choose an option : ")

            if option == "1":
                print("\nTotal Payment\n")
                item = str(input("\nItem name : "))
                amount = int(input("Amount : "))
                price = int(input("Item price : "))
                tax = 0.12
                service_program = 2.000
                total = price*amount+(price*tax)+service_program
                print (f"Total Payment is", {total})
                choice = (input("Still in here? (Yes/No): "))
                if choice == "Yes":
                    print (f"Okay")
                else:
                    choice == "No"

            elif option == "2":
                print("\n==========Item List==========")
                print("1. Flowers\n2. Planting tools\n3. Seeds\n4. Exit")
                number = input("Enter the list numbers you want to see : ")

                if number == "1":
                    print(Flower_table)
                    choice = (input("Still in here? (Yes/No): "))
                    if choice == "Yes":
                        print (f"Okay")
                    else:
                        choice == "No"
                                
                elif number == "2":
                    print(Tools_table)
                    choice = (input("Still in here? (Yes/No): "))
                    if choice == "Yes":
                        print ("Okay")
                    else:
                        choice == "No" 

                elif number == "3":
                    print(Seed_table)
                    choice = (input("Still in here? (Yes/No): "))
                    if choice == "Yes":
                        print ("Okay")
                    else:
                        choice == "No"

                else: 
                    number == "4"
                            
            elif option == "3":
                print("==========Change Menu==========")
                print("1. Flowers\n2. Planting tools\n3. Seeds\n4. Exit")
                number = input("Enter the list numbers you want to see : ")

                if number == "1":
                    print(Flower_table)
                    section = input("Section (item name) to update: ")
                    new_data = input("Enter the new data for the row (e.g., '4, Lily, Rp 80.000'): ")
                    rows = table1.get_string(start=0, end=11)  
                    rows = rows.split("\n")  
                    for i, row in enumerate(rows):
                        if section in row:
                            row_index = i - 2 
                    rows[row_index + 2] = f"| {new_data} |"
                    updated_flower_table = "\n".join(rows)
                    print("Result after update:")
                    print(updated_flower_table)
                    table1 = updated_flower_table  
                    choice = (input("Still in here? (Yes/No): "))
                    if choice == "Yes":
                        print ("Okay")
                    else:
                        choice == "No"

                elif number == "2":
                    print(Tools_table)
                    section = input("Section (item name) to update: ")
                    new_data = input("Enter the new data for the row (e.g., '4, Lily, Rp 80.000'): ")
                    rows = table2.get_string(start=0, end=11) 
                    rows = rows.split("\n")  
                    for i, row in enumerate(rows):
                        if section in row:
                            row_index = i - 2 
                    rows[row_index + 2] = f"| {new_data} |"
                    updated_flower_table = "\n".join(rows)
                    print("Result after update:")
                    print(updated_flower_table)
                    table1 = updated_flower_table 
                    choice = (input("Still in here? (Yes/No): "))
                    if choice == "Yes":
                        print ("Okay")
                    else:
                        choice == "No"


                elif number == "3":
                    print(Seed_table)
                    section = input("Section (item name) to update: ")
                    new_data = input("Enter the new data for the row (e.g., '4, Lily, Rp 80.000'): ")
                    rows = table2.get_string(start=0, end=11) 
                    rows = rows.split("\n")  
                    for i, row in enumerate(rows):
                        if section in row:
                            row_index = i - 2 
                    rows[row_index + 2] = f"| {new_data} |"
                    updated_flower_table = "\n".join(rows)
                    print("Result after update:")
                    print(updated_flower_table)
                    table1 = updated_flower_table 
                    choice = (input("Still in here? (Yes/No): "))
                    if choice == "Yes":
                        print ("Okay")
                    else:
                        choice == "No"

                else:
                    number == "4"
                    break

            elif option == "4":
                print("==========Delete Menu==========")
                print("1. Flowers\n2. Planting tools\n3. Seeds\n4. Exit")
                number = input("Enter the list numbers you want to see : ")

                if number == "1":
                    print(Flower_table)
                    index_to_remove = int(input("The row you want to delete : "))
                    table1.del_row(index_to_remove)
                    for i, row in enumerate(table1._rows):
                        row[0] = i + 1
                    print("\nTable Update:")
                    print(table1)
                    choice = (input("Still in here? (Yes/No): "))
                    if choice == "Yes":
                        print ("Okay")
                    else:
                        choice == "No"
                
                elif number == "2":
                    print(Tools_table)
                    index_to_remove = int(input("The row you want to delete : "))
                    table2.del_row(index_to_remove)
                    for i, row in enumerate(table2._rows):
                        row[0] = i + 1
                    print("\nTable Update:")
                    print(table2)
                    choice = (input("Still in here? (Yes/No): "))
                    if choice == "Yes":
                        print ("Okay")
                    else:
                        choice == "No"

                elif number == "3":
                    print(Seed_table)
                    index_to_remove = int(input("The row you want to delete : "))
                    table3.del_row(index_to_remove)
                    for i, row in enumerate(table3._rows):
                        row[0] = i + 1
                    print("\nTable Update:")
                    print(table3)
                    choice = (input("Still in here? (Yes/No): "))
                    if choice == "Yes":
                        print ("Okay")
                    else:
                        choice == "No"
                
                elif number == "4":
                    break

            elif option == "5":
                break

            else:
                print("Invalid choice. Please try again.") 

    if enter_option == "2":
        while True:
            print(f"\nHola!, welcome to Garden Shop\n")
            print("1. Flowers\n2. Planting tools\n3. Seeds\n4. Back")
            Number = input("Let's see, what do you want today? : ")

            if Number == "1":
                print(Flower_table)
                Pilihan = input("Want to buy some? (Yes/No) : ")
                if Pilihan == "Yes":
                        print("Name:\nAddress:\nWant to order:\nHow many:\nPayment method:\n")
                        print("Use this format and send your email to allya09ditya@gmail.com!")
                else:
                    Pilihan = "No"
                            
            elif Number == "2":
                print(Tools_table)
                Pilihan = input("Want to buy some? (Yes/No) : ")
                if Pilihan == "Yes":
                    print("Name:\nAddress:\nWant to order:\nHow many:\nPayment method:\n")
                    print("Use this format and send your email to allya09ditya@gmail.com!")
                else:
                    Pilihan = "No"

            elif Number == "3":
                print(Seed_table)
                Pilihan = input("Want to buy some? (Yes/No) : ")
                if Pilihan == "Yes":
                    print("Name:\nAddress:\nWant to order:\nHow many:\nPayment method:\n")
                    print("Use this format and send your email to allya09ditya@gmail.com!")
                else:
                    Pilihan = "No"
                        
            elif Number == "4":
                break

            else:
                print("Invalid choice. Please try again.")
    else : 
        break