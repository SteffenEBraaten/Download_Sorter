import os
import shutil

#TODO
# Find a way to find the downloads folder to a user without an explicit path

# Change the "folder_to_sort" to the path of the folder you want to sort
folder_to_sort = '/Users/YOUR_USERNAME/Desktop/to_be_moved'
filepath = 'file_extensions.txt'

exstension = {}

def read_file(file):
    try:
        print("Reading from file...")
        with open(file, 'r') as fe:
            for line in __nonblank_lines(fe):
                word = line.split()
                __make_folder(word[0])
                exstension[word[0]] = []
                for i in range(1, len(word)):
                    exstension[word[0]].append(word[i])                    
    finally:
        __make_folder('Other')
        print('Reading from file completed!')
        fe.close()

def sort():
    print('Sorting started...')
    for file_name in os.listdir(folder_to_sort):
        source = folder_to_sort + '/' + file_name
        for key in exstension:
            for value in exstension[key]:
                if file_name.endswith(value):
                    source = folder_to_sort + '/' + file_name
                    destination = folder_to_sort + '/' + key + '/' + file_name
                    __move_file(source, destination)
        other = folder_to_sort + '/Other/' + file_name
        __move_file(source, other)
    print('Sorting completed!')

def __nonblank_lines(file):
    for line in file:
        line = line.rstrip()
        if line:
            yield line

def __make_folder(name):
    new_folder = folder_to_sort + '/' + name
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

def __move_file(source, destination):
    if os.path.isfile(source):
        shutil.move(source, destination)

def main():
    read_file(filepath)
    sort()

main()