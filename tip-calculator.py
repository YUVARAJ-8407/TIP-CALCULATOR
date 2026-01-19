print("Welcome to TIP CALCULATOR:")
print("Make sure you would only type the numbers instead of any alphabets(letter/word) which cause the device to restart")
while True:
    try:
        bill_before_tip=float(input("What was the total bill: $"))
        tip=float(input("How much tip would you like to give:"))
        people=int(input("How many people to split the bill:"))
        bill_after_tip=(bill_before_tip*tip/100)+bill_before_tip
        print(f"Total bill: ${bill_after_tip:.2f}")
        bill_spearhead= bill_after_tip / people
        print(f"Bill per person: ${bill_spearhead:.2f}")
        break
    except ZeroDivisionError:
            print("Total bill cannot be split among [0] people")
    except ValueError:
        print("You typed an invalid input")
