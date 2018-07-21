def get_year():
    n = ""
    
    while len(n) != 4:
        try:
            n = input("Enter a 4 digit year: ")
            if len(n) != 4:
                print("Please enter a four digit integer for the year")
            else:
                year = int(n)
            
        except ValueError:
            print("Please enter a four digit integer for the year")
    return year
lst = [1, 2, 3, 4, 5]
summation = 0
totalPrint = ""
for x in lst:
    summation += x
    totalPrint += str(x) + " + "
print(f"{totalPrint}= {summation}")
