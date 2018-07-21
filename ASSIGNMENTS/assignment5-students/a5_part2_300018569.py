#Family name: Tara
# Student number: 300018569
# Course: IT1 1120 
# Assignment Number: 5

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    ''' class representing a rectangle in a plane '''
    def __init__(self, bottom_left, top_right, color):
        ''' (Rectangle, Point, Point, str) -> None
        initialize rectangle with bottom left point at  bottom_left
        and top right point at top_right with a color of color.'''
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.color = color
        
    def get_bottom_left(self):
        '''(Rectangle)->Point
        Returns the bottom left point of the Rectangle'''
        return self.bottom_left
    
    def get_top_right(self):
        '''(Rectangle)->Point
        Returns the top right point of the Rectangle'''
        return self.top_right

    def get_color(self):
        '''(Rectangle)->str
        Returns the color of the Rectangle'''
        return self.color
    
    def reset_color(self, color):
        '''(Rectangle, str)->None
        Re-sets the color to a different color'''
        self.color = color

    def get_perimeter(self):
        '''(Rectangle)->number
        Returns the perimeter of the Rectangle'''
        dx = self.top_right.get()[0] - self.bottom_left.get()[0]
        dy = self.top_right.get()[1] - self.bottom_left.get()[1]

        perimeter = 2 * dx + 2 * dy
        
        return perimeter

    def get_area(self):
        '''(Rectangle)->number
        Returns the area of the Rectangle'''
        dx = self.top_right.get()[0] - self.bottom_left.get()[0]
        dy = self.top_right.get()[1] - self.bottom_left.get()[1]

        area = dx * dy
        
        return area
    
    def move(self, dx, dy):
        '''(Rectangle, number, number)->None
        moves the rectangle by dx and dy along the plane'''
        self.bottom_left.move(dx, dy)
        self.top_right.move(dx, dy)

    def intersects(self, other):
        '''(Rectangle, Rectangle)->bool
        Returns True if the rectangles share a common point.
        Otherwise returns False.'''

        #Get the x_coords and y_coords of each defining point of each rectangle

        #Self
        x_bot_left_self = self.bottom_left.get()[0]
        y_bot_left_self = self.bottom_left.get()[1]
        x_top_right_self = self.top_right.get()[0]
        y_top_right_self = self.top_right.get()[1]

        #Other
        x_bot_left_other = other.bottom_left.get()[0]
        y_bot_left_other = other.bottom_left.get()[1]
        x_top_right_other = other.top_right.get()[0]
        y_top_right_other = other.top_right.get()[1]

        #Horizontally detached
        if x_top_right_other < x_bot_left_self or x_top_right_self < x_bot_left_other:
            return False
        #Vertically detached
        elif y_top_right_other < y_bot_left_self or y_top_right_self < y_bot_left_other:
            return False
        #if neither of the above is true it is intersecting.
        return True
    
    def contains(self, x, y):
        '''(Rectangle, number, number)->bool
        Returns True if the rectangle contains the point (x,y)
        otherwise returns False.'''

        in_x_bound_of_rectangle = self.bottom_left.get()[0] <= x <=  self.top_right.get()[0]

        in_y_bound_of_rectangle = self.bottom_left.get()[1] <= y <= self.top_right.get()[1]
        
        return in_x_bound_of_rectangle and in_y_bound_of_rectangle
    
    def __eq__(self, other):
        '''(Rectangle, Rectangle)->bool
        Returns True if self and other have the same points for bottom left,
        top right and they have the same color.'''
        
        is_same_bot_left = self.bottom_left == other.bottom_left

        is_same_top_right = self.top_right == other.top_right

        is_same_color = self.color == other.color

        return is_same_bot_left and is_same_top_right and is_same_color
    
    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation Rectangle(bottom_left, top_right, color)'''
        return "Rectangle({},{},'{}')".format(self.bottom_left, self.top_right, self.color)
    
    def __str__(self):
        '''(Rectangle)->str
        Returns nice string representation of the Rectangle object that also describes it.'''
        
        template = "I am a {} rectangle with bottom left corner at {} and top right corner at {}."
        return template.format(self.color, self.bottom_left.get(), self.top_right.get())

class Canvas:
    """Class representing a collection of rectangles"""
    def __init__(self, items = []):
        ''' (Canvas, list of Rectangles) -> None
        initialize list of rectangles in canvas with rectangles if provided'''
        self.rectangles = items[:]
        
    def add_one_rectangle(self, rectangle):
        '''(Canvas, Rectangle) -> None
        Adds the rectangle to the collection of rectangles in the canvas'''
        self.rectangles.append(rectangle)
    
    def count_same_color(self, color):
        '''(Canvas, str)->int
        Returns the number of rectangles with the same color as the colour provided
        in the canvas'''
        count = 0
        for rectangle in self.rectangles:
            if rectangle.get_color() == color:
                count += 1
        return count
            

    def total_perimeter(self):
        '''(Canvas) -> number
        Returns sum of all perimeters of the rectangles in the Canvas.'''
        perimeter = 0

        for rectangle in self.rectangles:
            perimeter += rectangle.get_perimeter()
            
        return perimeter

    def min_enclosing_rectangle(self):
        '''(Canvas) -> Rectangle
        Returns the minimum enclosing rectangle of the canvas
        Precondition: Atleast one rectangle in canvas.
        '''
        #initializes the min and max points to the first rectangle's
        #bottom left, and top right points.
        min_x = self.rectangles[0].get_bottom_left().get()[0]
        min_y = self.rectangles[0].get_bottom_left().get()[1]
        max_x = self.rectangles[0].get_top_right().get()[0]
        max_y = self.rectangles[0].get_top_right().get()[1]

        #Gets the min and max x and y positions throughout the entire canvas.
        for rectangle in self.rectangles:
            bottom_left = rectangle.get_bottom_left()
            top_right = rectangle.get_top_right()

            min_x = min(min_x, bottom_left.get()[0])
            min_y = min(min_y, bottom_left.get()[1])
            
            max_x = max(max_x, top_right.get()[0])
            max_y = max(max_y, top_right.get()[1])

        return Rectangle(Point(min_x, min_y), Point(max_x, max_y), 'red')

    def common_point(self):
        '''(Canvas) -> bool
        Returns true if all rectangles contain a common point,
        Otherwise false'''
        #Goes through each unique pair of rectangles and checks if they intersect
        for first in range(len(self.rectangles)-1):
            first_rect = self.rectangles[first]
            for second in range(first + 1, len(self.rectangles)):
                second_rect = self.rectangles[second]
                if not(first_rect.intersects(second_rect)):
                    return False
        #If they all intersect they share a common point via Helly's theorem
        return True 
                
        
    def __repr__(self):
        '''(Canvas)->str
        Returns canonical string representation Canvas(rectangles)'''

        return "Canvas({})".format(self.rectangles)
    
    def __len__(self):
        '''(Canvas)->int
        Returns the number of Rectangles in the Canvas object'''

        return len(self.rectangles)
