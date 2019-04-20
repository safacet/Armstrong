#1634, 371, 153, 370, 407 are some of Armstrong numbers
while True:
    number = input("Enter a number:")
    digit = len(number)
    number = int(number)
    control = number
    """
Program will reduce the number for continue to pull the digits and after the process
it will need the number again to compare
    """
    sum = 0
    for i in range(digit,0,-1):
        a = (control//(10**(i-1)))**digit #Most valuable digits fourth power
        sum += a
        control -= (control//(10**(i-1)))*(10**(i-1)) #Deletes the most valuable digit
    if sum == number:
        print("Your number is an Armstrong number")
    else:
        print("Your number is NOT an Armstrong number")