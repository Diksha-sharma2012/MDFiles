## Problem 1: Find Highest Salary in Department A.
#### SELECT max(salary) FROM public.department WHERE department='A';

## Problem 2: Find Second Highest Salary in Department A.
### METHOD1: Using Subquery with MAX() and < 
#### SELECT MAX(Salary) FROM departments WHERE deaprtment='A' AND Salary < (SELECT MAX(Salary) FROM Departmnets WHERE department='A');  
* The SQL Subquery is used to solave this problem. And the " and salary" is used in the query because we are finding the salary by selecting a row.

### METHOD2:  Using DISTINCT, ORDER BY, LIMIT and OFFSET
#### SELECT  DISTINCT salary FROM departments WHERE department='A' ORDER BY salary DESC OFFSET 1 LIMIT 1;
* SELECT DISTINCT salary:- Retrieves unique salary values (removes duplicates) from the filtered rows.
* ORDER BY salary DESC:- Sorts the distinct salaries in descending order (highest first).
* OFFSET 1:- Skips the first row (which is the highest salary).
* LIMIT 1:- Returns only one row — which is now the second highest salary

## Problem 3: Find all the employee where Diksha live.
#### SELECT * FROM departments WHERE address IN (SELECT FROM departments WHERE emp_name='Diksha')
* If name = 'Diksha' returns more than one row, you'll get an error — to avoid that, you can use IN instead of =
### If the person is on a specific condition then run it as:
#### SELECT * FROM departments WHERE address IN (SELECT FROM departments WHERE emp_name='Diksha' AND emp_role='Sernior Manager');






