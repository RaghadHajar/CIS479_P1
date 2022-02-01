import pprint
import Puzzle as p

class Hashtable: #Code from https://thepythoncorner.com/posts/2020-08-21-hash-tables-understanding-dictionaries/
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None

    def __str__(self):
        return pprint.pformat(self.buckets) # here pformat is used to return a printable representation of the object

GoalBoard = p.Puzzle.Board()
GoalVector = [1,2,3,4,"-",5,6,7,8]
GoalBoard.fnPopulateBoard(GoalVector)

InitialBoard = p.Puzzle.Board()
InitialVector = [3,2,1,5,"-",4,7,8,6]
InitialBoard.fnPopulateBoard(InitialVector)



ExpansionSet = [(InitialBoard.ExpansionSetNum, InitialBoard),((InitialBoard.ExpansionSetNum + 1), GoalBoard)]
ExpansionSetHash = Hashtable(ExpansionSet)

print(ExpansionSetHash)
