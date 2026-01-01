from abc import ABC, abstractmethod
from enum import Enum


class VehicleStatus(Enum):
    AVAILABLE = "Available"
    IN_USE = "In Use"
    WARNING = "Warning"


class Vehicle(ABC):
    def __init__(self, model_name: str, battery_level: int, base_range: int):
        self.model_name = model_name
        self.battery_level = max(0, min(100, battery_level))
        self.base_range = base_range
        self.status = VehicleStatus.AVAILABLE

    @abstractmethod
    def calculate_remaining_range(self) -> float:
        pass

    def status_update(self):
        if self.battery_level < 10:
            self.status = VehicleStatus.WARNING
        print(f"Status update for {self.model_name}: {self.status.value}")


class EBike(Vehicle):
    def calculate_remaining_range(self) -> float:
        return (self.battery_level * self.base_range) / 100


class ECargoBike(Vehicle):
    def __init__(self, model_name: str, battery_level: int, base_range: int, cargo_kg: int):
        super().__init__(model_name, battery_level, base_range)
        self.cargo_kg = cargo_kg

    def calculate_remaining_range(self) -> float:
        base_calculation = (self.battery_level * self.base_range) / 100
        # Deduction: 2km per 10kg cargo
        deduction = (self.cargo_kg // 10) * 2
        return max(0.0, base_calculation - deduction)


if __name__ == "__main__":
    fleet = [
        EBike("City-Flash 200", 85, 120),
        EBike("Low-Battery-Bike", 8, 100),
        ECargoBike("Heavy-Cargo Plus", 90, 80, 50),
        ECargoBike("Eco-Transporter", 5, 60, 20)
    ]

    print("--- Range Overview ---")
    for v in fleet:
        range_km = v.calculate_remaining_range()
        print(f"Model: {v.model_name:18} | Range: {range_km:>5.1f} km")

    print("\n--- Status Updates (Polymorphism) ---")
    for v in fleet:
        v.status_update()