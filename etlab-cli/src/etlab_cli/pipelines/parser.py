from pathlib import Path
from typing import Callable, Any

from pydantic import ValidationError
import yaml

from expression import Result, Ok, Error, pipe

from etlab_cli.pipelines.schema import Pipeline

class ParseError(Exception):
    ...


def result_try(fn: Callable[[], Any], to_err: Callable[[Exception], ParseError]) -> Result[Any, ParseError]:
    try:
        return Ok(fn())
    except Exception as e: 
        return Error(to_err(e))

def read_text(path: Path) -> Result[str, ParseError]:
    return result_try(
        lambda: path.read_text(encoding="utf-8"),
        lambda e: ParseError(f"Falha ao ler arquivo: {path} \n {e}")
    )

def parse_yaml(text: str) -> Result[Any, ParseError]:
    return result_try(
        lambda: yaml.safe_load(text),
        lambda e: ParseError(f"YAML inválido\n {e}")
    )

def format_validation_error(e: ValidationError) -> str:
    lines = ["Erros de validação:"]
    for err in e.errors():
        loc = " -> ".join(map(str, err.get("loc", [])))
        msg = err.get("msg", "erro")
        typ = err.get("type", "")
        lines.append(f"  - [{loc}] {msg} ({typ})")
    return "\n".join(lines)

def to_pipeline(data: Any) -> Result[Pipeline, ParseError]:
    return result_try(
        lambda: Pipeline(**data),
        lambda e: ParseError(format_validation_error(e)) if isinstance(e, ValidationError) else ParseError(str(e))
    )

def parse_pipeline(path: Path) -> Result[Pipeline, ParseError]:
    return pipe(
        path,
        read_text,
        lambda r: r.bind(parse_yaml),
        lambda r: r.bind(to_pipeline)
    )

