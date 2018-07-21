import unittest
import random
from a5_part1_300018569 import *
from a5_part2_300018569 import *
from a5_part3_300018569 import *    
#uncomment above lines then replace a5_part1_xxxxxxxx,a5_part2_xxxxxxxx, a5_part3_xxxxxxxx, with the name of your assignment
#example: from a5_part1_300018482 import *
#         from a5_part2_300018482 import *
#         from a5_part3_300018482 import *


print("\nPlease wait... Sahil's tester is testing your code for ASSN5.")
print("This could take a few seconds...")

class TestA5(unittest.TestCase):
    #Test part1
    def test_largest_34(self):
        t1 = [1000, 1, 100, 2, 99, 200, -100]
        t2 = [1,2,3,4,5,6,7,8,9,10]
        t3 = [-100, 100, 200, -1000, 300, 356, 99, 69, 1000000000000]
        t4 = [100,100,100,200,300,400,300,300,100,100,100]
        t5 = [100,100,100,200,200,200]
        t6 = [-100,-100,200,200,300,200]
        t7 = [-100,-100,200,300,400,500]
        t8 = [x for x in range(1000000)]
        random.shuffle(t8)
        self.assertEqual(largest_34(t1), 199)
        self.assertEqual(largest_34(t2), 15)
        self.assertEqual(largest_34(t3), 500)
        self.assertEqual(largest_34(t4), 600)
        self.assertEqual(largest_34(t5), 300)
        self.assertEqual(largest_34(t6), 400)
        self.assertEqual(largest_34(t7), 500)
        self.assertEqual(largest_34(t8), 1999993)
    def test_largest_third(self):
        t1 = [1000, 1, 100, 2, 99, 200, -100]
        t2 = [1,2,3,4,5,6,7,8,9,10]
        t3 = [-100, 100, 200, -1000, 300, 356, 99, 69, 1000000000000]
        t4 = [100,100,100,200,300,400,300,300,100,100,100]
        t5 = [100,100,100,200,200,200]
        t6 = [-100,-100,200,200,300,200]
        t7 = [-100,-100,200,300,400,500]
        self.assertEqual(largest_third(t1), 1200)
        self.assertEqual(largest_third(t2), 27)
        self.assertEqual(largest_third(t3), 1000000000656)
        self.assertEqual(largest_third(t4), 1000)
        self.assertEqual(largest_third(t5), 400)
        self.assertEqual(largest_third(t6), 500)
        self.assertEqual(largest_third(t7), 900)
    def test_third_atleast(self):
        t1 = [1000, 1, 100, 2, 99, 200, -100]
        t2 = [1,2,3,4,5,6,7,8,9,10]
        t3 = [-100, 100, 200, -1000, 300, 356, 99, 69, 1000000000000]
        t4 = [100,100,100,200,300,400,300,300,100,100,100]
        t5 = [100,100,100,200,200,200]
        t6 = [-100,-100,200,200,300,200]
        t7 = [-100,-100,200,300,400,500]
        self.assertEqual(third_at_least(t1), None)
        self.assertEqual(third_at_least(t2), None)
        self.assertEqual(third_at_least(t3), None)
        self.assertEqual(third_at_least(t4), 100)
        self.assertEqual(third_at_least(t5), 100)
        self.assertEqual(third_at_least(t6), 200)
        self.assertEqual(third_at_least(t7), None)
    def test_sum_tri(self):
        t1 = [1000, 1, 100, 2, 99, 200, -100]
        t2 = [1,2,3,4,5,6,7,8,9,10] 
        t3 = [-100, 100, 200, -1000, 300, 356, 99, 69, 1000000000000]
        
        self.assertEqual(sum_tri(t1, 900), False)
        self.assertEqual(sum_tri(t1, 901), True)
        self.assertEqual(sum_tri(t1, 3000), True)
        self.assertEqual(sum_tri(t1, 4), True)
        self.assertEqual(sum_tri(t1, 203), True)
        self.assertEqual(sum_tri(t1, 200), True)
        self.assertEqual(sum_tri(t1, 101), True)
        self.assertEqual(sum_tri(t1, 105), False)

        self.assertEqual(sum_tri(t2, 27), True)
        self.assertEqual(sum_tri(t2, 55), False)
        self.assertEqual(sum_tri(t2, 30), True)
        self.assertEqual(sum_tri(t2, 24), True)
        self.assertEqual(sum_tri(t2, 21), True)

        self.assertEqual(sum_tri(t3, -1200), True)
        self.assertEqual(sum_tri(t3, 357), False)
        self.assertEqual(sum_tri(t3, 1000000000000), True)
        self.assertEqual(sum_tri(t3, 3000000000000), True)
        self.assertEqual(sum_tri(t3, 156), True)
        self.assertEqual(sum_tri(t3, 524), True)
    #Testing part 2
    ##Rectangle
    def test_reset_colour(self):
        r1 = Rectangle(Point(), Point(1,1), 'red')
        r1.reset_color("red-orange")
        self.assertEqual(r1.get_color(), 'red-orange')
        r1.reset_color("green-blue")
        self.assertEqual(r1.get_color(), 'green-blue')

    def test_get_perimeter(self):
        r1 = Rectangle(Point(), Point(2,1), 'red')
        r2 = Rectangle(Point(-100, -300), Point(100, 300), 'orange')
        r3 = Rectangle(Point(), Point(0, 1), 'red')
        self.assertEqual(r1.get_perimeter(), 6)
        self.assertEqual(r2.get_perimeter(), 1600)
        self.assertEqual(r3.get_perimeter(), 2)
        
    def test_get_area(self):
        r1 = Rectangle(Point(), Point(2,1), 'red')
        r2 = Rectangle(Point(-100, -300), Point(100, 300), 'orange')
        r3 = Rectangle(Point(), Point(0, 1), 'red')
        self.assertEqual(r1.get_area(), 2)
        self.assertEqual(r2.get_area(), 120000)
        self.assertEqual(r3.get_area(), 0)

    def test_move(self):
        r1 = Rectangle(Point(), Point(2,1), 'red')
        r2 = Rectangle(Point(-100, -300), Point(100, 300), 'orange')
        r3 = Rectangle(Point(), Point(0, 1), 'red')
        r1.move(2,1)
        self.assertEqual(r1.get_bottom_left().get(), (2, 1))
        self.assertEqual(r1.get_top_right().get(), (4, 2))
        r2.move(-2,1)
        self.assertEqual(r2.get_bottom_left().get(), (-102, -299))
        self.assertEqual(r2.get_top_right().get(), (98, 301))
        r3.move(-1,1)
        self.assertEqual(r3.get_bottom_left().get(), (-1, 1))
        self.assertEqual(r3.get_top_right().get(), (-1, 2))
    def test_str(self):
        r1=Rectangle(Point(), Point(1,1), "red")
        r2=Rectangle(Point(), Point(3,4), "red-orange")
        self.assertEqual(str(r1), "I am a red rectangle with bottom left corner at (0, 0) and top right corner at (1, 1).")
        self.assertEqual(str(r2), "I am a red-orange rectangle with bottom left corner at (0, 0) and top right corner at (3, 4).")

    def test_rect_eq(self):
        r1 = Rectangle(Point(2,3),Point(3,4),'blue')
        r2 = eval(repr(r1))
        r3 = Rectangle(Point(1,1), Point(2,2.5), "blue")
        r4 = Rectangle(Point(1,1), Point(2,2.5), "blue")
        r5 = Rectangle(Point(1,1), Point(2,2.5), "red")
        self.assertEqual(r1 == r2, True)
        self.assertEqual(r3 == r4, True)
        self.assertEqual(r4 == r5, False)
        
    def test_intersects(self):
        r1=Rectangle(Point(1,1), Point(2,2), "blue")
        r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
        r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
        r4=Rectangle(Point(0,0), Point(10,10), "orange")
        r5=Rectangle(Point(0,0), Point(1,1), "red")
        self.assertEqual(r1.intersects(r2), False)
        self.assertEqual(r2.intersects(r1), False)
        self.assertEqual(r1.intersects(r3), True)
        self.assertEqual(r2.intersects(r3), False)
        self.assertEqual(r4.intersects(r1), True)
        self.assertEqual(r4.intersects(r2), True)
        self.assertEqual(r4.intersects(r3), True)
        self.assertEqual(r5.intersects(r1), True)
    def test_contains(self):
        r=Rectangle(Point(1,1), Point(2,5), "blue")
        self.assertEqual(r.contains(1.5, 1), True)
        self.assertEqual(r.contains(2, 2), True)
        self.assertEqual(r.contains(0, 0), False)
    ##Canvas
    def test_add_rect(self):
        c = Canvas()
        r1=Rectangle(Point(1,1), Point(2,2), "blue")
        r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
        r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
        c.add_one_rectangle(r1)
        c.add_one_rectangle(r2)
        c.add_one_rectangle(r3)
        c.add_one_rectangle( Rectangle(Point(0,0),Point(100,100),"orange") )
        self.assertEqual(len(c), 4)
    def test_repr_canv(self):
        c = Canvas()
        r1=Rectangle(Point(1,1), Point(2,2), "blue")
        r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
        r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
        c.add_one_rectangle(r1)
        c.add_one_rectangle(r2)
        c.add_one_rectangle(r3)
        c.add_one_rectangle( Rectangle(Point(0,0),Point(100,100),"orange") )
        self.assertEqual(str(c), "Canvas([Rectangle(Point(1,1),Point(2,2),'blue'), Rectangle(Point(2,2.5),Point(3,3),'blue'), Rectangle(Point(1.5,0),Point(1.7,3),'red'), Rectangle(Point(0,0),Point(100,100),'orange')])")
        
    def test_len_canv(self):
        d = Canvas()
        g = Canvas([Rectangle(Point(), Point(), "red")])
        self.assertEqual(len(d), 0)
        self.assertEqual(len(g), 1)

    def test_count_color(self):
        c = Canvas()
        r1=Rectangle(Point(1,1), Point(2,2), "blue")
        r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
        r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
        c.add_one_rectangle(r1)
        c.add_one_rectangle(r2)
        c.add_one_rectangle(r3)
        self.assertEqual(c.count_same_color("blue"), 2)
        self.assertEqual(c.count_same_color("red"), 1)
        self.assertEqual(c.count_same_color("yellow"), 0)
        self.assertEqual(c.count_same_color("red blue"), 0)

    def test_min_enclosing(self):
        c=Canvas()
        r1=Rectangle(Point(1,1), Point(2,2), "blue")
        r2=Rectangle(Point(1,1), Point(4,4), "blue")
        r3=Rectangle(Point(-2,-2), Point(-1,-1), "blue")
        r4=Rectangle(Point(0,-100),Point(1,100), "yellow")
        c.add_one_rectangle(r1)
        c.add_one_rectangle(r2)
        c.add_one_rectangle(r3)
        c.add_one_rectangle(r4)
        rect = c.min_enclosing_rectangle()
        self.assertEqual(rect.get_bottom_left().get(), (-2,-100))
        self.assertEqual(rect.get_top_right().get(), (4,100))
    
    def test_common_point(self):
        c=Canvas()
        g=Canvas()
        r1=Rectangle(Point(1,1), Point(2,2), "blue")
        r2=Rectangle(Point(1.5,1.5), Point(4,4), "blue")
        r3=Rectangle(Point(-2,-2), Point(2,1.5), "blue")
        r4=Rectangle(Point(0,-100),Point(1.5,100), "yellow")

        _r1=Rectangle(Point(-2,-2), Point(-1,2), "blue")
        _r2=Rectangle(Point(-2,-2), Point(2,-1), "blue")
        _r3=Rectangle(Point(1,-2), Point(2,2), "blue")
        _r4=Rectangle(Point(-2,1), Point(2,2), "blue")

        c.add_one_rectangle(r1)
        c.add_one_rectangle(r2)
        c.add_one_rectangle(r3)
        c.add_one_rectangle(r4)
        self.assertEqual(c.common_point(), True)

        g.add_one_rectangle(_r1)
        g.add_one_rectangle(_r2)
        g.add_one_rectangle(_r3)
        g.add_one_rectangle(_r4)
        self.assertEqual(g.common_point(), False)

    #Testing part 3
    def test_digit_sum(self):
        self.assertEqual(digit_sum(1969), 25)
        self.assertEqual(digit_sum(100000000000001), 2)
        self.assertEqual(digit_sum(1000101010101012334566928171),64)
        self.assertEqual(digit_sum(1220136825991110068701238785423046926253574342803192842192413588385845373153881997605496447502203281863013616477148203584163378722078177200480785205159329285477907571939330603772960859086270429174547882424912726344305670173270769461062802310452644218878789465754777149863494367781037644274033827365397471386477878495438489595537537990423241061271326984327745715546309977202781014561081188373709531016356324432987029563896628911658974769572087926928871281780070265174507768410719624390394322536422605234945850129918571501248706961568141625359056693423813008856249246891564126775654481886506593847951775360894005745238940335798476363944905313062323749066445048824665075946735862074637925184200459369692981022263971952597190945217823331756934581508552332820762820023402626907898342451712006207714640979456116127629145951237229913340169552363850942885592018727433795173014586357570828355780158735432768888680120399882384702151467605445407663), 4237)
    def test_digital_root(self):
        self.assertEqual(digital_root(1969), 7)
        self.assertEqual(digital_root(1220136825991110068701238785423046926253574342803192842192413588385845373153881997605496447502203281863013616477148203584163378722078177200480785205159329285477907571939330603772960859086270429174547882424912726344305670173270769461062802310452644218878789465754777149863494367781037644274033827365397471386477878495438489595537537990423241061271326984327745715546309977202781014561081188373709531016356324432987029563896628911658974769572087926928871281780070265174507768410719624390394322536422605234945850129918571501248706961568141625359056693423813008856249246891564126775654481886506593847951775360894005745238940335798476363944905313062323749066445048824665075946735862074637925184200459369692981022263971952597190945217823331756934581508552332820762820023402626907898342451712006207714640979456116127629145951237229913340169552363850942885592018727433795173014586357570828355780158735432768888680120399882384702151467605445407663), 7)
        self.assertEqual(digital_root(1000101010101012334566928171), 1)
        self.assertEqual(digital_root(100000000000001), 2)
if __name__ == '__main__':
    unittest.main()
