from .utils.compiler_containers import component_container


class compiler:
    def __init__(self, lexer, parser):
        self.symbolTable = {}

        self.lexer = lexer
        self.parser = parser
        pass