class Puzzle: #Raghad and #Najem
    """This is the class that holds the whole game"""
    pass

    class MinPQ:
        """A minimum priority queue. 
        Can be used for ordering h(n), selecting f(n) and must be used for the frontier set
        As directed by the professor we do not have to build from scrath
        use an implementation of heapq. Library info found here:"""
        #https://thepythoncorner.com/posts/2020-08-21-hash-tables-understanding-dictionaries/ """

        pass
    
    class Hashtable:
        """Data structure to be used for storage of explored set. 
        Will be used at the end of the puzzle to print all boards for the path
        As directed by the porfessor we do not have to build from scratch
        Using code from"""
         ##https://docs.python.org/3/library/heapq.html """
        
        pass
    
    class Move:
        def __init__(self
        ,StartingIndex = ()
        ,NewIndex = ()
        ,InitialOrder = 0
        ,PuzzleNum = '-'
        ,PuzzleGoalIndex = ()
        ,GValue = 0
        ,HValue = 0
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
        def __init__(self,NumRow,NumCol):
            self.arrayBoard = [[0]*NumCol for i in range(NumRow)]
            self.fFunctionValue = 0 #Maps to right
            self.gFunctionValue = 0  #Maps to left
            self.hFunctionValue = None  #Doesn't map
            self.ExpansionSetNum = 1 #Bottom Row with a # before the number ex #1
            self.BoardOutput = ""
            self.FrontierSet = MinPQ
            
        def __print__(self):
            for row in range(len(self.arrayBoard)):
                if row == 0:
                    self.BoardOutput = "_"*len(self.arrayBoard)*2 + "/n"
                for col in range(len(self.arrayBoard[row])):
                    if col == 0 and row == 0:
                        self.BoardOutput += "|"
                    if row == len(self.arrayBoard) and col == len(self.arrayBoard):
                        self.BoardOutput += "_"*len(self.arrayBoard)*2
                        
        def __eq__(self, OtherBoard):
            listTruthValues = []
            if (len(self.arrayBoard) == len(OtherBoard.arrayBoard)):
                for row in range(len(self.arrayBoard)):
                    for col in range(len(self.arrayBoard)):
                        if self.arrayBoard[row][col] != OtherBoard.arrayBoard[row][col]:
                            return False
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
                if PuzzleNum in range(len(self.arrayBoard[row])):
                    for col in self.arrayBoard[row]:
                        if PuzzleNum == self.arrayBoard[row][col]:
                            IndexPosition = (row, col)
                            return (IndexPosition)
                else:
                    next
                    
        def fnFindBlank(self):
            Find(self, '-')
            
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
            
            Move1 = Move()
            Move2 = Move()
            Move3 = Move()
            Move4 = Move()
            
            if BlankCol != 0: #skip west if border
                Move1 = BlankCol - 1
                Move1Cost = 2
                ### Add function call to add to PQFrontier both the move and the cost###
            
            if BlankRow != 0: #skip north if border
                Move2 = BlankRow - 1 
                Move2Cost = 1
                ### Add function call to add to PQFrontier both the move and the cost###
                
            if BlankCol != len(self.arrayBoard) - 1: #skip east if border
                Move3 = BlankCol + 1 
                Move3Cost = 2
                ### Add function call to add to PQFrontier both the move and the cost###
            
            if BlankRow != len(self.arrayBoard) - 1: #skip south if border
                Move4 = BlankRow + 1 
                Move4Cost = 4
                ### Add function call to add to PQFrontier both the move and the cost###
        
        def fnCalculateH(self, CurrentIndex = (), GoalIndex = (), GoalBoard = None):
            if GoalBoard is not None:
                if CurrentIndex == ():
                    CurrentIndex = self.fnFindBlank()
                if GoalIndex == ():
                    GoalBoard.fnFindBlank()
            else:
                print("Hey, I think you need to setup a GoalBoard before we keep going")
            pass
        
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
