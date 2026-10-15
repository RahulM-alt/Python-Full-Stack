class Vehicle:
    def __init__(self, vehicle_id: str, base_rate: float):
        self._vehicle_id = vehicle_id
        self._base_rate = float(base_rate)

    def display_details(self) -> str:
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate:.2f}"

    def rental_charge(self) -> float:
        return 0.0


class Car(Vehicle):
    def __init__(self, vehicle_id: str, base_rate: float, num_seats: int):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self) -> float:
        return self._base_rate * self.num_seats


class Bike(Vehicle):
    def __init__(self, vehicle_id: str, base_rate: float, bike_type: str):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self) -> float:
        return self._base_rate * 0.5


def calculate_rental(vehicle: Vehicle) -> float:
    return vehicle.rental_charge()


# Example usage
car = Car("CAR001", 100.0, 4)
bike = Bike("BIKE001", 60.0, "Scooter")

print(car.display_details())
print(calculate_rental(car))    # 400.0

print(bike.display_details())
print(calculate_rental(bike))   # 30.0