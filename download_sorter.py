import os
import sys

folder_to_sort = '{}/Downloads/'.format(os.path.expanduser('~'))
filepath = 'file_extensions.txt'

exstensions = {}


def read_file(file):
    """
    Reads the extensions in the file and loads them into the extensions dictionary. 

    If the file format is not correct an exception will be thrown and the program
    will be terminated.
    """

    try:
        with open(file, 'r') as fe:
            print('Reading from file...')
            for line in fe:
                word = line.split()
                exstensions[word[0]] = []
                for i in range(1, len(word)):
                    exstensions[word[0]].append(word[i])
        print('Reading from file completed!')
    except IOError as e:
        print(e)
        sys.exit()


def sort_files():
    """
    Sorting the files in the selected folder based on the extensions which is
    loaded from the file read in read_file(file). 

    If the file extension matches one of the extentions it will be moved to 
    the folder that the extension relates to.

    However, if the extension of the file does not match any of our defined 
    extensions it will be placed in the "Other" folder.
    """
    
    print('Sorting started...')
    for file in os.listdir(folder_to_sort):
        source = '{}/{}'.format(folder_to_sort, file)
        if(__sort_file(source, file)):
            continue
        __sort_other_file(source, file)
    print('Sorting completed!')


def __sort_file(source, file):
    for key in exstensions:
        for value in exstensions[key]:
            if file.lower().endswith(value):
                __make_folder(key)
                destination = '{}/{}/{}'.format(folder_to_sort, key, file)
                __move_file(source, destination)
                return True
    return False


def __sort_other_file(source, file):
    __make_folder('Other')
    destination = '{}/Other/{}'.format(folder_to_sort, file)
    __move_file(source, destination)


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
