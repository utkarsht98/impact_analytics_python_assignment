# impact_analytics_python_assignment

- Since I saw that we have to mutliple combinations of a student present/absent on a single day, I can divide it into multiple sub problems.
- So, I used recursion to calculate all the valid ways a student can attend classes.
  - For every day I checked both the cases:
    1. If the student attended the class.
    2. If the student did not attend the class.
- Base case will be when the total days are complete, then I check if the candidate has used up more than the allowed consecutive holidays, then return 0, else return 1.

- For calculating the no. of ways where at the day of graduation, the student will be absent.
  - At the last day, if the no. of allowed consecutive hoidays left are >= 1, then if candidate takes a holiday, it has to be on last day, so I increment the count to 1. 
    
