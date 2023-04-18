# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:20:38 2023

@author: tommaso
"""
import numpy as np
import pandas as pd
from roundGrade import roundGrade


def computeFinalGrades(grades):  #matrix NxM with N students and M assignments
    gradesFinal=np.zeros(len(grades))
    
    for i in range (len(grades)):
        student_grades=grades[i]
        rounded_grades=roundGrade(student_grades)
        
        assignments=len(grades[0])
        
            
        if assignments== 1:
                
            gradesFinal[i]=rounded_grades[i]
                
        if assignments>1:
            
            min_index=rounded_grades.argmin()
            
            np.delete(rounded_grades,min_index)
            
            temporary_mean=np.array([np.mean(rounded_grades)])
            
            gradesFinal[i]=roundGrade(temporary_mean)
            
        if -3 in rounded_grades:
            
            gradesFinal=-3
    gradesFinal=np.intc(gradesFinal)
            
    return gradesFinal

print(computeFinalGrades([[-1.5,-0.7,1],[7.5,4.7,8.8],[3]]))
