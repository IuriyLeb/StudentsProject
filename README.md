## OracleStudent.py

This module presents methods of choosing random student in a group to make easily for teacher to ask students

### Methods: 

1) `segments`: selection of random student considering current weights
    Model of a comparison of the length of the segment of the probability to be answered
    Initially, every student get segment of length 100. After student's answer length of segment will be cut in half
    The boundaries of all segments are shifted
    
2) `randomizer`: selection of random student considering number of times
student answer. Initially, every student gets zero point.
Student who is asked gets one point and can not be
choose the second time in row, after it point returt to zero

3) `delete`: selection random of student excluding student who is 
answered on every step.

For install clone repository on your local mashine oracleStudent.py is an entry point

### Usage: 
* `python oracle.py -m segments` - runs the script with "segments" module
* `python oracle.py -m randomizer` - runs the script with "randomizer" module
* `python oracle.py -m delete` - runs the script with "delete" module
* `oracle.py -h` - help page.
