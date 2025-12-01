from dataclasses import dataclass
@dataclass
class Tratta():
    id_hub_origine: str
    id_hub_destinazione: str
    guadagno_medio: int

    def __str__(self):
        return f"{self.id_hub_origine} - {self.id_hub_destinazione}"
    def __repr__(self):
        return f"{self.id_hub_origine} - {self.id_hub_destinazione}"











