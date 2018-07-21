import unittest, ast, warnings
# uncomment above line then replace a4_xxxxxxxx with the name of your assignment
from a4_300018569 import *


def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            test_func(self, *args, **kwargs)
    return do_test


print("\nPlease wait... Sahil's tester is testing your code for ASSN4.")
print("This could take a minute or two...")
net1 = create_network("net1.txt")
net2 = create_network("net2.txt")
net3 = create_network("net3.txt")
net4 = create_network("big.txt")
net5 = create_network("huge.txt")
net6 = create_network("test-net-0.txt")
net7 = create_network("test-net-1.txt")


class TestA4(unittest.TestCase):
    @ignore_warnings
    def test_create_network(self):
        print("\nTest 1/8: Testing create_network")
        self.assertEqual(net1, [(0, [1, 2, 3]), (1, [0, 4, 6, 7, 9]), (2, [0, 3, 6, 8, 9]), (3, [0, 2, 8, 9]), (4, [1, 6, 7, 8]), (5, [9]), (6, [1, 2, 4, 8]), (7, [1, 4, 8]), (8, [2, 3, 4, 6, 7]), (9, [1, 2, 3, 5])])
        self.assertEqual(net2, [(0, [1, 2, 3, 4, 5, 6, 7, 8, 9]), (1, [0, 4, 6, 7, 9]), (2, [0, 3, 6, 8, 9]), (3, [0, 2, 8, 9]), (4, [0, 1, 6, 7, 8]), (5, [0, 9]), (6, [0, 1, 2, 4, 8]), (7, [0, 1, 4, 8]), (8, [0, 2, 3, 4, 6, 7]), (9, [0, 1, 2, 3, 5])])
        self.assertEqual(net3, [(0, [1, 2, 3, 4, 5, 6, 7, 8, 9]), (1, [0, 4, 6, 7, 9]), (2, [0, 3, 6, 8, 9]), (3, [0, 2, 8, 9]), (4, [0, 1, 6, 7, 8]), (5, [0, 9]), (6, [0, 1, 2, 4, 8]), (7, [0, 1, 4, 8]), (8, [0, 2, 3, 4, 6, 7]), (9, [0, 1, 2, 3, 5]), (100, [112]), (112, [100, 114]), (114, [112])])
        self.assertEqual(net4, ast.literal_eval(open("big_out.txt").readline()))
        self.assertEqual(net5, ast.literal_eval(open("huge_out.txt").readline()))
        self.assertEqual(net6, [])
        self.assertEqual(net7, [])
    def test_get_common_friends(self):
        print("\nTest 2/8: Testing getCommonFriends")
        self.assertEqual(getCommonFriends(3,1, net1), [0,9])
        self.assertEqual(getCommonFriends(0,112, net3), [])
        self.assertEqual(getCommonFriends(217, 163, net4), [0, 100, 119, 150])
        self.assertEqual(getCommonFriends(1030, 1045, net5), [107,909,955,1043,1111,1197,1368,1788])

    def test_recommend(self):
        print("\nTest 3/8: Testing recommend")
        self.assertEqual(recommend(6, net1), 7)
        self.assertEqual(recommend(4, net2), 2)
        self.assertEqual(recommend(0, net2), None)
        self.assertEqual(recommend(114, net3), 100)
        self.assertEqual(recommend(112, net3), None)
        self.assertEqual(recommend(217, net4), 163)
        self.assertEqual(recommend(1030, net5), 1045)

    def test_k_or_more_friends(self):
        print("\nTest 4/8: Testing k_or_more_friends")
        self.assertEqual(k_or_more_friends(net1,5),3)
        self.assertEqual(k_or_more_friends(net2,8),1)
        self.assertEqual(k_or_more_friends(net3,12),0)
        self.assertEqual(k_or_more_friends(net4,70),33)
        self.assertEqual(k_or_more_friends(net5, 100),491)
        
    def test_max_num_friends(self):
        print("\nTest 5/8: Testing maximum_num_friends")
        self.assertEqual(maximum_num_friends(net1), 5)
        self.assertEqual(maximum_num_friends(net2), 9)
        self.assertEqual(maximum_num_friends(net3), 9)
        self.assertEqual(maximum_num_friends(net4), 347)
        self.assertEqual(maximum_num_friends(net5), 1045)

    def test_people_with_most_friends(self):
        print("\nTest 6/8: Testing people_with_most_friends")
        self.assertEqual(people_with_most_friends(net1), [1,2,8])
        self.assertEqual(people_with_most_friends(net2), [0])
        self.assertEqual(people_with_most_friends(net3), [0])
        self.assertEqual(people_with_most_friends(net4), [0])
        self.assertEqual(people_with_most_friends(net5), [107])

    def test_average_num_friends(self):
        print("\nTest 7/8: Testing average_num_friends, some of these may false fail depending on" 
              "your computer so don't worry too much, just make sure these values are close enough to vida's")
        self.assertEqual(average_num_friends(net1), 3.8)
        self.assertEqual(average_num_friends(net2), 5.0)
        self.assertEqual(average_num_friends(net3), 4.153846153846154)
        self.assertEqual(average_num_friends(net4), 19.78)
        self.assertEqual(average_num_friends(net5), 43.69101262688784)

    def test_knows_everyone(self):
        print("\nTest 8/8: Testing knows_everyone")
        self.assertEqual(knows_everyone(net1), False)
        self.assertEqual(knows_everyone(net2), True)
        self.assertEqual(knows_everyone(net3), False)
        self.assertEqual(knows_everyone(net4), False)
        self.assertEqual(knows_everyone(net5), False)
if __name__ == '__main__':
    unittest.main()
