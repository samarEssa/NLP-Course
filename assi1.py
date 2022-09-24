# import random
# number = int(input())
# for i in range(number)  :
#  GN=random.randint(0,number)
#  print(GN)

# import random
# passlen = int(input("enter the length of password"))
# s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# p = "".join(random.sample(s,passlen ))
# p1 = random.sample(s,passlen )# method sample create a list 
# print(p1)
# print(p)

# from tkinter import END


# while True:
#     i=input("Enter Text :") 
#     if i == 'stop':break
#     print(i)


# while True:
#     reply = input("Enter Text: ")
#     if reply == 'stop': break
#     print(reply)
# from ast import Add

 #list odd numbers 1-200
for i in range(1,201):
    if i %2 != 0 :
        print(i)
# creat list of name 
Name =["ahmed","ali","mohamed","Asmaa","Shimaa","Fatma"]
Name.insert(0,"sahar")
Name.insert(7,"suha")
#creat list of age 
Age=[20,25,18,30,35,20]
Age.insert(0,30)
Age.insert(2,25)
print(Age)
#spilt list of name 
mid_id=4
first_list=Name[:mid_id]
secand_list=Name[mid_id :]
print(first_list)
print(secand_list)
# creat a dic
my_dic=dict(zip(Name,Age))
print(my_dic)