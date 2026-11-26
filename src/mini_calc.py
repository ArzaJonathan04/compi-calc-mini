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
    
class Lexer:
    SIMBOLOS_UN_CARACTER = {
        "=": "OP_ASSIGN",
        "+": "OP_ADD",
        "-": "OP_SUB",
        "*": "OP_MUL",
        "/": "OP_DIV",
        "(": "PUNCT_LPAREN",
        ")": "PUNCT_RPAREN",
        ";": "PUNCT_SEMI",
    }

    def __init__(self, codigo: str):
        self.codigo = codigo
        self.pos = 0
        self.linea = 1
        self.columna = 1
        self.longitud = len(codigo)

    def _actual(self) -> Optional[str]:
        if self.pos < self.longitud:
            return self.codigo[self.pos]
        return None

    def _avanzar(self) -> Optional[str]:
        car = self._actual()
        if car is None:
            return None
        self.pos += 1
        if car == "\n":
            self.linea += 1
            self.columna = 1
        else:
            self.columna += 1
        return car

    def _saltar_espacios(self) -> None:
        while (car := self._actual()) is not None and car in (" ", "\t", "\r", "\n"):
            self._avanzar()

    def tokenizar(self) -> List[Token]:
        tokens: List[Token] = []

        while True:
            self._saltar_espacios()
            car = self._actual()
            if car is None:
                break

            inicio_linea = self.linea
            inicio_col = self.columna

            if car.isdigit():
                lexema = ""
                while (c := self._actual()) is not None and c.isdigit():
                    lexema += c
                    self._avanzar()
                tokens.append(Token("NUM", lexema, inicio_linea, inicio_col))

            elif "a" <= car <= "z":
                lexema = ""
                while (c := self._actual()) is not None and "a" <= c <= "z":
                    lexema += c
                    self._avanzar()

                if lexema == "print":
                    tokens.append(Token("KW_PRINT", lexema, inicio_linea, inicio_col))
                elif len(lexema) == 1:
                    tokens.append(Token("ID", lexema, inicio_linea, inicio_col))
                else:
                    raise LexerError(
                        inicio_linea,
                        inicio_col,
                        f"Identificador no válido '{lexema}': las variables deben ser de una sola letra [a-z]."
                    )

            elif car in self.SIMBOLOS_UN_CARACTER:
                tipo_token = self.SIMBOLOS_UN_CARACTER[car]
                self._avanzar()
                tokens.append(Token(tipo_token, car, inicio_linea, inicio_col))

            else:
                self._avanzar()
                raise LexerError(
                    inicio_linea,
                    inicio_col,
                    f"Carácter no válido '{car}'."
                )

        tokens.append(Token("EOF", "", self.linea, self.columna))
        return tokens


class Parser:
   
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.actual_idx = 0

    @property
    def token_actual(self) -> Token:
        return self.tokens[self.actual_idx]

    def _error_sintactico(self, mensaje: str) -> ParserError:
        tok = self.token_actual
        return ParserError(tok.linea, tok.columna, mensaje)

    def _consumir(self, tipo_esperado: str) -> Token:
        tok = self.token_actual
        if tok.tipo == tipo_esperado:
            self.actual_idx += 1
            return tok
        raise self._error_sintactico(
            f"Se esperaba {tipo_esperado}, pero se encontró {tok.tipo} ('{tok.lexema}')."
        )

    def parsear(self) -> None:
        self.programa()

    def programa(self) -> None:
        self.lista_sentencias()
        self._consumir("EOF")

    def lista_sentencias(self) -> None:
        while self.token_actual.tipo in ("ID", "KW_PRINT"):
            self.sentencia()

    def sentencia(self) -> None:
        tok = self.token_actual
        if tok.tipo == "ID":
            self._consumir("ID")
            self._consumir("OP_ASSIGN")
            self.expresion()
            self._consumir("PUNCT_SEMI")
        elif tok.tipo == "KW_PRINT":
            self._consumir("KW_PRINT")
            self.expresion()
            self._consumir("PUNCT_SEMI")
        else:
            raise self._error_sintactico(
                f"Sentencia no válida: se esperaba 'ID' o 'print', pero se encontró '{tok.lexema}'."
            )

    def expresion(self) -> None:
        self.termino()
        self.expresion_prima()

    def expresion_prima(self) -> None:
        while self.token_actual.tipo in ("OP_ADD", "OP_SUB"):
            if self.token_actual.tipo == "OP_ADD":
                self._consumir("OP_ADD")
            else:
                self._consumir("OP_SUB")
            self.termino()

    def termino(self) -> None:
        self.factor()
        self.termino_prima()

    def termino_prima(self) -> None:
        while self.token_actual.tipo in ("OP_MUL", "OP_DIV"):
            if self.token_actual.tipo == "OP_MUL":
                self._consumir("OP_MUL")
            else:
                self._consumir("OP_DIV")
            self.factor()

    def factor(self) -> None:
        tok = self.token_actual
        if tok.tipo == "PUNCT_LPAREN":
            self._consumir("PUNCT_LPAREN")
            self.expresion()
            self._consumir("PUNCT_RPAREN")
        elif tok.tipo == "ID":
            self._consumir("ID")
        elif tok.tipo == "NUM":
            self._consumir("NUM")
        else:
            raise self._error_sintactico(
                f"Factor no válido: se esperaba '(', 'ID' o 'NUM', pero se encontró '{tok.lexema}'."
            )

