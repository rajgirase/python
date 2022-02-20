# oops --
#    inheritance    Like father property to its children
#    encapsulation    eg class---methods and variables
#    abstraction    data hiding from end user
#    polymorphism    one thing many form like +  --concatenate and addi
#########################################################

import math
import random
from typing import Counter, List
from department import Department
from college import College
from subjects import Subject
from student import Student
from utility import geneate_stud

c=College(101,"dypatil","raj",20)
d1=Department(10,"science","raj")
d2=Department(11,"IT","ram")
d3=Department(12,"Eng","vishu")
d4=Department(13,"hindi","roshni")
c.dept.extend([d1,d2,d3,d4])
# print(c)

stud=geneate_stud(20,Student)
# print(stud)

d1.studen.extend(stud[0:5])
d2.studen.extend(stud[5:10])
d3.studen.extend(stud[10:15])
d4.studen.extend(stud[15:21])
# print(d1)
# print(d4)


depts=[d1,d2,d3,d4]

for d in depts:  
    d.stud_no=len(d.studen)

# print(d1)
# print(d2)
# print(d3)
# print(d4)


subject_list=["science","maths","english","mechanics","graphic","physics"]
s1=Subject(101,subject_list[0],True)
s2=Subject(102,subject_list[1],False)
s3=Subject(103,subject_list[2],False)
s4=Subject(104,subject_list[3],True)


list1=[s1,s2,s3,s4]

##########################################################
# random.shuffle(list1)
# print(list1[0:random.randint(1,4)]
#############################################################

for i in stud:
    
    random.shuffle(list1)
    rndom_sub=list1[0:random.randint(1,4)]

    i.stud_sub.extend(rndom_sub)
    # print(i, end="\n")

# print(c)
# import json
# r=json.dumps()
# print(r)
######################################################
# print(c.dept)

# for dep in c.dept:
#     for std in dep.studen:
#         print(std.stud_id)

###########################################


# for dep in c.dept:
#     print(f"--------------------Depart:{dep.dept_name}-----------------")

#     for std in dep.studen:
#         print(f"-----------------Stude:{std.stud_name}---------------------------")
#         print(std.stud_sub)
    

# def get_dept(depp):
#     for dpt in c.dept:
            
#         if dpt.dept_name == depp:
#             print(dpt.studen)
            
# get_dept("Eng")




##################################################

# def get_subject(subb):
#     maths_stud=[]
#     for dpt in c.dept:
#         for std in dpt.studen:
#             l=list(map(lambda x:x.sub_name,std.stud_sub))
#             if subb in l:
#                 maths_stud.append(std)
#             print(maths_stud,len(maths_stud))
# get_subject("maths")
    
####################Any Function#################################

""">>> l=[1,2,3,4]
>>> any(l)
True
>>> l=[]
>>> any(l)
False
>>> l=[1,2,0,0,0]
>>> any(l)
True
>>> l=[0,0,0]
>>> any(l)
False
>>> l=[1,0,0,0]
>>> any(l)
True
>>>
"""





####################Assignment 5#####################################


####Startwith method
        
# def get_stud_startname():
#     for i in c.dept:
#         for s in i.studen:
#             p=s.stud_name
#             nm=p.startswith("A")
#             if nm==True:
#                 print(p)
            
                

# res=get_stud_startname()


###############################Average Marks in Subject#################################################


# def num_of_stud(nm):
#     lst_sub=[]
#     add=0
#     for d in c.dept:
#         for i in d.studen:
#             for s in i.stud_sub:
#                 if s.sub_name==nm:
#                     lst_sub.append(s)
#                     Total=i.stud_marks
#                     add+=Total
    
                                    
#     avg=add/len(lst_sub)
#     print(f"Subject is:--{nm} and its average:--{avg}")


# res=num_of_stud("maths")



###########################Type######################################

# def get_dept(depp):
#     # print(type(depp))
#      for dpt in c.dept:    
#          if dpt.dept_name in depp:
#              if type(depp)==str:
#                  print("------------Str type----------------")
#                  print(dpt.studen)
#              elif type(depp) == list:
#                  print("-------------List type-----------------")
#                  print(dpt.studen)
                         
# get_dept(["Eng","IT"])



###################################num of Student Subject###########################################

# def num_of_stud(nm):
#     lst_sub=[]
#     add=0
#     for d in c.dept:
#         for i in d.studen:
#             for s in i.stud_sub:
#                 if s.sub_name==nm:
#                     lst_sub.append(s)


#     print(lst_sub,len(lst_sub))

# res=num_of_stud("science")

###########################Marks greater than 50#######################################

# def stud_marks():
#     lst_sub=[]
    
#     for d in c.dept:
#         for i in d.studen:
#             if i.stud_marks>=50:
#                 lst_sub.append(i)

    
#     print(lst_sub)



# res=stud_marks()









######################################################################################


#CRUD Operation--Create,Read,Update,Delete

from basefile import Baseclass
class amazon(Baseclass):
    prod_list=[]
    def __init__(self,pid,pname,pcat,pprice,pqty):
        self.prodid=pid
        self.prodname=pname
        self.prodcat=pcat
        self.prodprice=pprice
        self.prodqty=pqty
    @classmethod
    def get_all_prod(cls):
        return cls.prod_list
    @classmethod
    def get_all_id(cls):
        ids_list=list(map(lambda x: x.prodid,cls.prod_list)) 
        return ids_list   
    @classmethod
    def get_single_prod(cls,pid):        
        if pid in cls.get_all_id():

            for prod in cls.prod_list:
                if prod.prodid==pid:
                    return prod
        else:
            return "ID not present"
    @classmethod
    def del_all_product(cls):
        cls.prod_list.clear()
        return cls.prod_list
    @classmethod
    def del_single_prod(cls,pid):
        for p in cls.prod_list:
            if p.prodid==pid:
                cls.prod_list.remove(p)
                break
        return cls.prod_list        
    @classmethod            
    def udate_prod(cls,pid,data):
        for i in cls.prod_list:
            if i.prodid==pid:
                if data.get("prodname"):
                    i.prodname=data.get("prodname")
                    
                if data.get("prodcat"):
                    i.prodcat=data.get("prodcat")      
                if data.get("prodprice"):
                    i.prodprice=data.get("prodprice")
                if data.get("prodqty"):
                    i.prodqty=data.get("prodqty")
        return cls.prod_list

a1=amazon(101,"mobile","electronic",34500,5)
a2=amazon(102,"laptop","electronic",4500,5)
a3=amazon(103,"ac","electronic",12000,5)

amazon.prod_list.extend([a1,a2,a3])
# print(amazon.get_all_prod())

############################################
# print(a1)

# amazon.prod_list.append(a1)
# print(amazon.prod_list)

# amazon.prod_list.extend([a1,a2,a3])
# print(amazon.prod_list)
###############################################################


# print(amazon.get_single_prod(104))

# print(amazon.del_single_product())

# print(amazon.del_single_prod(102))

# print(amazon.udate_prod(102,{"prodname":"fridge"}))

# print(amazon.udate_prod(105,{"prodname":"fridge"}))

# print(amazon.udate_prod(102,{"prodname":"milk","prodcat":"Grocery"}))






