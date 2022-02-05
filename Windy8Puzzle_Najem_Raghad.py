import heapq
import math

class Puzzle: #Raghad and #Najem
    """This is the class that holds the whole game"""

    class MinPQ:
        """A minimum priority queue. 
        Can be used for ordering h(n), selecting f(n) and must be used for the frontier set
        As directed by the professor we do not have to build from scrath
        use an implementation of heapq. Library info found here:"""
        ##https://docs.python.org/3/library/heapq.html """

        def __init__(self):
            self.pq = heapq
    
    class Move:
        def __init__(self
        ,StartingIndex = ()
        ,NewIndex = ()
        ,InitialOrder = 0
        ,PuzzleNum = '-'
        ,PuzzleGoalIndex = ()
        ,GValue = 0
        ,HValue = 0
        ,FValue = 0 
        ):
            self.InitialOrder = InitialOrder 
            self.StartingIndex = StartingIndex
            self.NewIndex = NewIndex
            self.PuzzleNum = PuzzleNum
            self.PuzzleGoalIndex = PuzzleGoalIndex
            self.GValue = GValue
            self.HValue = HValue
            
        def __gt__(self):
            pass
        
        def __eq__(self):
            pass
        
        def __lt__(self):
            pass
        
        def fnFindGoalIndex(self, GoalBoard):
            self.PuzzleGoalIndex = GoalBoard.fnFindBlank()
            

    class Board:
        """Class to store all board types and related functions"""
        def __init__(self,NumRow=3,NumCol=3): #initial state
            self.arrayBoard = [[0]*NumCol for i in range(NumRow)]
            self.fFunctionValue = 0 #Doesn't map
            self.gFunctionValue = 0  #Maps to left
            self.hFunctionValue = 0  #Maps to right
            self.ExpansionSetNum = 1 #Bottom Row with a # before the number ex #1
            self.BoardOutput = ""
            self.FrontierSet = []#MinPQ
            
        def __repr__(self):
            for row in range(len(self.arrayBoard)):
                if row == 0:
                    self.BoardOutput = "_"*len(self.arrayBoard)*4 + "\n"
                for col in range(len(self.arrayBoard[row])):
                    if col == 0:
                        self.BoardOutput += "| "
                    self.BoardOutput += " " + str(self.arrayBoard[row][col]) + " "
                    if row == len(self.arrayBoard) and col == len(self.arrayBoard[row]):
                        self.BoardOutput += "_"*len(self.arrayBoard)*4
                    if col == len(self.arrayBoard[row]):
                        self.BoardOutput += "|"
                self.BoardOutput += " |\n"
            self.BoardOutput += "_"*len(self.arrayBoard)*4 + "\n"
            self.BoardOutput += "|" + "  "
            self.BoardOutput += str(self.gFunctionValue)
            self.BoardOutput += "  " + "|" + "  "
            self.BoardOutput += str(self.hFunctionValue)
            self.BoardOutput += "  "+ "|\n"
            self.BoardOutput += "_"*len(self.arrayBoard)*4
            self.BoardOutput += "\n"
            self.BoardOutput += " "*(len(self.arrayBoard)+2)
            self.BoardOutput += "#"
            self.BoardOutput += str(self.ExpansionSetNum)
            self.BoardOutput += " "*len(self.arrayBoard)
            return self.BoardOutput
                        
        def __eq__(self, OtherBoard): #comparing goal and initial 
            listTruthValues = []
            if (len(self.arrayBoard) == len(OtherBoard.arrayBoard)):
                for row in range(len(self.arrayBoard)):
                    for col in range(len(self.arrayBoard[row])):
                        if self.arrayBoard[row][col] != OtherBoard.arrayBoard[row][col]:
                            return False
                        else:
                            listTruthValues.append((row,col))
                if len(listTruthValues) == len(self.arrayBoard) * len(self.arrayBoard[0]):
                    return True
            else:
                return False
                
        def __setattr__(self,Name,Value):
            self.__dict__[Name] = Value
            
        def fnPopulateBoard(self, listPuzzleNum):
            """Enter the positions of the arrayBoard by using a vector
            of the Puzzle Numbers (listPuzzleNum)
            Send it in the order of top left to bottom right
            Don't forget the '-' blank value
            """
            if len(listPuzzleNum) % len(self.arrayBoard) != 0:
                print("The length of the list is incorrent")
            else: 
                for indexPuzzleNum in range(len(listPuzzleNum)):
                    RowNum = indexPuzzleNum // len(self.arrayBoard)
                    ColNum = indexPuzzleNum % len(self.arrayBoard)
                    self.arrayBoard[RowNum][ColNum] = listPuzzleNum[indexPuzzleNum]
    
        def fnFind(self, PuzzleNum):
            for row in range(len(self.arrayBoard)):
                for col in range(len(self.arrayBoard[row])):
                    if PuzzleNum == self.arrayBoard[row][col]:
                        IndexPosition = (row, col)
                        return (IndexPosition)
                else:
                    next
                    
        def fnFindBlank(self):
            IndexPosition = self.fnFind("-")
            return IndexPosition
            
        def fnSwap(self, IndexStart, IndexEnd):
            BeginRow    =   IndexStart[0]
            BeginCol    =   IndexStart[1]
            EndRow      =   IndexEnd[0]
            EndCol      =   IndexEnd[1]
            SwapBoard = copy.deepcopy(self)
            SwapBoard.arrayBoard[EndRow][EndCol] = self.arrayBoard[BeginRow][BeginCol]
            SwapBoard.arrayBoard[BeginRow][BeginCol] = self.arrayBoard[EndRow][EndCol]
            return SwapBoard
            
        def fnFindPossibleMoves(self, tupleIndex=()):
            """ Check for the possible movesets in the directed way:
            West, North, East, South
            Col - 1, Row - 1, Col + 1, Row + 1
            Update frontier set PQ with possible moves.
            """
            Move1 = Move()
            Move2 = Move()
            Move3 = Move()
            Move4 = Move()
            
            if tupleIndex == ():
                IndexPosStart = self.fnFindBlank()
            else:
                IndexPosStart = tupleIndex
            BlankRow = IndexPosStart[0]
            BlankCol = IndexPosStart[1]
            
            Move1 = Move(
                StartingIndex = (BlankRow, BlankCol)
                ,InitialOrder = 1)
            Move2 = Move(
                StartingIndex = (BlankRow, BlankCol)
                ,InitialOrder = 2)
            Move3 = Move(
                StartingIndex = (BlankRow, BlankCol)
                ,InitialOrder = 3)
            Move4 = Move(
                StartingIndex = (BlankRow, BlankCol)
                ,InitialOrder = 4)
            
            if BlankCol != 0: #skip west if border
                Move1.GValue = self.gFunctionValue + 2
                Move1.NewIndex = (BlankRow, BlankCol - 1)
                Move1.PuzzleNum = self.arrayBoard[Move1.NewIndex[0]][Move1.NewIndex[1]]
                PossibleExpansionSet1 = self.fnSwap(IndexPosStart, Move1.NewIndex)
                Move1.HValue = PossibleExpansionSet1.fnCalculateH()
                Move1.FValue = Move1.HValue + Move1.GValue
                ### Add function call to add to PQFrontier both the move and the cost###
            
            if BlankRow != 0: #skip north if border
                Move2.GValue = self.gFunctionValue + 1
                Move2.NewIndex = (BlankRow - 1, BlankCol)
                Move2.PuzzleNum = self.arrayBoard[Move2.NewIndex[0]][Move2.NewIndex[1]]
                PossibleExpansionSet2 = self.fnSwap(IndexPosStart, Move2.NewIndex)
                Move2.HValue = PossibleExpansionSet2.fnCalculateH()
                Move2.FValue = Move2.HValue + Move2.GValue
                ### Add function call to add to PQFrontier both the move and the cost###
                
            if BlankCol != len(self.arrayBoard[0]) - 1: #skip east if border
                Move3.GValue = self.gFunctionValue + 2
                Move3.NewIndex = (BlankRow, BlankCol + 1)
                Move3.PuzzleNum = self.arrayBoard[Move3.NewIndex[0]][Move3.NewIndex[1]]
                PossibleExpansionSet3 = self.fnSwap(IndexPosStart, Move3.NewIndex)
                Move3.HValue = PossibleExpansionSet3.fnCalculateH()
                Move3.FValue = Move3.HValue + Move3.GValue
                ### Add function call to add to PQFrontier both the move and the cost###
            
            if BlankRow != len(self.arrayBoard) - 1: #skip south if border
                Move4.GValue = self.gFunctionValue + 3
                Move4.NewIndex = (BlankRow + 1, BlankCol)
                Move4.PuzzleNum = self.arrayBoard[Move4.NewIndex[0]][Move4.NewIndex[1]]
                PossibleExpansionSet4 = self.fnSwap(IndexPosStart, Move4.NewIndex)
                Move4.HValue = PossibleExpansionSet4.fnCalculateH()
                Move4.FValue = Move4.HValue + Move4.GValue
                ### Add function call to add to PQFrontier both the move and the cost###
        
        def fnCalculateH(self, GoalBoard, CurrentIndex = (), GoalIndex = ()):
            if GoalBoard is not None:
                CurrentH = 0
                if CurrentIndex == () and GoalIndex == ():
                    for row in range(len(self.arrayBoard)):
                        for col in range(len(self.arrayBoard[row])):
                            CurrentPuzNum = self.arrayBoard[row][col]
                            GoalIndex = GoalBoard.fnFind(CurrentPuzNum)
                            CurrentH += (math.sqrt((GoalIndex[1] - col )**2 ))*2
                            NorthSouth = GoalIndex[0] - row
                            if NorthSouth < 0:
                                CurrentH += math.sqrt((NorthSouth)**2 )
                            elif NorthSouth > 0:
                                CurrentH += (math.sqrt((NorthSouth)**2 ))*3
                            
            else:
                print("Hey, I think you need to setup a GoalBoard before we keep going")
            
            return CurrentH
        
        def fnCalculateG(self, CostOfNewMove, PreviousG = None):
            """Can be used to calculate g(n) """
            if PreviousG == None:
                PreviousG = copy.deepcopy(self.gFunctionValue)
            
            NewG = PreviousG + CostOfNewMove
            return NewG
            pass
        
        def fnCalculateF(self, GValue = None, HValue = None):
            if GValue == None:
                GValue = self.gFunctionValue
            if HValue == None:
                HValue = self.hFunctionValue
                
            CurrentF = GValue + HValue
            return CurrentF
