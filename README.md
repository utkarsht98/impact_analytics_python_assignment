# impact_analytics_python_assignment

1) Solution using recursion
  - Since I saw that we have to mutliple combinations of a student present/absent on a single day, I can divide it into multiple sub problems.
  - So, I used recursion to calculate all the valid ways a student can attend classes.
    - For every day I checked both the cases:
      1. If the student attended the class.
      2. If the student did not attend the class.
  - Base case will be when the total days are complete, then I check if the candidate has used up more than the allowed consecutive holidays, then return 0, else return     1.

  - For calculating the no. of ways where at the day of graduation, the student will be absent.
    - At the last day, if the no. of allowed consecutive hoidays left are >= 1, then if candidate takes a holiday, it has to be on last day, so I increment the count to       1.
 
 ---- New Update------
 
 2) Solution using dynamic programming

  - The time complexity for above given solution is exponential since, we are trying all the combinations of days vs no. of miss days left. 
  - So to avoid calculating repeated states, I used dynamic programming to store the already calculated states in a dp matrix.
  - I created a matrix of noOfDays+1 and missDays+1, since the index start from 0 and we need values from 1 to n.
  - The ans at "dp[noOfDays][missDays]" has the total no. of ways stored in it.
  - The complexity reduce from exponential to quadratic.
  - So, T.C is - O(no. of states * operations for each state)
  - no. of states = dp matrix
  - operation for each state = 1
  - So final TC = O(noOfdays*missDays)
