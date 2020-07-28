from questions import Person
from questions import Node
from questions import print_depth
from questions import print_depth_with_objects
from questions import lca


def test_print_depth(capfd):
    # testing with the sample input in the question
    a = {
        'key1': 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }
    print_depth(a)
    out, err = capfd.readouterr()
    assert out == 'key1 : 1\nkey2 : 1\nkey3 : 2\nkey4 : 2\nkey5 : 3\n'\

    #testing with one level of input
    b = {
        "key1" : 1
    }
    print_depth(b)
    out, err = capfd.readouterr()
    assert out == 'key1 : 1\n'

    # testing with zero input
    c = {}
    print_depth(c)
    out, err = capfd.readouterr()
    assert out == ''

    # As the algorithm is written following DFS, this will print in depth of other levels before completing
    #the following level, therefore testing.
    a = {
        'key1': 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        },
        "key6": 1
    }
    print_depth(a)
    out, err = capfd.readouterr()
    assert out == 'key1 : 1\nkey2 : 1\nkey3 : 2\nkey4 : 2\nkey5 : 3\nkey6 : 1\n'

def test_depth_with_objects(capfd):
    person_a = Person('User', '1', None)
    person_b = Person(first_name="User", last_name= "2", father=person_a)

    # testing with the sample provided in the question
    a = {
        'key1': 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user" : person_b
            }
        }
    }

    print_depth_with_objects(a)
    out, err = capfd.readouterr()
    assert out == 'key1 : 1\nkey2 : 1\nkey3 : 2\nkey4 : 2\nkey5 : 3\nuser : 3\nfirst_name : 4\nlast_name : 4\nfather : 4\n' \
                    + 'first_name : 5\nlast_name : 5\nfather : 5\n'

    # testing with only object from first key in the data
    b = {
        "user" : person_b
    }

    print_depth_with_objects(b)
    out, err = capfd.readouterr()
    assert out == 'user : 1\nfirst_name : 2\nlast_name : 2\nfather : 2\n' \
           + 'first_name : 3\nlast_name : 3\nfather : 3\n'

    # testing with empty dictionary
    c = {
    }

    print_depth_with_objects(c)
    out, err = capfd.readouterr()
    assert out == ''


def test_lca(capfd):
    v_1 = Node(1)
    v_2 = Node(2)
    v_3 = Node(3)
    v_4 = Node(4)
    v_5 = Node(5)
    v_6 = Node(6)
    v_7 = Node(7)
    v_8 = Node(8)
    v_9 = Node(9)
    v_unconnected = Node(100)
    v_3.parent = v_2.parent = v_1
    v_4.parent = v_5.parent = v_2
    v_8.parent = v_9.parent = v_4
    v_7.parent = v_6.parent = v_3

    #             1      100
    #           /  \
    #          2    3
    #        / \   / \
    #       4   5  6  7
    #      / \
    #     8  9

    # testing from node 6 and 7, the lca will be node 3
    lca(v_7, v_6)
    out, err = capfd.readouterr()
    assert out == '3\n'

    # testing from node 3 and 7, the lca will be node 3
    lca(v_3, v_7)
    out, err = capfd.readouterr()
    assert out == '3\n'

    # testing from node 1 and 1, the lca will be node 1
    lca(v_1, v_1)
    out, err = capfd.readouterr()
    assert out == '1\n'

    # testing from node 8 and 7, the lca will be node 1
    lca(v_8, v_7)
    out, err = capfd.readouterr()
    assert out == '1\n'

    # testing from node 100 and 7, there is no lca
    lca(v_unconnected, v_7)
    out, err = capfd.readouterr()
    assert out == ''

    # testing edge case node None and 7, there is no lca
    lca(None, v_7)
    out, err = capfd.readouterr()
    assert out == ''

    # testing edge case input None and None, there is no lca
    lca(None, None)
    out, err = capfd.readouterr()
    assert out == ''






