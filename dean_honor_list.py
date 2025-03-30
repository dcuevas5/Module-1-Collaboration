# Name: David Cuevas
# File: dean_honor_list.py
# Description: This code accepts student names and GPAs,
# and determines if they qualify for the Dean's List (GPA ≥ 3.5)
# or the Honor Roll (GPA ≥ 3.25). The process stops when the
# last name 'ZZZ' is entered.

# Start of the program
while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == 'ZZZ':
        break  # Exit the loop if 'ZZZ' is entered

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    print(f"\n{first_name} {last_name} - GPA: {gpa}")
    
    if gpa >= 3.5:
        print("Congratulations! This student made the Dean's List.")
    elif gpa >= 3.25:
        print("This student made the Honor Roll.")
    else:
        print("This student did not qualify for any recognition.")

    print("-" * 40)  # Separator line

# End of the program
print("Program ended.")
