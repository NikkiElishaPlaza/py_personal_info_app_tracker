def search_user_info():
    print("Welcome to the personal info search!")
    
    # Ask for the full name
    user_name = input("Enter the full name (First name, M.I., Last name) to search for: ").strip()

    # File path for personal info
    personal_info_file_path = "personal_info.txt"

    try:
        with open(personal_info_file_path, "r") as file:
            file_content = file.read()
            
            # Check if the full name exists in the file
            if user_name in file_content:
                print(f"\nInformation found for {user_name}:\n")
                # Display the information found
                start_index = file_content.find(user_name)
                end_index = file_content.find('---', start_index)
                
                print(file_content[start_index:end_index].strip())
            else:
                print(f"No information found for {user_name}.")
    except FileNotFoundError:
        print(f"Error: {personal_info_file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

search_user_info()
