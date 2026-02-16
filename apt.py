# Student Attendance Tracker

REQUIRED_PERCENTAGE = 75


# -------- Function: Calculate Attendance --------
def calculate_attendance(total_classes, absents):
    attended = total_classes - absents
    percentage = (attended / total_classes) * 100
    return percentage


# -------- Function: Eligibility Check --------
def check_status(percentage):
    if percentage >= REQUIRED_PERCENTAGE:
        print("You are eligible for exams.")
    elif percentage >= 65:
        print("Warning: Attendance getting low.")
    else:
        print("Critical Attendance Shortage!")


# -------- Function: Classes Needed Prediction --------
def classes_needed(total_classes, absents):
    attended = total_classes - absents
    extra_classes = 0

    while True:
        new_percentage = ((attended + extra_classes) /
                          (total_classes + extra_classes)) * 100

        if new_percentage >= REQUIRED_PERCENTAGE:
            return extra_classes

        extra_classes += 1


# -------- Function: Save Record --------
def save_record(total, absents, percentage):
    with open("attendance.txt", "a") as file:
        file.write(
            f"Total Classes: {total}, Absents: {absents}, Attendance: {percentage:.2f}%\n"
        )


# -------- Function: Add Attendance --------
def add_attendance():
    try:
        total = int(input("Enter total classes conducted: "))
        absents = int(input("Enter number of absents: "))

        if total <= 0:
            print("Total classes must be greater than 0.")
            return

        if absents < 0 or absents > total:
            print("Invalid number of absents.")
            return

        percentage = calculate_attendance(total, absents)

        print(f"\nYour Attendance: {percentage:.2f}%")
        check_status(percentage)

        needed = classes_needed(total, absents)

        if percentage < REQUIRED_PERCENTAGE:
            print(
                f"You must attend next {needed} classes continuously to reach 75%."
            )

        save_record(total, absents, percentage)
        print("Record saved successfully!\n")

    except ValueError:
        print("Please enter valid numbers only.")


# -------- Function: Predict Future Attendance --------
def predict_attendance():
    try:
        total = int(input("Enter total classes so far: "))
        absents = int(input("Enter absents so far: "))
        future_absents = int(input("If you miss how many more classes? "))

        attended = total - absents
        new_total = total + future_absents
        new_absents = absents + future_absents

        new_percentage = calculate_attendance(new_total, new_absents)

        print(f"\nPredicted Attendance: {new_percentage:.2f}%")

    except ValueError:
        print("Invalid input.")


# -------- Main Menu --------
def main():
    while True:
        print("\n====== Attendance Tracker ======")
        print("1. Add Attendance")
        print("2. Predict Attendance")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_attendance()
        elif choice == "2":
            predict_attendance()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
main()