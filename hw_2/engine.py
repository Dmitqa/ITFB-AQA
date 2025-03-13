from dataclasses import dataclass


@dataclass(frozen=False)
class Engine:
    volume: float
    pistons: int
