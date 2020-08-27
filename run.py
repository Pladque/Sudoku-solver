import time
import os

######  PUBLIC VARIABLES    ##########  PUBLIC VARIABLES    #########   PUBLIC VARIABLES
                #########ROWS##############
sudoku_tab = [  8, 0, 9, 0, 0, 7, 0, 4, 0,  #
                0, 7, 1, 0, 2, 0, 0, 0, 5,  #C
                0, 4, 0, 0, 0, 0, 0, 3, 9,  #O
                6, 0, 0, 0, 0, 8, 0, 0, 0,  #L
                9, 0, 0, 4, 6, 0, 0, 0, 0,  #U
                0, 0, 2, 1, 9, 0, 8, 0, 0,  #M
                0, 6, 0, 0, 0, 0, 4, 0, 0,  #N
                0, 9, 0, 2, 8, 6, 5, 0, 0,  #S
                5, 0, 0, 0, 0, 0, 0, 0, 0,  #
              ]

posibilities = {}     # key is position and value is a list with fitting numbers
####################################################################################

#SolvingFunction
    #Solves sudoku[sudoku table must be public, 1D tab of size 9x9
    #To start you should give counter = 0; going_back = False
    #params: counter - number from 0 to 80 [ for 9x9 tab ], that represents position on sudoku_tab
    #going_back - bool, True is going back from recursion, False is going deeper in recursion
    #returns: 81 if table is solved, True if is going back from recursion because some numbers dont fit
def SudokuSolver(counter, going_back ):

    #Visual Solving
    #os.system('cls')
    #printBoard()

    if counter == 81:
        return 81  #If sudoku is solved. Returning 81 just to go back from recursion but sudoku is solved at that moment
    for num in posibilities[counter]:
        if isValueGood(counter, num):
            if going_back is False:
                sudoku_tab[counter] = num
                going_back = SudokuSolver(counter + 1, False)
            elif going_back is True and sudoku_tab[counter] != num:
                sudoku_tab[counter] = num
                going_back = SudokuSolver(counter + 1, False)

    if going_back == 81:
        return 81              #If sudoku is solved
    sudoku_tab[counter] = 0
    return True                #If any number doesnt match, going backs


#prints the board
    #return: None
def printBoard():
    for i in range(81):
        if i % 9 == 0: print()
        print(sudoku_tab[i], end='')
        print('\t', end='')
    return


#CheckRows
    #checks if a given value is in the column in which pos is located. Position of pos is ignore
    #params:pos - int, position
    #value- value that function is looking for (for sudoku purpous: value is value of number on position 'pos'
    #return: bool (T if found, else F)
def checkRowIsThereTheSameValue(pos, value):

    column = int(pos/9)
    for i in range(9):
        if sudoku_tab[i+column*9] == value and i!=pos%9:
            return True
    return False


#Check Colums
#checks if a given value is in the row in which pos is located. Position of pos is ignore
    #params:pos - int, position
    #value- value that function is looking for (for sudoku purpous: value is value of number on position 'pos'
    #return: bool (T if found, else F)
def checkColumnIsThereTheSameValue(pos, value):

    row = int(pos % 9)
    for i in range(9):
        if sudoku_tab[(i*9) + row] == value and i != int(pos/9):
            return True
    return False


#Find Square
    #Calculate in which square 'pos' is located
    #params: pos - int, position
    #return: (x,y) where x and y are square position [values from 0 to 2 for tab 9x9]
def CalculateSquares(pos):   #returns square index as tuple
    quarter_row = int((pos % 9)/3)
    quarter_column = int(int(pos/9)/3)
    return (quarter_row,quarter_column)


#Check Square
#checks if a given value is in the squre in which pos is located. Position of pos is ignore
    #params:pos - int, position
    #value- value that function is looking for (for sudoku purpous: value is value of number on position 'pos'
    #return: bool (T if found, else F)
def checkSquaresIsThereTheSameValue(pos, value):
    (quarter_row, quarter_column) = CalculateSquares(pos)
    calc_base = quarter_column*27+quarter_row*3
    for x in range(3):
        for y in range(3):
            if sudoku_tab[y*9  +calc_base +x] == value and y*9+calc_base+x != pos:
                return True
    return False


#Is Value Fitting?
    #checks if a given value is in the row, square and colums in which pos is located. Position of pos is ignore
    #params:pos - int, position
    #value- value that functions are looking for (for sudoku purpous: value is value of number on position 'pos'
    #return: bool (T if NOT FOUND, else F is FOUND)
def isValueGood(pos, value):
    if checkRowIsThereTheSameValue(pos, value) or checkColumnIsThereTheSameValue(pos, value) or checkSquaresIsThereTheSameValue(pos, value):
        return False
    return True


#Posibilities Finder and inserting values that could have only one possible value
    #finding all possible values that can be set to sudoku_tab for every position
    #params: none
    #return: none
def insertIfSureAndFindPosibleNumbers():
    number_of_matching = 0
    matching_value = 0
    for pos in range(81):
        temp_list_values = []
        if sudoku_tab[pos] == 0:
            for value in range(9):
                value+=1            #because i want to start from 1 to 9
                if isValueGood(pos, value):
                    number_of_matching += 1
                    matching_value = value
                    temp_list_values.append(matching_value)
            if number_of_matching == 1:     #if found only one matching value to pos than insert value to that pos
                sudoku_tab[pos] = matching_value
            posibilities[pos] = temp_list_values
        else:
            posibilities[pos] = [sudoku_tab[pos]]
        number_of_matching=0
    return


def start_timer():
    return time.time()


#Printing how much time sudoku took
    #params: t0 - time when program started
    #return: none
def print_timer(t0):
    print()
    print("it took:")
    print(time.time() - t0)
    input()


#Solve Sudoku
    #params: none, but sudoku tab has to be public vairable and dictionary 'posibilities' to save possible values
    #return: none
def SolveSudoku():
    insertIfSureAndFindPosibleNumbers()
    SudokuSolver(0, False)


#Print Sudoku Tab
    #params: t0 - time when program started
    #sudoku tab has to be public vairable and dictionary 'posibilities' to save possible values
    #return: none
def print_results(t0):
    os.system('cls')
    printBoard()
    print_timer(t0)

#Start timer, solve sudoku, and show results
    #params: none
    #sudoku tab has to be public vairable and dictionary 'posibilities' to save possible values
    #return: none
def main():
    t0 = start_timer()
    SolveSudoku()
    print_results(t0)


#Start here
print("If you are running this not in IDE, that may makes some issues")
input("press any key to start solving sudoku")
main()






