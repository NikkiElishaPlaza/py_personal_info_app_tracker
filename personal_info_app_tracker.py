# main func
def main():
    print("Welcome to personal info app tracker!")

    # txt file path to store data
    personal_info_file_path = "personal_info.txt"

    while True:
        # get user personal data
        user_personal_info = get_user_info()

        # write info to txt file
        save_personal_info_to_file(personal_info_file_path, user_personal_info)

        # repeating the process and continue adding data
        continue_input = input("Would you like to add another entry? (yes/no): ").strip().lower()
        if continue_input != "yes":
            print("Thank you for using the personal info tracker. Goodbye!")
            break

# get user infos
def get_user_info():
    # user name
    while True:
        user_name = input("Enter your full name (First name, M.I., Last name): ")

        if user_name and not any(char.isdigit() for char in user_name):
            break
        else:
            print("Kindly enter a valid name that contains letters and not numbers.")
    # user bday
    while True:
        user_bday = input("Enter your Birthdate (Month Day, Year): ")

        try:
            if "," in user_bday and " " in user_bday:

                comma_position = user_bday.find(",")
                last_space_position = user_bday.rfind(" ")
            month_day = user_bday[:comma_position]
            year = user_bday[last_space_position + 1:]

            if year.isdigit() and len(year) == 4:
                day_part = month_day.split()[-1]
                break
            else:
                print("Year must be valid 4-digit number only.")
        except:
            print("Kindly print your birthdate in a proper format: Month Day, Year (e.g., December 25, 0000)")
    # user phone number
    while True:
        user_phone_number = input("Enter your phone number here: ")

        if user_phone_number.isdigit() and len(user_phone_number) == 11:
            break
        else:
            print("Enter a valid personal number with 11 digits.")
    # user telephone number
    while True:
        user_telephone_number = int(input("Enter your telephone number here (Enter 0 if N/A): "))

        if user_telephone_number == 0 or len(user_telephone_number) == 10:
            break
        else:
            print("Invalid input.")
            break
    # user address
    while True:
        user_address = input("Enter your Address here: ")

        if user_address:
            break
        else:
            print("Address cannot be empty.")

    return {
        "Full Name": user_name,
        "Birthdate": user_bday,
        "Personal Number": user_phone_number,
        "Telephone Number": user_telephone_number,
        "Address": user_address
    }
# Storing in a txt file
separator = "-" * 25
def save_personal_info_to_file(file_path, personal_info):
    try:
        with open(file_path, "a") as file:
            file.write(
                f"\nFull name: {personal_info['Full Name']}\n"
                f"Birthdate: {personal_info['Birthdate']}\n"
                f"Personal number: {personal_info['Personal Number']}\n"
                f"Telephone number: {personal_info['Telephone Number']}\n"
                f"Address: {personal_info['Address']}\n"
                f"{separator}"
            )
        print(f"Personal information saved successfully in {file_path}.")
    except Exception as e:
        print(f"An error occurred while saving the information: {e}")
    
main()