# Regular if-else statement
def adult(age):
    if age >= 18:
        return True
    else: 
        return False
    
# Turnary operator
def isAdult(age):
    return True if age >= 18 else False

adult = adult(20)
adult2 = isAdult(12)

print(adult, adult2)