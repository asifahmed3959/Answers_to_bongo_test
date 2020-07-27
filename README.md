# Answers_to_bongo_test

This repository presents the answer to the questions of the recruitment for Bongo BD. 
There are 3 files in the repository: 
1) questions.py: This python script contains the functions which are the answer to the question.
2) test_cases.py: This python script contains test cases/ unit test to test the functions if they are working properly.
3) requirements.txt: This txt file contains the information of all the packages used to run the scripts and running the pytest.

Here are the steps to run the test cases:
1)  A python virtual environment is needed. 
2. To ensure the correct packages are used to run the test cases, the packages can be installed using the command:

```sh
$ pip install -r requirements.txt
```
3. Now the test cases can be ran using the command:

```sh
$ pytest
```

# Technoligies used

  - Python 3.6.9
  - Pytest 5.4.3

### Questions:

1) Write the following function’s body. A nested dictionary is passed as parameter. You need to
print all keys with their depth. 
    - The answer to this question is the function named print_depth from line 3 to 7 of questions.py script
    - For testing an empty dictionary is used, key with only one depth is used and tested with upto 3 depths

2) Write a new function with same functionality from Question 1, but it should be able to handle
a Python object in addition to a dictionary from Question 1.
    - The answer to this question is the function named print_depth_with_objects from line 14 to 25 of questions.py script along with a helped function from line 28 to 37.
    - For testing the same sample was used to unit testing 

3) Write following functions body. 2 Nodes are passed as parameter. You need to find Least
Common Ancestor and print its value.
    - The answer to this question is the function named lca from line 41 to 57 of questions.py script. 
    - The time complexity for this problem in worst case scenario is O(n) and space complexity is also O(n).
    - The function returns -1 if no common ancester is found.
    - The test cases checks the usual sample send with the question along with empty cases, disconnected nodes, and other possible cases. 

