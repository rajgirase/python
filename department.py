
from basefile import Baseclass

class Department(Baseclass):
    
    def __init__(self,did,dname,dhod):
        self.dept_Id=did
        self.dept_name=dname
        self.dept_hod=dhod
        self.studen=[]
        self.stud_no= None
        