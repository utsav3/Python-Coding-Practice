# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:27:39 2018

@author: utsav
"""
import csv


def read_csv():
    '''
        Reads the csv file to find the min diff
        between the quizzes 5 and 6
    '''
    try:
        csv_reader = csv.reader(open('class.csv', 'r'))
    except IOError:
        print("File not Found")
    quiz5 = 0
    quiz6 = 0
    diff_score = []
    names=[]
    next(csv_reader)
    for row in csv_reader:
        quiz5 = row[5]
        quiz6 = row[6]
        diff_score.append(abs(int(quiz5)-int(quiz6)))
        names.append(row[0])
    min_score = min(diff_score)
    print(names[diff_score.index(min_score)])
read_csv()