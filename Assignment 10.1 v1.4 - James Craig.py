# This program will prompt the user for a directory and file name to 
# save a file that will contain the user's contact information. It will
# then read back the contents of the file after it is created.

# Importing os module to enable functions to see if a directory exists
# and create it if it doesn't.
import os

# Function that crates a directory if the user wanted to save the file
# to a directory that did not exist.
def create_dir(file_path):
    print(f"\nDirectory not found creating {file_path}")
    os.makedirs(file_path)

# Function to prompt the user for their contact info and write it to 
# a text file in the directory and with the file name the user requested.
def write_data(file_path_name):
    user_name = input("\nPlease enter your contact info: \n Name: ")
    user_address = input("Address: ")
    user_phone_num = input ("Phone number: ")
    with open(file_path_name, 'w') as file_object:
        file_object.write(f"{user_name}, {user_address}, {user_phone_num}")

# Function that confirms the data writen to the file created in the write_data
# function as it prints the contents of the file that was created.
def read_data(file_path_name):
    with open(file_path_name) as file_object:
        data =file_object.read()
    print(f"\nFile Successfully created with the following content: \n{data}")

# Main function that prompts the user for the file directory and if the path
# doesn't exist it calls the create_dir function to create a directory for
# the path specified. After it calls the write_data and read_data functions
# to write data to a text file containing the user's contact info and then
# read it back to show the user it was successfully saved.
def main():
    directory = input("In what directory do you wish to save your file?\n c:/")
    file_path = f"/{directory}"
    exists = os.path.exists(file_path)
    
    if exists == False:
        create_dir(file_path)

    file_name = input("File name: ")
    file_path_name = f"{file_path}/{file_name}.txt"
    write_data(file_path_name)
    read_data(file_path_name)

main()
