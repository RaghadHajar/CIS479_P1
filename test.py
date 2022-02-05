import pprint
import Puzzle as p

#Step 1 Build Puzzle
InitialBoard = p.Puzzle.Board()
OtherBoard = p.Puzzle.Board()
InitialVector = [8,2,1,5,"-",4,7,3,6]
InitialBoard.fnPopulateBoard(InitialVector)

#Step 2 Set Goal
GoalBoard = p.Puzzle.Board()
GoalVector = [1,2,3,4,"-",5,6,7,8]
GoalBoard.fnPopulateBoard(GoalVector)

#Step 3
#Calculate current H
print(InitialBoard.fnCalculateH(GoalBoard))
print(InitialBoard.fnFindPossibleMoves(GoalBoard))
#Step 4 
#Find all possible moves
#Part a Move to the West cost 2
#ai Calculate G to make this move
#aii Calculate what H would be if the board changed so you could make this Move
#aiii Calculate f (g + h) of this move
#aiv Add f-value to frontier set position 1

#Part b Move to the North cost 1
#ai Calculate G to make this move
#aii Calculate what H would be if the board changed so you could make this Move
#aiii Calculate f (g + h) of this move
#aiv Add f-value to frontier set position 2

#Part c Move to the East cost 2
#ai Calculate G to make this move
#aii Calculate what H would be if the board changed so you could make this Move
#aiii Calculate f (g + h) of this move
#aiv Add f-value to frontier set position 3

#Part d Move to the South cost 3
#ai Calculate G to make this move
#aii Calculate what H would be if the board changed so you could make this Move
#aiii Calculate f (g + h) of this move
#aiv Add f-value to frontier set position 4

#Step 5 sort frontier set
#Cost in ascending order
#Step order # in ascending order 

#Step 6 pop FIFO value from frontier set

#Step 7 use popped value to create new table
##Increase current G to += self.gFunctionValue from previous state 
##Recalculate H value store in self.hFunctionValue
##Increase self.ExpansionSetNum by 1


#Step 8 add board as (Board.ExpansionSetNum, Board) in Hashtable (dictionary)

#Go to step 3

#continue until board == goal board

ExpansionSet = {InitialBoard.ExpansionSetNum : InitialBoard,InitialBoard.ExpansionSetNum + 1 : GoalBoard}

for board in ExpansionSet.values():
    print(board)
