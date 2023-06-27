import numpy as np
import time

def contains_duplicates(group):
    counts = [False] * 9
    for item in group:
        if item == 0:
            continue
        
        if counts[item-1]:
            return True

        counts[item-1] = True
    
    return False

class Sudoku:
    def __init__(self, data=None):
        if isinstance(data, np.ndarray):
            self.data = data
            
        if isinstance(data, list):
            self.data = np.array(data)
            
        if isinstance(data, str):
            self.data = np.array([int(i) for i in data]).reshape(9,9)
            
        if data is None:
            self.data = np.zeros((9,9), dtype=int)
            
    def copy(self):
        return Sudoku(self.data.copy())
    
    def get(self, position):
        row = None
        column = None
        
        if isinstance(position, tuple):
            row, column = position
            
        if isinstance(position, int):
            row = position // 9
            column = position % 9
            
        if row is None or column is None:
            raise ValueError(f"Incorrect position given, given {position}")
        
        return self.data[row, column]
            
    def set(self, position, value):
        row = None
        column = None
        
        if isinstance(position, tuple):
            row, column = position
            
        if isinstance(position, int):
            row = position // 9
            column = position % 9
            
        if row is None or column is None:
            raise ValueError(f"Incorrect position given, given {position}")
        
        self.data[row, column] = value
            
    def is_valid(self):
        for row in self.data:
            if contains_duplicates(row):
                return False
            
        for column in self.data.T:
            if contains_duplicates(column):
                    return False
            
        for i in range(3):
            for j in range(3):
                if contains_duplicates(self.data[i*3:i*3+3, j*3:j*3+3].flatten()):
                    return False
                
        return True
    
    def is_valid_at_pos(self, position):
        row = None
        column = None
        
        if isinstance(position, tuple):
            row, column = position
            
        if isinstance(position, int):
            row = position // 9
            column = position % 9
            
        if row is None or column is None:
            raise ValueError(f"Incorrect position given, given {position}")
        
        if contains_duplicates(self.data[row]):
            return False
        
        if contains_duplicates(self.data[:,column]):
            return False
        
        if contains_duplicates(self.data[row//3*3:row//3*3+3, column//3*3:column//3*3+3].flatten()):
            return False
        
        return True
            
        
        
        
if __name__ == "__main__":
    Sudoku = Sudoku("864371259325849761971265843436192587198657432257483916689734125713528694542916378")
    print(Sudoku.data)
    start_time = time.time()
    for _ in range(100000):
        Sudoku.is_valid()
    print(f"--- {time.time() - start_time} seconds ---")
    
    # sudoku.place(0, 1)
    # sudoku.place((1, 3), 2)
    # print(sudoku.data)