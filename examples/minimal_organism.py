"""Minimal closed-loop organism stand.
This is an engineering baseline, not a biological model.
Run: python examples/minimal_organism.py
"""
from dataclasses import dataclass

@dataclass
class Organism:
    position: float = 0.0
    energy: float = 1.0
    step: int = 0

    def update(self, food: float) -> None:
        self.step += 1
        signal = food - self.position
        self.position += max(-0.1, min(0.1, signal * 0.05))
        self.energy -= 0.01
        if abs(food - self.position) < 0.05:
            self.energy = min(1.0, self.energy + 0.05)

def main() -> None:
    organism = Organism()
    for _ in range(100):
        organism.update(1.0)
    print("Digital Organisms Lab — minimal closed loop")
    print(f"steps={organism.step}")
    print(f"position={organism.position:.4f}")
    print(f"energy={organism.energy:.4f}")

if __name__ == "__main__":
    main()
