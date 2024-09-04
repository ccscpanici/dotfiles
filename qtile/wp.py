#!/usr/bin/python

import os
from os import listdir
import random
class WallpaperChanger(object):

    def __init__(self, directory_list):
        self.directories = directory_list
        self.files = self.get_files()

    def __get_folder_files__(self, folder):
        file_list = []
        for a_file in os.listdir(folder):
            if(a_file.endswith(".png") or a_file.endswith(".jpg") or \
                a_file.endswith(".jpeg") or a_file.endswith(".svg")):
               full_path = folder + "/" + a_file
               file_list.append(full_path)
            # end if
        # end looping through files
        return file_list

    def get_files(self):
        file_list = []
        for a_folder in self.directories:
            file_list = file_list + self.__get_folder_files__(a_folder)
        # end for
        return file_list

    def get_random(self):
        return random.choice(self.files)
