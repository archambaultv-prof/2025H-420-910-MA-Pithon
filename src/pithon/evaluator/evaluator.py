from pithon.syntax import (
    PiAssignment, PiBinaryOperation, PiNumber, PiBool, PiValue, PiProgram, PiVariable,
    PiIfThenElse, PiNot, PiAnd, PiOr, PiWhile, PiPrint, PiNone
)

def empty_env() -> list[tuple[str, PiValue]]:
    return []

def lookup(env: list[tuple[str, PiValue]], name: str) -> PiValue:
    pass

def insert(env: list[tuple[str, PiValue]], name: str, value: PiValue) -> None:
    pass

def evaluate(node: PiProgram, env: list[tuple[str, PiValue]]) -> PiValue:
    pass
