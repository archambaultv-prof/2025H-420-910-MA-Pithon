from typing import Any, Type, TypeVar
from pithon.evaluator.envframe import EnvFrame
from pithon.syntax import (
    PiAssignment, PiBinaryOperation, PiNumber, PiBool, PiStatement, PiProgram, PiVariable,
    PiIfThenElse, PiNot, PiAnd, PiOr, PiWhile, PiNone, PiList, PiTuple, PiString,
    PiFunctionDef, PiFunctionCall, PiFor, PiBreak, PiContinue, PiIn, PiReturn
)
from pithon.evaluator.envvalue import EnvValue, FunctionClosure


def initial_env() -> EnvFrame:
    pass

def lookup(env: EnvFrame, name: str) -> EnvValue:
    pass

def insert(env: EnvFrame, name: str, value: EnvValue) -> None:
    pass

def evaluate(node: PiProgram, env: EnvFrame) -> EnvValue:
    pass
