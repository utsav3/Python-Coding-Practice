# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 20:10:22 2018

@author: utsav
"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QPushButton, QLineEdit , QLabel, QListWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot
import random
import itertools
import os



class boggle_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup()
        
    def setup(self):
        self.setWindowTitle("Boggle Game")
        self.setToolTip("Play the boggle game")
        
        
        self.boggle_game= boggleGame(self)
        self.setCentralWidget(self.boggle_game)
        
        exit_action = QtWidgets.QAction('Exit', self)
        exit_action.triggered.connect(QtWidgets.qApp.quit)
        
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_action)
        
        self.show()
        
    def closeEvent(self, event):
        reply = QuitMessage().exec_()
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class boggleGame(QtWidgets.QWidget):
    list_of_words = []
    grid_2d_list = []
    def __init__(self,parent):
        QtWidgets.QWidget.__init__(self,parent)
        self.setup()
            
    def setup(self):
        self.board = boggleBoard(self)
        self.new_btn = StartNewGameBtn(self)
        self.quit_btn = quitBtn(self)
        #ADD WORDS BUTTON        
        self.add_wordBtn = add_wordBtn(self)
        #SCORE BUTTON
        self.score_Btn = scoreBtn(self)
        
        self.grid = QtWidgets.QGridLayout()
        
        self.grid.addWidget(self.board, 6, 6, 1, 1)
    
        
        #2d List
        #Gets the list of chars from 4 random faces
        self.grid_2d_list = rollDice()
        
        #Flat 1d list
        flat_list = []
        flat_list = list(itertools.chain.from_iterable(self.grid_2d_list))        

        grid_char_list = []                    
        for i in range(0,4):
            for j in range(0,4):
                index = i*4+j
                grid_char_list.append(flat_list[index])
                self.grid.addWidget(QPushButton(flat_list[index]),i+1,j+1)
        #print(grid_2d_list)
        self.setLayout(self.grid)
        self.grid.addWidget(self.new_btn, 6, 1, 1, 1)
        self.grid.addWidget(self.quit_btn, 6, 2, 1, 1)        
        self.grid.addWidget(self.add_wordBtn, 5, 4, 1, 1)        
        self.grid.addWidget(self.score_Btn, 6, 4, 1, 1)        
        
        
        #TEXT BOX
        self.words_label = QLabel(self)
        self.words_label.setText("Enter Words::")
        self.words_label.move(10,140)
        self.textbox = QLineEdit(self)
        self.textbox.move(100,145)
        self.textbox.resize(200,40)
        
        
        #LIST BOX
        self.word_listbox = QListWidget(self)
        self.word_listbox.move(500,10)
        self.word_listbox.resize(280,280)
        self.word_listbox.addItem(self.textbox.text())

        self.score_Btn.clicked.connect(self.score_onClick)       
        self.add_wordBtn.clicked.connect(self.add_onClick)
        
    def add_onClick(self):   
        word = self.textbox.text()
        if not word:
            return
        self.textbox.clear()
        self.word_listbox.addItem(word)
        self.list_of_words.append(word)
        #print(self.list_of_words)
        
    def score_onClick(self):
        total_points = user_words(self.grid_2d_list,self.list_of_words)
        msg_box= QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText('Your total score is {}'.format(total_points) 
            + ' points \n Play Again?')
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval=msg_box.exec()
        
        if retval == msg_box.Yes:
            restart_program()
        else:
            QtWidgets.qApp.quit()
            

        
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)        
        
def rollDice():
    #ROLL DICE STARTS HERE
    dice_faces = ['a','e','a','n','e','g',
                  'a','h','s','p','c','o',
                  'a','s','p','f','f','k',
                  'o','b','j','o','a','b',
                  'i','o','t','m','u','c',
                  'r','y','v','d','e','l',
                  'l','r','e','i','x','d',
                  'e','i','u','n','e','s',
                  'w','n','g','e','e','h',
                  'l','n','h','n','r','z',
                  't','s','t','i','y','d',
                  'o','w','t','o','a','t',
                  'e','r','t','t','y','l',
                  't','o','e','s','s','i',
                  't','e','r','w','h','v',
                  'n','u','i','h','m','qu']
    return gridGen(dice_faces)
        
def gridGen(dice_faces):
    dice_list = []
    list_of_list = []
    random_index_list = list(range(0,16))
    random.shuffle(random_index_list)
    l_index = 0
    for i in range(0,4):
        l_index = l_index+4
        random_index=random_index_list.pop()        
        
        index = random_index * 6    
        if (index<=90):
            for i in range (0,4):
                dice_list.append(dice_faces[index])
                index = index+1
            list_of_list.append(dice_list[l_index-4:l_index])

    return list_of_list

def user_words(listoflist, word_list):
        for word in word_list:
            check_validity = valid_word(word)
            if not check_validity:
                word_list.remove(word)
        word_list = list(set(word_list))
        return calc_points(listoflist,word_list)
        #print(*word_list)
    

def valid_word(word):
    file = open ("words.txt")
    strings = file.read().splitlines()
    if word in strings:
        if len(word)>2:
            return True
        else:
            print('Word should be more than 2 letters. Enter again!')
    elif word.lower() == 'x':
        return False
    else:
        print('is not valid word. Enter again!')
        return False
    
def calc_points(in_grids, input_words):
        points = 0
        for j in range(0, len(input_words)):
            if find_word(input_words[j], in_grids):
                    if len(input_words[j]) == 3 or len(input_words[j]) == 4:
                        print('The word ', input_words[j], 'is worth 1 point')
                        points += 1
                    if len(input_words[j]) == 5:
                        print('The word ', input_words[j], 'is worth 2 point')
                        points += 2
                    if len(input_words[j]) == 6:
                        print('The word ', input_words[j], 'is worth 3 point')
                        points += 3
                    if len(input_words[j]) == 7:
                        print('The word ', input_words[j], 'is worth 5 point')
                        points += 5
                    if len(input_words[j]) >= 8:
                        print('The word ', input_words[j], 'is worth 11 point')
                        points += 11 
            else:
                print('The word ', input_words[j], 
                      'is not present in the grid.')
        return points
    
def find_word(input_word, input_grid):
    for row in range(0, len(input_grid)):
        for col in range(0, len(input_grid)):
            if check_grid_word(input_word, row, col, input_grid):
                return True
    return False


def check_grid_word(word, row, col, input_grid):
    if word == '':
        return True
    elif row<0 or row>=4 or col<0 or col>=4 or word[:1] != input_grid[row][col]:
        return False
    else:
        char = input_grid[row][col]
        input_grid[row][col] = '*'
        rest = word[1:len(word)]
        result = check_grid_word(rest, row-1, col-1, input_grid) \
            or check_grid_word(rest, row-1, col, input_grid)   \
            or check_grid_word(rest, row-1, col+1, input_grid) \
            or check_grid_word(rest, row, col-1, input_grid)   \
            or check_grid_word(rest, row, col+1, input_grid)   \
            or check_grid_word(rest, row+1, col-1, input_grid) \
            or check_grid_word(rest, row+1, col, input_grid)   \
            or check_grid_word(rest, row+1, col+1, input_grid) \
            
        input_grid[row][col] = char
        return result
    

    
class boggleBoard(QtWidgets.QWidget):
    def __init__(self , parent):
        QtWidgets.QWidget.__init__(self, parent)        
        self.setFixedSize(400,260)
            
                        

class QuitMessage(QtWidgets.QMessageBox):
    def __init__(self):
        QtWidgets.QMessageBox.__init__(self)
        self.setText("Do you really want to quit?")
        self.addButton(self.Yes)
        self.addButton(self.No)

class StartNewGameBtn(QtWidgets.QPushButton):
    def __init__(self,parent):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Start New Game")
        self.move(150,360)
        
class scoreBtn(QtWidgets.QPushButton):
    def __init__(self,parent):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Score")
        self.move(350,100)
        
class add_wordBtn(QtWidgets.QPushButton):
    def __init__(self,parent):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Add Word")
        self.move(350,60)
    
class quitBtn(QtWidgets.QPushButton):    
    def __init__(self,parent):
        QtWidgets.QPushButton.__init__(self,parent)        
        self.setText("Quit")        
        self.move(150,160)        
        self.clicked.connect(QtWidgets.qApp.quit)        
        self.setToolTip("Close the Boggle game.")
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = boggle_window()
    app.exec_()