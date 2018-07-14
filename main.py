#!/usr/bin/env
import json
from Reporter import Reporter
# This is the program that is used to manage my video data locally
# potentially this could also be used to manage all other files
# Expected Functions include:
#   1. Detecting files that have the same size in bytes
#   2. Detecting files with the same name (exact match except for the extension)
#   3. Listing all files found in 1 and 2 and store them in a csv file with an 
#       absolute path to the files
#   4. Allow manually deleting entries in the csv file created in 3 and is able 
#       to read the csv file and delete files listed according to 5
#   5. For files with same size, keep file that has a human-readable name (this is
#       sometimes a manual process); for files with same name, keep file that is
#       larger (assumed to be higher quality)
# 


def config():
    configs = None
    with open("./config/config.json", "r") as conf:
        configs = json.load(conf)
    return configs

def main():
    reporter = Reporter(config())
    reporter.create_index()

if __name__ == "__main__":
    main()