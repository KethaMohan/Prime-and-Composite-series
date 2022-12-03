print('************* Prime and Composite Numbers in Given Range ***************')
print('Welcome')
print('Created by')
print('Name: Ketha Mohan')
print('Reg No:12207967')
print('Roll Number: 15')    
print('Let\'s continue with project')
print()


def pricom(a,b):
    P=0
    C=0
    for i in range(Lower,Upper+1):
        count=0
        for j in range(2,i):
            if  i%j==0:
               count+=1
        if i==1:
            print(i,'is neither prime nor composite')
        elif i>1:
            if count<=0:
                P+=1
                print(i,'is prime number ')
            else:
              C+=1
              print(i,'is composite number')
    print(P,'prime numbers and',C,'composite numbers')
    print()
    
Lower=int(input('Enter Lower Number: '))
Upper=int(input('Enter Upper Number: '))

pricom(Lower,Upper)

print('Thank You')
