import random

def get_random_nm():
    s=""
    for i in range(random.randint(4,10)):
        c=chr(64+random.randint(1,26))
        s+=c
    return s.title()

 
def geneate_stud(no,cls_nm):
    prod_list=[]
    for i in range(1,no+1):
        s=cls_nm(sid=0+i,sname=get_random_nm(),sage=random.randint(19,26),smarks=random.randint(40,99))
        prod_list.append(s)
    return prod_list