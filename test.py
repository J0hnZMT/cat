import argparse


def open_file(file_name):
    ''' Read and Display text file on screen '''
    with open(file_name, "r") as f:
        for line in f:
            print(line)


def write_file(file_name,file_content):
    ''' Create a new text file '''
    with open(file_name, "w") as f:
        f.write(file_content)


def append_file(file_name,file_content):
    ''' Modifying file '''
    with open(file_name, "a") as f:
        for i in range(2):
            f.write(file_content)


def delete_file(file_name):
    ''' Delete the text file '''
    with open(file_name, "w") as f:
        f.truncate()


def cat_file(first_file,second_file,new_file):
    ''' File concatenation '''
    file_names = [first_file,second_file]
    with open(new_file, 'w') as f:
        for f_name in file_names:
            with open(f_name) as infile:
                f.write(infile.read())


def main():
    x=True
    while x:
        print("1.Read")
        print("2.Write")
        print("3.Append")
        print("4.Delete")
        print("5.Concatenate")
        print("6.Exit")
        choice = input("Input the number here: ")

        if choice == '1':
            file_name = input("File name: ")
            open_file(file_name)
        elif choice == '2':
            file_name = input("File name: ")
            file_content = input("File content: ")
            write_file(file_name,file_content)
        elif choice == '3':
            file_name = input("File name: ")
            file_content = input("File content: ")
            append_file(file_name,file_content)
        elif choice == '4':
            file_name = input("File name: ")
            delete_file(file_name)
        elif choice == '5':
            first_file = input("First File name: ")
            second_file = input("SecondFile name: ")
            new_file = input("New File name: ")
            cat_file(first_file,second_file,new_file)
            print("File Created")
        elif choice == '6':
            print("Closing...")
            x=False
        else:
            print("Not in the choices")


if __name__ == '__main__':
    main()

