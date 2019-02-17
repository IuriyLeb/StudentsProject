## OracleStudent.py

This module presents methods of choosing random student in a group to make easily for teacher to ask students

### Methods: 

1. `segments`: selection of random student considering current weights. 
Model of a comparison of the length of the segment of the probability to be answered. 
Initially, every student get segment of length 100. After student's answer length of segment will be cut in half
The boundaries of all segments are shifted
    
2. `randomizer`: selection of random student considering number of times
student answer. Initially, every student gets zero point.
Student who is asked gets one point and can not be
choose the second time in row, after it point return to zero

3. `delete`: selection random of student excluding student who is 
answered on every step.

For install clone repository on your local machine; oracle.py is an entry point.

### Usage: 
* **python oracle.py -m '1', '2' or '3'** 1:segments, 2:randomizer, 3:delete_student