from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

class FileOrginazor(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(folder_to_track):
            source = folder_to_track + "/" + file_name
            destination = folder_move_to + "/" + file_name
            os.rename(source, destination)
            print("Moved the file {0} to {1}.".format(file_name, destination))

folder_to_track = '/Users/YOUR_USERNAME/Desktop/to_be_moved'
folder_move_to = '/Users/YOUR_USERNAME/Desktop/moved'
event_handler = FileOrginazor()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()