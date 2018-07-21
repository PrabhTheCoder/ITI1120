response = "yes"
while response.casefold().strip() == "yes":
    nums = input("Enter Two Numbers in the form N1 N2: ").split()
    nums = [int(nums[0]), int(nums[1])]
    print("The sum of", nums[0], "and", nums[1], "is", sum(nums))
    response = input("Enter enter if you would like to add another 2 numbers? ")
    
