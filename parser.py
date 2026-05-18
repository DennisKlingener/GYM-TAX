#!/usr/bin/env python3


import logging
import argparse
from pathlib import Path
import re



class Parser:

    log = logging.getLogger("Parser")

    constants = {}

    data = {}

    def __init__(self, args):
        self.dataFilePath = Path(args.path)
        
        
    def parse(self):
        
        # Ensure the path is valid.
        if not self.dataFilePath.exists():
            self.log.error("Path to data file is invalid!")
            return

        
        # Open the file and begin parsing.
        with open(self.dataFilePath, "r") as file:

            # We will need to skip the header section first by finding the header ende string.
            self.process_header(file)

            # Search for constatns and process them.
            self.process_constants(file)
            

            # Process the execises now.
            for line in file:
            
                if "#" in line:
                    # process exercise.
                    

                    



                
            
            
            
            
            
            pass
             


        
        
        
        
        pass



    def process_header(self, filePointer):
        for line in filePointer:
            if not re.search("======*", line):
                continue
            else:
                return


    def process_constants(self, filePointer):
        if filePointer.readline() == "CONSTANTS":
            for line in filePointer:

                if line == "END CONSTANTS":
                    return

                key, value = line.split("=")
                self.constants[key] = value

    def process_exercise(self, filePointer):
            
            exerciseName, setRange, _ = filePointer.readline() 

            try:
                minSet, maxSet = setRange.split("-")
            except:
                minSet, maxSet = setRange, setRange

            self.data[exerciseName] = {
                "minSet": minSet,
                "maxSet": maxSet,
                "data": {}
            }

            for line in filePointer:

                # Save the current position.
                curPos = filePointer.tell()

                if "-" not in line:
                    filePointer.seek(curPos)
                    return
                
                











def parse_args():
    parser = argparse.ArgumentParser("Getting them Gainz son")
    parser.add_argument("--path", required=True, type=str, help="Path to your log file. ")
    return parser.parse_args()











if __name__ == "__main__":
    args = parse_args()
    
    
    
    
    
    print("Sup")


