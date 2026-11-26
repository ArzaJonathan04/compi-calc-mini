import sys
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Token:
    tipo: str
    lexema: str
    linea: int
    columna: int

    def __str__(self) -> str:
        return f'<{self.tipo}, "{self.lexema}", {self.linea}, {self.columna}>'

class CompiladorError(Exception):
    
    def __init__(self, linea: int, columna: int, mensaje: str):
        self.linea = linea
        self.columna = columna
        self.mensaje = mensaje
        super().__init__(f"Error [Línea {linea}, Columna {columna}]: {mensaje}")

class LexerError(CompiladorError):
    pass

class ParserError(CompiladorError):
    pass
