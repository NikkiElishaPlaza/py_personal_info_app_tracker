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
    
    while True:
        user_name = input("Enter your name: ")

        if user_name and not any(char.isdigit() for char in user_name):
            break
        else:
            print("Kindly enter a valid name that contains letters and not numbers.")
    




# Storing in a txt file
    """
    txt file format
    Full name, Birthdate, Personal number, Telephone number, Address
    """
