#!/usr/bin/env

class Reporter():
    def __init__(self, configs):
        """
        This reporter will do all the work.
        """
        self.root = configs["root_path"]
        self.video_types = configs["video_types"]
    
    def create_index(self):
        """
        This creates an index of all the files in the root
        path, including file name, size, create date and 
        path
        """
        