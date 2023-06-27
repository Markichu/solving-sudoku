from sudoku import Sudoku
import time

class BacktrackingSolver:
    def __init__(self, sudoku):
        self.sudoku = sudoku.copy()
        
    def run(self):
        zero_indices = [i for i, value in enumerate(self.sudoku.data.flatten()) if value == 0]
        zero_pointer = 0
        iterations = 0
        start_time = time.time()
        
        while True:
            iterations += 1
            # print(''.join(str(x) for x in self.sudoku.data.flatten()))
            
            if zero_pointer >= len(zero_indices):
                break
            
            pointer_pos = zero_indices[zero_pointer]
            value = self.sudoku.get(pointer_pos)
            
            if value == 9:
                self.sudoku.set(pointer_pos, 0)
                zero_pointer -= 1
                continue
            
            self.sudoku.set(pointer_pos, value + 1)
            
            if self.sudoku.is_valid_at_pos(pointer_pos):
                zero_pointer += 1
                
        print(f"Found solution in {iterations} iterations in {time.time() - start_time} seconds")
        
        
if __name__ == "__main__":
    sudoku = Sudoku("000801000000000043500000000000070800000000100020030000600000075003400000000200600")
    # sudoku = Sudoku("095000080007040050180920060000600029060070105300281700070090310004510090002304000")
    solver = BacktrackingSolver(sudoku)
    solver.run()
    print(solver.sudoku.data)