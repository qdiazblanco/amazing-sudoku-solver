SIZE = 9 #tamaño del sudoku
SUDOKU_DIGITS = range(1,10) #numeros validos del sudoku
BLANK_SYMBOL = 0 #simbolo para interpretar las casillas vacias

class Sudoku :
    
    data: list[list[int]]

    def is_sudoku_digit(i : int) -> bool:
        return i in SUDOKU_DIGITS

    def is_blank(i : int) -> bool:
        return i == BLANK_SYMBOL

    def is_valid_digit(i : int) -> bool:
        return is_sudoku_digit(i) or is_blank(i)
    
     

    def __init__(self, given_data : list[list[int]]) -> void:

        if not isinstance(given_data, list[list[int]]) :
            raise ValueError("Sudoku must be a matrix")

        if not len(given_data) == SIZE & not all(len(row) == SIZE for row in given_data) :
            raise ValueError(f"Sudoku must be a {SIZE}x{SIZE} matrix")

        if not all(is_valid_digit(digit) for row in given_data for digit in row) :
            raise ValueError(f"All Sudoku digits must be in {SUDOKU_DIGITS} or be a {BLANK_SYMBOL}")
        
        #comprobar si es valido (dos iguales en misma fila por ej)
        
        self.data = given_data

    def __repr__(self) : #que este bonico
        pass

    def __getitem__(self, key) :
        pass

    def row(self, i : int) -> list[int]:
        pass

    def col(self, j : int) -> list[int]:
        pass

    def box(self, k : int) -> list[int]:
        pass

    def is_correct(self) -> bool: #comprueba si vas bien
        pass

    def is_solved(self) -> bool : #comprueba si esta resuelto
        pass

