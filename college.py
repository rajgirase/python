from basefile import Baseclass
class College(Baseclass):
    def __init__(self,cid,cname,prin_name,num_stud):
        self.clg_Id=cid
        self.clg_name=cname
        self.princi_name=prin_name
        self.stud_num=num_stud
        self.dept=[]

if __name__=="__main__":
    c=College(101,"dypatil","raj",98)
    print(c)


    
        