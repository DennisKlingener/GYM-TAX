# GYM-TAX
Parsable syntax used to track gym routines with supporting features 

- TODO
- RECURSION???



# SYNTAX OF GYM-TAX
- Needs to be a header portion of the file with notes etc
    - Everything before a sting of 5 > "=" characters are denoted as notes/header and will be ignored.   

- Need to define constants.
    - Constants are defined in the constatns sections as so
    - CONSTANTS
      NameOfConstant=value(int)
      N constants
      END CONSTANTS

- Need to define where a execise begins. 
    - "#" denotes a exercise.

- When denoting an exercise the following syntax is expected:
    - "Exercise name | number of sets *(| extra data) :"
    - Need to support a range of sets
    - Need to define the syntax for denoting set ranges.

- imediatly afgter the exersice has been defined, the following format is expected:
    - Need to define the wiehgt list.... and the "-" charactrer in it.
    - "- Date: weight used (each key word if needed) @ (number of reps completed per set for N sets comma seperated). AGAIN or BUMP keyword and any notes always ended with a period.
    - THE AGAIN/BUMP SHOULD NOT BE A KEYWORD SHOULD SIMPLY BE A NOTE....



- Comments -> "//"