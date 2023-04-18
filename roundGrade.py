# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:01:35 2023

@author: tommaso
"""
import numpy as np

def roundGrade(grades): #if the number is exactly halfway, it rounds it to the higher grade

    grades_2decimal=np.round(grades,2)# converts all numbers to a 2 decimal number
    
    gradesRounded=np.zeros(len(grades))# creates an array of zeros with the same size as the input array
    
    
    for i in range(len(grades)):# analyzes all the numbers in the input array and adds the corresponding grade
    #of the 7-step scale in the output array
        if grades_2decimal[i]>-3 and grades_2decimal[i]<-1.5 :
            gradesRounded[i]=-3
            
        if grades_2decimal[i]>=-1.5 and grades_2decimal[i]<1:
            gradesRounded[i]=0
            
        if grades_2decimal[i]>=1 and grades_2decimal[i]<3:
            gradesRounded[i]=2
            
        if grades_2decimal[i]>=3 and grades_2decimal[i]<5.5:
            gradesRounded[i]=4
            
        if grades_2decimal[i]>=5.5 and grades_2decimal[i]<8.5:
            gradesRounded[i]=7
            
        if grades_2decimal[i]>=8.5 and grades_2decimal[i]<11:
            gradesRounded[i]=10
            
        if grades_2decimal[i]>=11 and grades_2decimal[i]<=12:
            gradesRounded[i]=12
            
    gradesRounded=np.intc(gradesRounded)    # converts the output array into an array of integers                  
    
    return gradesRounded
