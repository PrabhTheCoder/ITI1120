import tkinter.filedialog
import grade
a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename, 'r')

a1_histfilename = tkinter.filedialog.askopenfilename()
a1_histfile = open(a1_histfilename, 'r')

# Read the grades into a list.

# Count the grades per range.

# Write the histogram to the file.

"""
0-9:   *
10-19: **
20-29: ***
  :
90-99: **
100:   *
"""
