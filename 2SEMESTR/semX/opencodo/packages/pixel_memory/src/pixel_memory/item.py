from dataclasses import dataclass, field
from typing import List
import numpy as np
import time


@dataclass
class MemoryItem:
    fact: str
    embedding: np.ndarray
    keywords: List[str]
    importance: float = 1.0
    access_count: int = 0
    created_at: float = field(default_factory=time.time)

    ACCESS_BOOST = 1.0
    DECAY_RATE = 0.0001

    def compute_importance(self) -> float:
        age = time.time() - self.created_at
        recency_bonus = max(0, 500 - age * 50)
        return self.importance + (self.access_count * self.ACCESS_BOOST) + recency_bonus

    def boost_access(self) -> None:
        self.access_count += 1

    def update_importance(self, new_score: float) -> None:
        self.importance = new_score