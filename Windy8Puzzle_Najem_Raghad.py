class Puzzle: #Raghad and #Najem
    """This is the class that holds the whole game"""
    pass

    class MinPQ:
        """A minimum priority queue. 
        Can be used for ordering h(n), selecting f(n) and must be used for the frontier set
        As directed by the professor we do not have to build from scrath
        use an implementation of heapq. Library info found here:"""
        #https://docs.python.org/3/library/heapq.html """
        pass
    
    class Hashtable:
        """Data structure to be used for storage of explored set. 
        As directed by the porfessor we do not have to build from scratch
        Using code from:"""
        #https://thepythoncorner.com/posts/2020-08-21-hash-tables-understanding-dictionaries/ """
        pass
    
    class Board:
        """Class to store all board types and related functions"""
        def __init__(self):
            self.arrayBoard = [[]]
            self.fFunctionValue = 0 #Maps to right
            self.gFunctionValue = 0  #Maps to left
            self.ExpansionSetNum = 1 #Bottom Row with a # before the number ex #1
            self.BoardOutput = ""
            
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
            if len(self.arrayBoard) == len(OtherBoard.arrayBoard):
                for row in range(len(self.arrayBoard)):
                    for col in range(len(self.arrayBoard)):
                        if self.arrayBoard[row][col] != OtherBoard.arrayBoard[row][col]:
                            return False
                return True
            else
                return False
                
        def __setattr__
                        
            
        def fnPopulateBoard(self, listPuzzleNum):
            """Enter the positions of the arrayBoard by using a vector
            of the Puzzle Numbers (listPuzzleNum) as strings
            Send it in the order of top left to bottom right
            Don't forget the '-' blank value
            """
            for indexPuzzleNum in range(len(listPuzzleNum)):
                if (len(listPuzzleNum) + 1) % (len(self.arrayBoard) + 1) == 0:
                    if indexPuzzleNum <= len(self.arrayBoard[0]):
                        self.arrayBoard[0][indexPuzzleNum] = listPuzzleNum[indexPuzzleNum]
                    elif ((indexPuzzleNum+1)- (len(self.arrayBoard[0])+1)) <= (len(self.arrayBoard[0])+1):
                        RowNumber = indexPuzzleNum // len(self.arrayBoard[0]) 
                        ColNumber = indexPuzzleNum % len(self.arrayBoard)
                else:
                    print("The length of the listPuzzleNum is incorrect")
                        
            
    
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
            
        def fnFindPossibleMoves(self):
            pass
        
        def fnCalculateH(self):
            pass
        
        def fnCalculateG(self):
            pass
        
        def fnCalculateF(self):
            pass
        
print(4//4)
