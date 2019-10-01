def open_file(file_name):
    with open(file_name, "r") as f:
        content = f.read()
        print(content)

def append_file(file_name,file_content):
    with open(file_name, "w") as f:
        for i in range(2):
            f.write(file_content)
def write_file(file_name,file_content):
    with open(file_name, "w") as f:
        f.write(file_content)
    
print("1.Read")
print("2.Write")
print("3.Append")
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
else:
    print("Not in the choices")


