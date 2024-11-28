def sim_toolkit():
    while True:
        print("\n SIM 1")
        print("1. Safaricom")
        print("2. M_PESA")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("You selected Safaricom.")
        elif choice == "2":
            while True:
                print("\n SIM 1 - M_PESA")
                print("1. Send Money")
                print("2. Withdraw Cash")
                print("3. Buy Airtime")
                print("4. Loans and Savings")
                print("5. Lipa na M_PESA")
                print("6. My Account")
                print("0. Back")
                mpesa_choice = input("Enter your choice: ")

                if mpesa_choice == "1":
                    while True:
                        phone = input("Enter Phone Number (10-13 digits): ")
                        if phone.isdigit() and 10 <= len(phone) <= 13:
                            print(f"Phone number {phone} validated.")
                            break
                        else:
                            print("Invalid phone number. Try again.")
                    break
                elif mpesa_choice == "0":
                    break
                else:
                    print("Invalid choice. Try again.")
        elif choice == "0":
            print("Exiting SIM Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


sim_toolkit()



















































# `print("""
# SIM 2

# Safaricom+
# M-PESA
# """)
# choice1 = int( input("Enter your choice : ") )

# def safaricom():
#     print("""
#     SIM 2

# 1. M-Banking services
# 2. My Account
# """)
# def m_pesa():
#     print("""
#     SIM 2

# 1. Send Money
# 2. Withdraw Cash
# 3. Buy Airtime
# 4. Lipa na M-PESA
# """)
# mpesa_choice = int( input("Enter your choice") )
# if choice1==2:
#     m_pesa()

# elif choice1==1:
#     safaricom()
# `