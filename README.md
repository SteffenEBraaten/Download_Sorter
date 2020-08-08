# Download Sorter <img alt="GitHub" src="https://img.shields.io/github/license/SteffenEBraaten/Download_Sorter">
A simple python script to keep your downloads folder nice and tidy.

This program will sort your files in diffrent folders based on it's extension type. You are free to add/remove any folder or extensions you may want by manipulating the file_extensions.txt file. Some of the file extension in this file is basedupon [FileInfos common file types list](https://fileinfo.com/filetypes/common).

## Prerequisites
You'll need [Python 3](https://www.python.org/) to run the script. 

## Running the script
To run the script simply write the following in the terminal:
```bash
 python3 download_sorter.py
 ```

### Known Issues
#### Running the script in WSL
This script will not be able to sort your downloads folder in windows if you're running the script on linux using WSL (Windows subsystem for linux). 

The reason is because the os module in python will identify the os as linux and not windows. It will then try to sort the downloads folder in the linux filesystem (which does not exist by default in WSL) instead of the downloads folder in the windows filesystem.

##### Workaround
Run the script in powershell or run the file in the file explorer.

## Demo
![](https://github.com/SteffenEBraaten/Download_Sorter/blob/master/Images/download_sorter_demo.gif)
