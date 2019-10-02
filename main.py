import argparse


def open_file(file_name):
    ''' Read and Display text file on screen '''
    with open(file_name, "r") as f:
        for line in f:
            print(line)


def write_file(file_name):
    ''' Create a new text file '''
    with open(file_name, "w") as f:
        f.write(input("Input your content here: "))


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
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The filename you want to display", type=str)
    # parser.add_argument("content", help="The content of the file", type = str)
    # parser.add_argument("-w", "--write", help="Create a new file and store the text",\
    #                     action="store_true")
    args = parser.parse_args()
    open_file(args.file)
    # if args.write:
    #     write_file(args.file, args.content)

if __name__ == '__main__':
    main()

