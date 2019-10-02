import argparse


def open_file(file_names):
    ''' Read and Display text file on screen '''
    for file_name in file_names:
        with open(file_name, "r") as f:
            for line in f:
                print(line)


def write_file(file_names):
    ''' Write the new content to the selected file '''
    for file_name in file_names:
        with open(file_name, "w+") as f:
            f.write(input("Input your content here: "))
        with open(file_name, "r") as f:
            for line in f:
                print(line)


def create_file(file_names):
    ''' Create a new text file '''
    with open(file_name, "w") as f:
        f.write(input("Input your content here: "))


def append_file(file_names):
    ''' Modifying file '''
    for file_name in file_names:
        with open(file_name, "a") as f:
            f.write(input("Input your content here: "))
        with open(file_name, "r") as f:
            for line in f:
                print(line)


def delete_file(file_names):
    ''' Delete the text file '''
    for file_name in file_names:
        with open(file_name, "w") as f:
            f.truncate()


def cat_file(file_names):
    ''' File concatenation '''
    # file_names = [file_names]
    new_file = input("Name of new file: ")
    with open(new_file, 'w+') as f:
        for f_name in file_names:
            with open(f_name) as inf:
                f.write(inf.read())
    with open(new_file, "r") as f:
        for line in f:
            print(line)

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("file", nargs='*', help="The filename you want to display", type=str)
    group.add_argument("-w", "--write", help="Create a new file and store the text",\
                        action="store_true")
    group.add_argument("-a", "--append", help="Append new text in the file specified", \
                       action="store_true")
    group.add_argument("-t", "--truncate", help="Delete the content of the selected files", \
                       action="store_true")
    group.add_argument("-c", "--cat", help="Concatenate the selected files", \
                       action="store_true")
    args = parser.parse_args()

    if args.write:
        write_file(args.file)
    elif args.truncate:
        delete_file(args.file)
    elif args.append:
        append_file(args.file)
    elif args.cat:
        cat_file(args.file)
    else:
        open_file(args.file)

if __name__ == '__main__':
    main()

