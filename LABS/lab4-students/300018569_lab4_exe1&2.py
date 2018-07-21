##################QUESTION 1:###########################
def is_eligible(age, citizenship, prison):
    """(int, str, str) -> bool

    Return eligibility of voting depending on the user being over 18,
    being of a citizenship of canadian origin, and not being in prison
    
    Preconditions: age >= 0, prison is either yes or no
    """
    citizenship = citizenship.strip().casefold()
    prison = prison.strip().casefold()
    return (age >= 18 and (citizenship == "canada" or citizenship == "canadian")
            and prison == "no")
            
name=input("What is your name? ")
age= int(input("How old are you? "))
citizenship = input("What is your citizenship? ")
prison = input("Are you currently convicted and in prison? ")

if is_eligible(age, citizenship, prison):
     print(name, ", you are eligible to vote")
else:
     print(name, ", you are ineligible to vote") 
    
###############Question 2: #############################
def mess(s):
    """(str) -> str

    Returns a string with the last 8 consonants(r,s,t,v,w,x,y,z) in s
    capitalized, and with blank spaces in s replaced with dashes (-).
    """
    accumulator = ''
    for ch in s:
        if ch in "rstvwxyz":
            accumulator += ch.upper()
        elif ch == ' ':
            accumulator += '-'
        else:
            accumulator += ch
    
    return accumulator    
