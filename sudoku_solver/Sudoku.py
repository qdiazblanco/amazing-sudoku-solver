SIZE = 9 #tamaño del sudoku
SUDOKU_DIGITS = range(1,10) #numeros validos del sudoku
BLANK_SYMBOL = 0 #simbolo para interpretar las casillas vacias

class Sudoku :
    
    data: list[list[int]]

    def __init__(self, given_data : list[list[int]]) -> void:

        if not isinstance(given_data, list[list[int]]) :
            raise ValueError("Sudoku must be a matrix")

        if not len(given_data) == 9 & not all(len(row) == 9 for row in given_data) :
            raise ValueError("Sudoku must be a 9x9 matrix")
        
        for j in range(9) :
            for i in range(9) :
                if not given_data[j][i] < 10 & given_data[j][i] >= 0:
                    raise ValueError("All digits must be between 0 and 9") 



