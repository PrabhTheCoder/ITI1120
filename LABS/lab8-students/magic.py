def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''

     # this tests the condition that is implied by the definition
     # i.e. that m has to be a square matrix
     if(not(is_square(m))): # if matrix is not square
          return False      # return False

     # YOUR CODE GOES HERE
     diagonal_down = 0
     diagonal_up = 0
     length = len(m)
     columns = [0] * length
     rows = [0]* length
     numbers = []
     # TEST CONDITION 1
     for row_index in range(length):
          for column_index in range(length):
               tmp = m[row_index][column_index]
               if tmp not in numbers:
                    numbers.append(tmp)
               else:
                    return False

               
     # TEST CONDITION 2
     for row_index in range(length):
          rows[row_index] = sum(m[row_index])
          for column_index in range(length):
               curr = m[row_index][column_index]
               columns[column_index] += curr
               if row_index == column_index:
                    diagonal_down += curr
               if length - 1- row_index == column_index:
                    diagonal_up += curr
     test_val = rows[0]
     for i in rows:
          if i != test_val:
               return False
     for i in columns:
          if i != test_val:
               return False

     return diagonal_up == diagonal_down == test_val

# main
# TESTING OF magic functions
276
951
483
# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not 
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
