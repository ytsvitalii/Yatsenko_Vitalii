from abc import ABC, abstractmethod
from typing import Any


class CarBuilder(ABC):
    def __init__(self):
        super(CarBuilder, self).__init__()

    @abstractmethod
    def set_type_engine(self):
        pass

    @abstractmethod
    def set_volume_engine(self):
        pass

    @abstractmethod
    def set_abs(self):
        pass

    @abstractmethod
    def set_airbag(self):
        pass

    @abstractmethod
    def set_esp(self):
        pass

    @abstractmethod
    def is_computer(self):
        pass

    @abstractmethod
    def is_air_conditioning_or_climate_control(self):
        pass

    @abstractmethod
    def set_interior_trim(self):
        pass


class Equipment:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        parts_as_strings = [str(part) for part in self.parts]
        print(f"Product parts: {', '.join(parts_as_strings)}", end="")



class ConcreteCarBuilder(CarBuilder, ABC):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._equipment = Equipment()

    @property
    def product(self) -> Equipment:
        product = self._equipment
        self.reset()
        return product

    def set_type_engine(self, engine_type: str):
        self._equipment.add(engine_type)

    def set_volume_engine(self):
        self._equipment.add(3.0)

    def set_abs(self):
        self._equipment.add("ABS available")

    def set_airbag(self):
        self._equipment.add("Airbag available")

    def set_esp(self):
        self._equipment.add("ESP available")

    def is_computer(self):
        self._equipment.add("Is Computer")

    def is_air_conditioning_or_climate_control(self):
        self._equipment.add("Climate control available")

    def set_interior_trim(self):
        self._equipment.add("Alcantara")




class CarDirector(CarBuilder):
    def __init__(self) -> None:
        self._car_builder = None

    @property
    def car_builder(self) -> CarBuilder:
        return self._car_builder

    def car_builder(self, car_builder: CarBuilder) -> None:
        self._car_builder = car_builder

    def build_minimal_viable_product(self) -> None:
        self.car_builder.set_abs()
        self.car_builder.set_volume_engine()
        self.car_builder.is_computer()
        self.car_builder.is_air_conditioning_or_climate_control()

    def build_full_viable_product(self) -> None:
        self.car_builder.is_computer()
        self.car_builder.is_air_conditioning_or_climate_control()
        self.car_builder.set_abs()
        self.car_builder.set_esp()
        self.car_builder.set_interior_trim()
        self.car_builder.set_airbag()
        self.car_builder.set_volume_engine()

    def is_computer(self):
        pass

    def is_air_conditioning_or_climate_control(self):
        pass

    def set_abs(self):
        pass

    def set_airbag(self):
        pass

    def set_esp(self):
        pass

    def set_interior_trim(self):
        pass

    def set_type_engine(self):
        pass

    def set_volume_engine(self):
        pass



director = CarDirector()
builder = ConcreteCarBuilder()
director.car_builder = builder

print("Standard: ")
director.build_minimal_viable_product()
builder.set_type_engine("Benzin")  # Set the engine type to Benzin
builder.product.list_parts()

print()
print("Luxury: ")
director.build_full_viable_product()
builder.set_type_engine("Diesel")  # Set the engine type to Diesel
builder.product.list_parts()


