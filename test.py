import pprint
import Puzzle as p
import heapq

def heapsort(iterable):
        h = []
        for value in iterable:
            heapq.heappush(h, value)
        return [heapq.heappop(h) for i in range(len(h))]

#Step 1 Build Puzzle
InitialBoard = p.Puzzle.Board()
OtherBoard = p.Puzzle.Board()
InitialVector = ["-",1,2,3,4,5,6,7,8]
"""
print("HELLO! \n" +
    "Welcome to the wonderful puzzle solver! \n +"
    "This code was made by Raghad and Steven \n +")
UserInput = input("We would like you to send us a vector of size 9") 
if UserInput is None:
    pass
InitialBoard = UserInput
"""
InitialBoard.fnPopulateBoard(InitialVector)
ExpansionSet = {InitialBoard.ExpansionSetNum : InitialBoard}

#Step 2 Set Goal
GoalBoard = p.Puzzle.Board()
GoalVector = [1,2,3,4,"-",5,6,7,8]
GoalBoard.fnPopulateBoard(GoalVector)

#Step 3
#Calculate current H
InitialBoard.fnCalculateH(GoalBoard)

while InitialBoard != GoalBoard:
    #Step 4 
    #Find all possible moves
    FrontierSet = InitialBoard.fnFindPossibleMoves(GoalBoard)
    
    #Step 5 sort frontier set
    #Cost in ascending order
    #Step order # in ascending order 
    FrontierSet = heapsort(FrontierSet)
    heapq.heapify(FrontierSet)
    
    #Step 6 pop FIFO value from frontier set
    #Step 7 use popped value to create new table
    ##Increase current G to += self.gFunctionValue from previous state 
    ##Recalculate H value store in self.hFunctionValue
    ##Increase self.ExpansionSetNum by 1
    BestMove = heapq.heappop(FrontierSet)
    while BestMove.NewBoard in ExpansionSet.values():
        BestMove = heapq.heappop(FrontierSet)
        BestMove.NewBoard.fnCalculateH
    #Step 8 add board as (Board.ExpansionSetNum, Board) in Hashtable (dictionary)
    
    ExpansionSet.update({BestMove.NewBoard.ExpansionSetNum : BestMove.NewBoard})
    #Go to step 3
    
    #continue until board == goal board
    InitialBoard = BestMove.NewBoard
    
    #
for board in ExpansionSet.values():
    print(board)
