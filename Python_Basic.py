#  #my first program

# # y=input("Enter your age:")
# # print(input("name:"))
# # print(input(" Age:"))
# # print(10<5)
# # print(10!=10)
# # # a=15
# # # b=2
# # # print(a%b)
# # print(15%2)
# rain= True
 
# if rain==True:
#     print("not go to school")
 
# else:  
#     print("go to school")

# age= float(input("Age:"))
# if age>=18:
#     print("selected")    
# else:
#     print("Not selected") 

# print(type(age))   
# print(age)
# a=int(input("Enter length:"))
# b=int(input("Enter length:"))
# if a==b:
#     print("this is a square")
# else:
#     print("this is a rectangle")    
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if a>=b and a>=c:
#     print("a is a largest number")
# elif b>=a and b>=c:
#     print("b is a largest number")
# else:
#     print("c is a largest number")       
# for i in  range(5,11,2):
#     print (i)
# for i in range(10):
#     print("I Love You")
# a= list(range(10))
# b=list(range(3,10))
# c=list(range(1,10,2))
# print(a)
# print(b)
# print(c)
# a="hello world"
# for letter in a:
#     print(letter)
# bag=["alu","piaj",3,2.5,-1,0,50,23] 
# for item in bag:
#     print(bag) 
# list2=[12,32,45,76,21]
# for i in list2:
#     if i<=40:
#         print(i)    
# for i in range(20):
#     if i%3==0 and i%5==0:
#         print(i)
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)
# a=0
# while a<=10:
#     a=a+1
#     if a==5:
#         break
#     print(a)
 
# a=0
# while a<=10:
#     a=a+1
#     if a>=5:
#         continue
#     print(a)
 
# a=10
# while a==10:
#     print(a)       
# while True:
#     print("I Love You")
# while True:
#     name=input("Enter your name:")
#     if name=="quit" or name =='q':
#         break
#     print("hello ",name,"good morning")
# nested loop
# for row in range(3):
#     for col in range(row+1):
#         print("#",end=' ')  #space using
#     print()   #new line
# nested list:
# bajarer list       
# bajar_list=[["alu","piaj"],["pizza",2.5,2],[3,6,5,7]] 
# for item in bajar_list:
    
#     for coto_item in item:
#         print(coto_item)
# num=int(input("Entetr number:"))
# for i in range(1,11):
#     print(num,' x ',i,'= ',num*i)
# factorial=1
# a=int(input("Enter value:"))
# for i in range(1,a+1):
#     factorial=factorial * i
# print(factorial)   
# fibonacci series:
# a=0
# b=1
# for i in range(10):
#     print(b,end=' ')
#     c=a+b
#     a=b
#     b=c
# //count the number of digit ina number:

# //Method-1:longcut
a=int(input("Enter number:"))
count=0
while a>0:
    digit=a%10
    print(digit)
    count=count +1
    a=a//10
print(count)
#  //Method-2:shortcut:
# a=input("Enter number:")
# print(len(a))
# check armstrong number:
# //method 1:
# a=int(input("Enter number:"))
# num_len=len(str(a))
# temp=a
# sum=0
# // while temp>0:
#     last_digit=temp%10
#     sum=sum+last_digit**num_len
#     temp//=10

# if sum==a:
#     print ("Armstrong number")
# else:
#     print ("Not Armstrong number")  
# //Method 2:shortcut
# a=input("Enter number:")
# num_len=len(a)
# sum=0
# for i in a:
#     sum+=int(i)**num_len
# if ilisnt(a)==sum:
#     print ("Armstrong number")
# else:
#     print ("Not Armstrong number")  
# //revers integer number and string:
# a=int(input("Enter number:"))
# rev_a=0
# while a>0:
#     last_digit=a%10
#     rev_a=rev_a*10 + last_digit
#     a//=10
# print(rev_a) DAY 7 COMPLETE:--
# string k list a convert:
# s="hello world"
# print(list(s))

# //append() method add element at end
# list=[1,2,3,4,5]  
# list.append(6)   #according to sequence a akta kore element add hobe
# list.append(7)  
# list.append("pizza")   
# print(list)
# list.insert(0,9) #insert hobe specipic position a
# print(list)

# //coppy method:
# a=[1,2,3,4]
# b=a.copy() 
# for i in b:
#     b[i]=(b[i]+1)
# print(b)
# // count method
# a=[2,5,5,6,3,'a','a','a','e','q']

# print(a.count('a'))
# # print(len(a))
# # item='a'
# # if item in a:
# #     print(item," is found")
# # else:
# #     print("Not found")    
# // #extend() add the element of a list to
# #  the end of the current list
# a.extend([0,0,8])
# # #shortcut:
# a+=[9,9]
# print(a)

# //pop method:last element delete kore
# a=[2,3,4,8,0,5]

# #// print("Delete ",a.pop(),"Updated list:",a)
# #remove() pop a particular element of given list
# a.remove(3)
# print(a)
# # a.clear()
# # print(a)
# a.reverse()##reverse elements of list
# print(a)
# #//by default assending order
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
 
# print(max(a))

# //taking user input: 
 
# n=5
# a=[]
# print("Enter ",n ,"elements:")
# for i in range(n):
#     a.append()
# print(a)
# taking multiple user inputs of string:
# a=input('Enter multiple strings:').split()
# print(a)

# //taking multiple inputs of integer:
# a=map(int,input("Enter multiple integer number:").split())
# print(list(a))

# List comprehension/list update:
# problem 1:
# a=[1,2,3,4,5]
# b=[i*5 for i in a]
# string
# print(b)
# //pronlem 2:
# a='hellow world'
# b=[i for i in a]
# print(b)
# print(list(a))#sortcut

# a=[i for i in range(1,20,2)]
# print (a)
# a=[]
# for i in range(1,20):
#     if i%3==0:
#         a.append(i)
# print(a)        
#       sortcut:
# b=[i for i in range(1,20) if i%3==0]#i is expresion
# print (b)
# //when using nested if else:
# a=[]
# for i in range(1,20):
#     if i%3==0:
#         a.append(i)
#     if i%5==0:
#         a.append(i)    
# print(a)   //same kaj sortcut a korbo usng list compreheion:
# b=[i for i in range(1,20) if i%3==0 or i%5==0]
# print(b)  //when using if else:
# a=["Even"if i%2==0 else "Odd" for i in range(1,20)]
# print(a)
# import calendar
# y=2025
# m=1
# for i in range(m,12):
#  print(calendar.month(y,i))
# //2D matrix to transpose matrix:
# matrix=[[1,2],[3,4],[5,6],[7,8]] #4 ta raw 2 ta col convert to 2 ta row 4 ta col
# # a=[]
# # for row in range(2):
# #    b=[]
# #    for col in matrix:
# #       b.append(col[row])
# #    a.append(a)
# # print(a)  
# # sortcut using list comprehension:
# res=[[col[row] for col in matrix]for row in range(2)]
# print(res)
# //swaping two list element:

# temp=a[0]
# a[0]=a[-1] #a[len(a)-1]
# a[-1]=temp
# print(a)
# //count unique elements in a list:
# a=[1,2,2,3,3,4,5,6]
# b=[]
# count=0
# for i in a:
#     if i not in b:
#         count=count+1
#         b.append(i)
# print(count)

# // Given a list , extract all elements whose frecuency is greater than k
# list=[4,6,4,3,3,4,3,4,3,8]
# k=3
# res=[]
# for i in list:
#     freq= list.count(i)
#     if freq >k and i not in res:
#         res.append(i)
# print(res)        
# // create the following list using list comprehension:
# a=[]
# for i in range(5):
#     for j in range(5):
#         if i==j:
#             continue
#         a.append(j)
# print(a)        

# //using list comprehension

# a=[[j for j in range(5) if i!=j] for i in range(5)]
# print(a) //nested list

# a=[i for i in range(5) if i%3==0]
# print(a)

# //indexing and immutability in string:
# a="Hello world" #0-10 index
# n=5
# a=[int(input(f"'Enter  {i+1} elements:'")) for i in range(n)]
# print(a)
# print(a[-1])
# # a[-1]="D"##update kora jacca na so immutable char hold korce
# print(a[-1])
# print(a)#// string print korce  
# for i in range(len(a)):
#     print(a[i]) # index shape a print korce
# print(a[6:11])# string slicing

# //String related built in method:
# reverse
a="hello world python"
# print(a.lower())#//but main string ta same ee thakbe  karon string change kora jai na 
# print(a.upper())
# print(a.title())# each string firsy letter upper case
# print(a.isupper())
# print(a.islower())
# print(a.istitle())
# print(a.isalpha())
# c="hello"
# print(c.isalpha())

# a="hello woRld world python"
# print(a.capitalize())## first charter upper case korce
# print(a.swapcase())##upper to lower/lower toupper
# b='GRO`'
# print(b.casefold())#more powerful lowercase in germal word
# c='Hellee'
# c=c.replace(c[-1],'o')# jekhane jekhane e ace sekhane sekhane o replace kore dicca

# print(c)
# print(c.replace('e','o')) #same 

# w='helle'
# print(w.replace('e','o',1))# 1 ta char update korbe
# o='HF34'
# print(o.isdigit())
# a=['h','e','l','l','o']
# print("".join(a)) ##join method->list to string
# b="hello"
# print(list(b)) ##() create a list each char of string
# print(b.split())##(covert  n string to n list )puro word ta kei list create korce
# a="1234"
# print(a).split()
# //string formating:(static to dynamic)
# //method 1:
# name="Rahim"
# age=10
# templete_string="I am {}.I am {} years old.".format(name,age)
# print(templete_string)

# templete_string="I am {1}.I am {0} years old.".format(age,name)
# print(templete_string)

# templete_string="I am {fname}.I am {fage} years old.".format(fname="anik",fage=20)
# print(templete_string)

# //method 2:
# str=f"i am {name}. I am {age} years old."
# print(str)
# //string concatenation:
# a=" hello"
# b="world"
# print(a+" ,"+b)
# print(a*3)
 

# //problem solving string sorting using python:
# input:x3b4U5i2
# output:bbbbiiuuuuuxxx

# a=input()
# res=""
# for i in range(0,len(a),2):
#     print(i)
#     res=res+a[i]*int(a[i+1])
# result=sorted(res.lower()) ##upper case a sort kora jai na tai lower case a convert kore nilam tarpor sort korlam
# print(result)
# print("".join(result))

# b=list(map(int,list(a)))

# print(b)
 ## list k string a convert korlam
##//check palindron:
# a=input('enter string:')
 
# # if a==a[::-1]:
 
# if a == ''.join(reversed(a)):
#     print ('palindron')
# else :
#     print('not palindron')  

# //funcion method:user define function
# def greeting():# dedine, function sin, colol
#     print ('hello')
# greeting()
# greeting()
# greeting()
# def sum(a=0,b=0):
#     print(f"the summation of {a} and {b} = {a+b}")
# sum(10,65)
# sum(10,20)
# sum(455,20)
# sum() # default parameter is called

# def greeting(name='anik',age=10):
#     print(f"hello {name}, you are {age} yours old")



# greeting()##default
# greeting("rahim",20)
# greeting(age=20,name="karim")
# def sum(a,b):
#     print(a+b) #update kora jai

# sum(2,3)    
# def sum(a,b):
#   return a+b #

 
# res=sum(2,3)
# res=res+4
# print(res)

# print(sum(2,3) ) #update kora jai
# print(sum(2,3)*3 )
# //type 1:
# def sum():
#  a=int(input('1st num:'))
#  b=int(input('1st num:'))
#  print('sum = ',a+b)
# sum() 
# //type 2:
# def addition():
#     a=3
#     b=4
#     return a+b
# res=addition()
# print(res*10)
# //type 3:
# def sum(a=0,b=0):
#     res=a+b+10
#     print (res)
# sum(10,20)  
# sum()  
# //type 4:
# def juich_meker(a,b):
#     res=f"mixture of {a} and {b} juich are ready."
#     return res
# result=juich_meker("apple","orrange")
# result2=juich_meker("banana","mango")
# print(result)
# print(result2)
# //lambda function: code less do more

# a=lambda:print("hello")
# a()
# a=lambda c,d:print("sum=",c+d)
# a(10,30)
# a=[1,2,34,6,5]
# print(len(a))
# a=1234
# print(len(str(a)))
# print(list(str(a))) # number k list a convert korte  hole:(num->str->list)

##??___________Class___________:
# class A:
#      def __init__(self):self.name='anik';self.id=241311144
#      def show(self):print(self.name);print(self.id)
# A().show()

#//del ketword(delete object):
#del s1,name->delete obj poperties

#del s1 -> delete obj
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student('anik')
# print(s1.name)
# del s1.name
# print(s1.name) ##error asbe:'Student' object has no attribute 'name'

# #//private attributes & method:
# class Account:

#     def __init__(self,acc_num,acc_pass):
#         self.acc_num=acc_num
#         self.__acc_pass=acc_pass
#     def get_pass(self):
#         return self.__acc_pass
#     def change_pass(self,acc_pass):
#         self.__acc_pass=acc_pass

    
# acc1=Account('acc123', '1bcd12')
# print("Your acc1  number is "+acc1.acc_num) 
# # print(acc1.acc_pass)## error asbe private password directly access kora jabe na
# print("Your acc1 password is "+acc1.get_pass())
# #chainge password
# acc_pass=input('Change password:')
# acc1.change_pass(acc_pass) 

# print("Your new password is ",acc1.get_pass(),"please mind it")
 



# class person:
  
#   __name="anik"

#   def __hello(self):
#     print("hello  ",self.__name)

#   def welcome(self):
#     self.__hello()

# s1=person()
# print (s1. welcome())  

#//inheritance:
# class car:
#     @staticmethod
#     def stop():
#         print("car stoped")
#     @staticmethod
#     def start():
#         print("car is started")
# class toyota(car):
#     def __init__(self,name):
#         self.name =name  

    
# car1=toyota("Toyota")
# car2=toyota("Fortune")
# print(car1.name)
# print(car1.start())
# print(car1.stop())

# print(car2.name)
# print(car2.start()) 
# print(car2.stop())

#multiple
# class A:
#     a="class a"
# class B:
#     b="class b"
# class C(A,B):
#     c="class c"
# c1=C()
# print(c1.a)
# print(c1.b)
# print(c1.c)    

#//supper method:

# class car:
#     def __init__(self,type):
#         self.type=type

#     @staticmethod
#     def stop():
#         print("car stoped")
#     @staticmethod
#     def start():
#         print("car is started")
# class toyota(car):
#     def __init__(self,name,type):
#         self.name =name 
#         super().__init__(type) 
#         super().start()
       
# car1=toyota("prius","electric")
# print(car1.type)


# class person:
#     name="sourov"
#     # def changeName(self,name):
#         #self.name=name  #change obj attributes
#         # self.__class__.name='anok'

#     @classmethod#change class attributes
#     def className(cls,name):
#         cls.name=name



# p1=person()
# p2=person()
# p1.className('rahul')
# print(p1.name) 
 
# # p1.changeName('anik')  
# # print(p1.name)
# print(person.name)


#property:\
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
        
#     @property 
#     def percentage(self):
#      return str((self.phy+self.chem+self.math)/3)+ "%"
        
# s1=Student(98,97,99)  
# print(s1.percentage)   

# s1.phy=95
# print(s1.percentage) 

# t="hello  WORLD"
# # print(t.swapcase())
# print(t.replace("hello","python"))
# text="hello python hello wowld"
# print(text.split())
# name=input('Enter name:').split()
# print(name)

# names=['Md', 'Sourov', 'Hossain', 'Anik']
# print(" ".join(names))

# str="  hello world  "
# print(str)
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())
# str="hello world"
# print(str.startswith("hello"))
# print(str.endswith("world"))
# print(str.find("world"))
# print(str.count('o'))
# print(str.isalnum())
# print(str.isalpha())
# print(str.isdigit())
# print(str.())
# import math
# print (math.factorial(5))
# print(math.fabs(-   7.5))
# print(math.floor( 7.5))
# print(math. ceil(7.5))
# print(math.pi)
# print(math.e)
# print(math.gcd(12,18))
# print(math.lcm(12,18))



