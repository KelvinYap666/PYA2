#Name: KelvinYap

#reverse function
def printBackward(n,n1,n2,n3):
    while int(n)>0:
        print(int(n)%10,end="")
        n=int(n)//10
    print(end=" ")
    while int(n1)>0:
        print(int(n1)%10,end="")
        n1=int(n1)//10
    print(end=" ")
    while int(n2)>0:
        print(int(n2)%10,end="")
        n2=int(n2)//10
    print(end=" ")
    while int(n3)>0:
        print(int(n3)%10,end="")
        n3=int(n3)//10
    print()

#double the even digits
def doubleDigits(n, n1, n2, n3):
    reversed_n = int(str(n)[::-1])
    reversed_n1 = int(str(n1)[::-1])
    reversed_n2 = int(str(n2)[::-1])
    reversed_n3 = int(str(n3)[::-1])
    
    new_n = int(str(reversed_n)[0] + str(int(str(reversed_n)[1]) * 2) + str(reversed_n)[2] + str(int(str(reversed_n)[3]) * 2))
    new_n1 = int(str(reversed_n1)[0] + str(int(str(reversed_n1)[1]) * 2) + str(reversed_n1)[2] + str(int(str(reversed_n1)[3]) * 2))
    new_n2 = int(str(reversed_n2)[0] + str(int(str(reversed_n2)[1]) * 2) + str(reversed_n2)[2] + str(int(str(reversed_n2)[3]) * 2))
    new_n3 = int(str(reversed_n3)[0] + str(int(str(reversed_n3)[1]) * 2) + str(reversed_n3)[2] + str(int(str(reversed_n3)[3]) * 2))

    return new_n, new_n1, new_n2, new_n3

#sum up the digits in each element
#find the special sum of all element in card
#and add the conclusion to check whether is valid or invalid
def getSumofDigits(n,n1,n2,n3,new_n,new_n1,new_n2,new_n3):
    sum1=0
    sum_n=new_n
    while int(sum_n) > 0:
        lastDigit=int(sum_n)%10
        sum1+=lastDigit
        sum_n = int(sum_n)//10
    sum2=0
    sum_n1=new_n1
    while int(sum_n1) > 0:
        lastDigit=int(sum_n1)%10
        sum2+=lastDigit
        sum_n1 = int(sum_n1)//10
    sum3=0
    sum_n2=new_n2
    while int(sum_n2) > 0:
        lastDigit=int(sum_n2)%10
        sum3+=lastDigit
        sum_n2 = int(sum_n2)//10
    sum4=0
    sum_n3=new_n3
    while int(sum_n3) > 0:
        lastDigit=int(sum_n3)%10
        sum4+=lastDigit
        sum_n3 = int(sum_n3)//10

    print("\nGet all the sum of all card digit in element\n")
    print(sum1, sum2, sum3, sum4)
    totalsum=sum1+sum2+sum3+sum4
    print("\nSum of all special elements in card\n{0}".format(totalsum))
    if sumDivide(totalsum):
        print("\nConclusion: \n"
              "\t{0}-{1}-{2}-{3} is a valid credit card because {4} % 10 = 0"
              .format(n,n1,n2,n3,totalsum))
    else:
        print("\nConclusion: \n"
              "\t{0}-{1}-{2}-{3} is an invalid credit card because {4} % 10 != 0"
              .format(n,n1,n2,n3,totalsum))

        
#function of if totalsum can be mod by 10
def sumDivide(totalsum):
    return totalsum % 10 == 0
    
#function to check if its valid
def CardLength(n,n1,n2,n3):
    return len(n) == 4 and len(n1) == 4 and len(n2) == 4 and len(n3) == 4

#function to check for alphabets
def validCard(n,n1,n2,n3):
    return n.isdigit() and n1.isdigit() and n2.isdigit() and n3.isdigit()


#main function          
def main():
    y='y'
    Y='Y'
    while y.lower() == 'y':
        print("Welcome to KelvinYap credit card company")
        n, n1, n2, n3 = input("Enter a credit card: ").split("-")
        if CardLength(n, n1, n2, n3)and validCard(n,n1,n2,n3):
            print("\nYou entered: {0} {1} {2} {3}".format(n, n1, n2, n3))
            print("\nReverse digits\n")
            printBackward(n, n1, n2, n3)
            new_n, new_n1, new_n2, new_n3 = doubleDigits(n, n1, n2, n3)
            print("\nMultiply  by 2 of each even digit\n")
            print("{0} {1} {2} {3}".format(new_n, new_n1, new_n2, new_n3))
            getSumofDigits(n, n1, n2, n3, new_n, new_n1, new_n2, new_n3)
            
            new_card = input("Enter another card? y/Y/n/N: ")
            if new_card.lower() != 'y':
                y = 'n'
        
        else:
            print("\nInvalid credit card format\n")
            new_card = input("Enter another card? y/Y/n/N: ")
            if new_card.lower() != 'y':
                y = 'n'


    input("\n\nPress Enter to terminate")
    
if __name__=="__main__":
    main()
