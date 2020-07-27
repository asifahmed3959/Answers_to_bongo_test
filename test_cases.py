from questions import Person
from questions import Node
from questions import print_depth
from questions import print_depth_with_objects
from questions import lca


def test_print_depth(capfd):
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

    b = {
        "key1" : 1
    }
    print_depth(b)
    out, err = capfd.readouterr()
    assert out == 'key1 : 1\n'

    c = {}
    print_depth(c)
    out, err = capfd.readouterr()
    assert out == ''


def test_depth_with_objects_and_one_depth_till_level_3(capfd):
    person_a = Person('User', '1', None)
    person_b = Person(first_name="User", last_name= "2", father=person_a)

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

def test_lca():
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

    assert lca(v_7, v_6) == 3
    assert lca(v_3, v_7) == 3
    assert lca(v_1, v_1) == 1
    assert lca(v_unconnected, v_9) == -1
    assert lca(None, v_7) == -1
    assert lca(None, None) == -1




