import os

def create_dir(file_path):
    print(f"\nDirectory not found creating {file_path}")
    os.makedirs(file_path)

def write_data(file_path_name):
    user_name = input("\nPlease enter your contact info: \n Name: ")
    user_address = input("Address: ")
    user_phone_num = input ("Phone number: ")
    with open(file_path_name, 'w') as file_object:
        file_object.write(f"{user_name}, {user_address}, {user_phone_num}")

def read_data(file_path_name):
    with open(file_path_name) as file_object:
        data =file_object.read()
    print(f"\nFile Successfully created with the following content: \n{data}")

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
