class Student(object):
    grade={
        'exam_max':100,
        'lab_max':15,
        'lab':10.5,
         'k':0.7,
    }    
    def __init__(self,name: str,grade: float ):
        self.name=name
        self.grade=grade

    def times_exam(self, tim: int, lev:float):
        print(f'times:{tim}\n level:{lev}')
    def times_lab(self, time=int, lab=float):
        print(f'Time:{time}\n Laba:{lab}')

student=Student("Andrey", 4)        
student.times_exam(8,5)
student.times_lab(3,6)
