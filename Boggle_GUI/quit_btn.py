# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 20:57:31 2018

@author: utsav
"""

class quit_btn(QtWidgets.QPushButton)    
    def __init__(self,parent):
        QtWidgets.QPushButton.__init__(self, parent)        
        self.setText("Quit")        
        self.move(150,160)        
        self.clicked.connect(QtWidgets.qApp.quit)        
        self.setToolTip("Close the triangle peg game.")
