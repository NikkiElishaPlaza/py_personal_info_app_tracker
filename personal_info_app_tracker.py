# main func
def main():
    print("Welcome to personal info app tracker!")

    # txt file path to store data
    personal_info_file_path = "personal_info.txt"

    # get user personal data
    user_personal_info = get_user_info()

    # write info to txt file
    save_personal_info_to_file = ()

    # repeating the process and continue adding data
    continue_input = ()

# get user infos
    """
    infos to get
    Full name (First name, M.I., Last name)
    Birthdate (M/D/Y)
    Personal number (+63 ___)
    Telephone number (if applicable, put 0 if N/A)
    Address
    """
def get_user_info():
    
    # user name
    while True:
        user_name = input("Enter your name: ")

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

    



# Storing in a txt file
        """
    txt file format
    Full name, Birthdate, Personal number, Telephone number, Address
        """
