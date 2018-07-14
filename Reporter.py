#!/usr/bin/env

from os import path, rmdir, remove, walk
class Reporter():
    def __init__(self, configs):
        """
        This reporter will do all the work.
        """
        self.root = configs["root_path"]
        self.video_types = configs["video_types"]
        self.index = {
            "filename":[],
            "path":[],
            "create_date":[],
            "size":[]
        }    

    def create_index(self):
        """
        This creates an index of all the files in the root
        path, including file name, size, create date and 
        path
        """
        for root, dirs, filenames in walk(self.root):
            for filename in filenames:
                self.index["filename"].append(filename)
                file_path = path.join(root, filename)
                self.index["path"].append(file_path)
                self.index["size"].append(path.getsize(file_path))
                self.index["create_date"].append(path.getmtime(file_path))
        with open("index.csv", "w") as index:
            for i in range(len(self.index["filename"])):
                index.write("{},{},{},{}\n".format(self.index["filename"][i],self.index["path"][i], 
                self.index["size"][i], self.index["create_date"][i]))
            
        