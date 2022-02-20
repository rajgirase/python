from basefile import Baseclass
class Student(Baseclass):
    def __init__(self,sid,sname,sage,smarks):
        self.stud_id=sid
        self.stud_name=sname
        self.stud_age=sage
        self.stud_marks=smarks
        self.stud_sub=[]