# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:37:26 2018

@author: utsav
"""

import random

def rollDice():
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
    face1 = gridGen(dice_faces)
    face2 = gridGen(dice_faces)
    face3 = gridGen(dice_faces)
    face4 = gridGen(dice_faces)
    grid_list = []
    listoflist = []
    for i in range (0,4):
        grid_list.append(random.choice(face1))
        grid_list.append(random.choice(face2))
        grid_list.append(random.choice(face3))
        grid_list.append(random.choice(face4))
        
    for i in range(0,4):
        index = i*4
        listoflist.append(grid_list[index:index+4])
        print(*grid_list[index:index+4])
    #print(*listoflist)
    user_words(listoflist)

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
    
    
def user_words(listoflist):
    print("Start typing your words! (press enter \
        after each word and enter 'X' when done)" )
    word_list = []
    word = ""
    while (word != 'X' and word != 'x'):
        word = input()
        word= word.lower()
        check_validity = valid_word(word)
        if check_validity:
            word_list.append(word)
    word_list = list(set(word_list))
    calc_points(listoflist,word_list)
    print(*word_list)
    
    
    
def gridGen(dice_faces):
    dice_list = []
    index = random.randint(0,16) * 6    
    if (index<=90):
        for i in range (0,6):
            dice_list.append(dice_faces[index])
            index = index+1
    return dice_list
        


def calc_points(in_grids, input_words):
        points = 0
        print(in_grids)
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
        print('Your total score is ', points, 'points')
    
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

if __name__ == '__main__':
    rollDice()