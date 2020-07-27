# 1) Write the following function’s body. A nested dictionary is passed as parameter. You need to
#    print all keys with their depth.
def print_depth(a, level=1):
    for i in a.keys():
        if type(a[i]) == dict:
            print(i + ' : ' + str(level))
            print_depth(a[i], level + 1)

        else:
            print(i + ' : ' + str(level))

# 2) Write a new function with same functionality from Question 1, but it should be able to handle
# a Python object in addition to a dictionary from Question 1.
def print_depth_with_objects(a, level=1):
    for i in a.keys():
        if type(a[i]) == dict:
            print(i + ' : ' + str(level))
            print_depth_with_objects(a[i], level+1)

        elif isinstance(a[i], Person):
            print(i + ' : ' + str(level))
            print_person_dfs(a[i], level + 1)

        else:
            print(i + ' : ' + str(level))

#function is related to answer2
def print_person_dfs(person, level=1):
    print("first_name : " + str(level))
    print("last_name : " + str(level))

    if isinstance(person.father, Person):
        print("father : " + str(level))
        print_person_dfs(person.father, level + 1)

    else:
        print("father : " + str(level))

# 3) Write following functions body. 2 Nodes are passed as parameter. You need to find Least
# Common Ancestor and print its value.
def lca(node1, node2):
    d = {}
    temp = node1

    while(temp!=None):
        d[temp.val] = 1
        temp = temp.parent

    temp = node2

    while(temp!=None):
        if temp.val in d:
            return temp.val
        else:
            temp=temp.parent

    return -1


#class Person for Person Object
class Person(object):

    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


#class Node for Node Object
class Node:

    def __init__(self, val=None, parent=None):
        self.val = val
        self.parent = parent
