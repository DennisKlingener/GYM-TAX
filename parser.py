#!/usr/bin/env python3


import logging
import argparse
from pathlib import Path
import re
import sys


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
            self._process_header(file)

            # Search for constatns and process them.
            self._process_constants(file)
            

            # Process the execises now.
            while True:

                # Read the line
                line = file.readline()

                # we have reached the end.
                if line == "":
                    return

                if self._is_comment(line):
                    continue
            
                # process exercise.
                if "#" in line:
                    self._process_exercise(file, line)

                    



                
            
            
            
            
            
             


        
        
        
        



    def _process_header(self, filePointer):
        while True:
            # Read the next line
            line = filePointer.readline()

            if not re.search("======*", line):
                continue
            else:
                return

    
    # Need better logic here to parse the constants....
    def _process_constants(self, filePointer):
        if filePointer.readline() == "CONSTANTS":
            while True:

                # Read the next line
                line = filePointer.readline()

                # save the current position
                curPos = filePointer.tell()

                if self._is_comment(line):
                    continue

                try:
                    key, value = line.split("=")
                    self.constants[key] = value
                except Exception as _:
                    filePointer.seek(curPos)
                    return


    def _process_exercise(self, filePointer, exerciseData):
            
        exerciseName, setRange, *_ = exerciseData.split("|")
        exerciseName = exerciseName.strip("# ")

        try:
            minSet, maxSet = setRange.split("-")
        except Exception as _:
            minSet, maxSet = setRange, setRange


        self.data[exerciseName] = {
            "minSet": minSet.strip(),
            "maxSet": maxSet.strip("S "),
            "data": {}
        }
        
        while True:
            
            # Read the next line
            line = filePointer.readline()


            if self._is_comment(line) or self._is_newline(line):
                continue

            # Save the current position.
            curPos = filePointer.tell()

            # Check to see if we have processed all the logs for this execise.
            if "-" not in line:
                filePointer.seek(curPos)
                return
            
            # Parse the current log line.
            date, data = line.split(":")

            weightInfo, data = data.split("@")

            setInfo, notes = data.split(".", 1)

            date = date.strip("- ")
            weightInfo = weightInfo.strip()
            setInfo = setInfo.split(",")

            for i in range(len(setInfo)):
                setInfo[i] = setInfo[i].strip()

            self.data[exerciseName]["data"] = {
                "dataCompleted": date,
                "totalWeight": weightInfo,
                "sets": setInfo
            }



            print(exerciseName)
            print(self.data[exerciseName])
            sys.exit()
                



    def _is_comment(self, line):
        if "//" in line:
            return True
        else:
            return False

    def _is_newline(self, line):
        if line == "\n":
            return True
        else:
            return False





def parse_args():
    parser = argparse.ArgumentParser("Getting them Gainz son")
    parser.add_argument("--path", required=True, type=str, help="Path to your log file. ")
    return parser.parse_args()











if __name__ == "__main__":
    args = parse_args()
    parser = Parser(args)
    parser.parse()

    
    
    
    


