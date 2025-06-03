from typing import Any, Type, TypeVar
from pithon.syntax import (
    PiAssignment, PiBinaryOperation, PiNumber, PiBool, PiStatement, PiProgram, PiVariable,
    PiIfThenElse, PiNot, PiAnd, PiOr, PiWhile, PiNone, PiList, PiTuple, PiString,
    PiFunctionDef, PiFunctionCall, PiFor, PiBreak, PiContinue, PiIn, PiReturn
)
from pithon.evaluator.envvalue import EnvValue, FunctionClosure

def initial_env() -> list[tuple[str, EnvValue]]:
    pass

def lookup(env: list[tuple[str, EnvValue]], name: str) -> EnvValue:
    pass

def insert(env: list[tuple[str, EnvValue]], name: str, value: EnvValue) -> None:
    pass

def evaluate(node: PiProgram, env: list[tuple[str, EnvValue]]) -> EnvValue:
    pass
