# t= int(input("enter temperature"))



# if t<0:
#     print("freezing")
# elif t==0 or t<10:
#     print("very cold")
# elif t==10 or t<20:
#     print("cold")
# elif t==20 or t<30:
#     print("warm")
# elif t==30 or t<40:
#     print("hot")
# else:
#     print("very hot")


#------------------------------------------------------------------------LOOPS--------------------------------------------------------------------------------------------

# a= int(input("enter a number:-"))

# for i in range(1,a+1):
#     print ("hello world")


# for i in range(a,0,-1):
#     print(i)


# for i in range(a,a*10,a):
#     print(i)


# for i in range(1,a+1):

#     sum = sum + i
# print(sum)

# for i in range (a,1,-1):
#     fact = fact*i
# print(fact)

# even=0
# odd=0
# for i in range(1,a+1):

#     if i%2 == 0:
#         even= even+i
#     else:
#         odd=odd+i

# print(f"odd and even numver is {odd},{even}")

# if i%even==0:
#     print(f"even number factor is{i}")
# else:
#     print(f"odd number factor is{i}")


# import random

# num1 = random.randint(1,10)


# t=0

# while True:
#     num2 = int(input("enter a number:-"))

#     if num1==num2:
#         print("you win")
#         t+=1
#         print(f"you win in {t} attempts")
#         break
#     elif num1>num2:
#         print("number is greater")
#         t+=1
#     elif num1<num2:
#         print("number is smaller")
#         t+=1
#     else:
#         print("you lose")
#         t+=1


# def hello(name):
#     print(f"hello my love {name}")

# hello("bhvaik")
# hello("dhurvi")


# name=input("enter your name:-")
# age=int(input("enter your age"))

# def voter(name,age):
#     if age>=18:
#         print(f"{name} you are  eligable")
#     else:
#         print(f"{name} you are not eligable")

# voter(name,age)

# a =[10,11,12,13]

# a[0]=14
# print(a)

# num = [-1,-2,-3,0,1,2,3]


# for i in range(num[0],len(num)):
#     if num[i]<0:
#         print(f"{num[i]} is negetive")
#     elif num[i]>0:
#         print(f"{num[i]}is positive")
#     else:
#         print(f"{num[i]}is zero")


# sum=0

# for i in num:
#     a=len(num)
#     sum= sum+i

# print(sum/a)


# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

# largest = num[0]
# slargest = num[0]
# index=0

# for i in range(len(num)):
#     if num[i]>largest:
#         slargest=largest
#         largest=num[i]
#         index=i
#     elif num[i]>slargest:
#         slargest=num[i]
#         index=i


# print(f"the largest number is {largest} and index is {index} and second largest number is {slargest} and index is {index}")


# for i in range(len(num) -1):
#     if num[i] < num[i+1]:
#         continue
#     else:
#         print("not sorted")
#         break
# else:
#     print("list is sorted")

# d1 = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500, 60: 600}
#
# sum=0
#
#
# for i in d1:
#     sum=sum+d1[i]

# print(sum)

# a = [1,1,3,3,5,6,6,8,8]

# d = {}
#
# for i in a:
#
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i]=1
# print(d)


# r = open("bhavik.txt", 'w')
#
# r.write("hello i am bhavik.i am python devloper.i study in L.d college of engginearing ahemdabad")
# r.close()

# -------------------------------------------------oops------------------------------------------------------------------------------------

# class Account:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def show(self):
#         print(f"your account details is {self.name}  and balance is {self.balance}")
#
#
# a = Account("bhavik",1000)
# b = Account("dhruvi",5000)
#
#
#
# a.show()
#

# class Bhavik:
#     def book(self):
#         b_name= input("Enter your name: ")
#         books=["hindi","gujrati","maths"]
#         if b_name in books:
#              print(f"{b_name.capitalize()} book made")
#         else:
#             print(f"{b_name.capitalize()} book is not available")
#
#
#
#
#
# a=input("Enter your value: ")
# if a=="1":
#     Bhavik().book()

# class A:
#     def __init__(self, x):
#         self.x = x
#
# s = A("bhavik")
# print(s.x)
