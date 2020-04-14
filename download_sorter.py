import os
import sys

folder_to_sort = '{}/Downloads/'.format(os.path.expanduser('~'))
filepath = 'file_extensions.txt'

exstensions = {}

def read_file(file):
    """
    Reads the extensions in the file and loads them into the extensions dictionary. 
    
    If the file format is not correct an exception will be thrown and the program
    will be terminate.
    """
    
    try:
        with open(file, 'r') as fe:
            print('Reading from file...')
            for line in fe:
                word = line.split()
                __make_folder(word[0])
                exstensions[word[0]] = []
                for i in range(1, len(word)):
                    exstensions[word[0]].append(word[i])
        __make_folder('Other')
        print('Reading from file completed!')
    except IOError as e:
        print(e)
        sys.exit()

def sort_files():
    """
    Sorting the files in the selected folder based on the extensions which is
    loaded from the file read in read_file(file). 
    
    If the fiel extension matches one of the extentions it will be moved to 
    the folder that the extension relates to.

    However if the extension does not match any of our extensions it will
    be placed in the "Other" folder.
    """

    print('Sorting started...')
    for file in os.listdir(folder_to_sort):
        source = '{}/{}'.format(folder_to_sort, file)
        for key in exstensions:
            for value in exstensions[key]:
                if file.lower().endswith(value):
                    destination = '{}/{}/{}'.format(folder_to_sort, key, file)
                    __move_file(source, destination)
        other = '{}/Other/{}'.format(folder_to_sort, file)
        __move_file(source, other)
    print('Sorting completed!')

def __make_folder(folder_name):
    new_folder = '{}/{}'.format(folder_to_sort, folder_name)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

def __move_file(source, destination):
    if os.path.isfile(source):
        os.rename(source, destination)

def main():
    read_file(filepath)
    sort_files()
    
main()