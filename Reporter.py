#!/usr/bin/env python

from os import path, rmdir, remove, walk, rename
import re


class Reporter():
    def __init__(self, configs):
        """
        This reporter will do all the work.
        """
        self.root = configs["root_path"]
        self.video_types = configs["video_types"]
        self.save_file_path = configs["save_file_path"]
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
            # rename directories
            for dir in dirs:
                newname = self._clean_filename(dir)
                self._rename_file(newname, dir, root)

            for filename in filenames:
                newname = self._clean_filename(filename)
                self._rename_file(newname,filename,root)
                self.index["filename"].append(newname)
                file_path = path.join(root, newname)
                self.index["path"].append(file_path)
                self.index["size"].append(path.getsize(file_path))
                self.index["create_date"].append(path.getmtime(file_path))
        with open(self.save_file_path, encoding="utf-8", mode="w+") as index:
            index.write("filename,path,size,create_date\n")
            for i in range(len(self.index["filename"])):
                try:
                    index.write("{},{},{},{}\n".format(self.index["filename"][i],self.index["path"][i], 
                    self.index["size"][i], self.index["create_date"][i]))
                except UnicodeEncodeError:
                    print(self.index["path"][i])
                    continue 
    @staticmethod
    def _clean_filename(filename):
       pattern = re.compile(r"[^\w\n\s\.]")
       newname = re.sub(pattern, "_", filename)
       return newname

    @staticmethod
    def _rename_file(newname, filename, root):
        rename(path.join(root, filename), path.join(root, newname))