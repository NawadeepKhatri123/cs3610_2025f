from abc import ABC, abstractmethod
from typing import Any

# ==========================================
# 1. The Product (Complex Object)
# ==========================================
class Pizza:
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        return f"Pizza with ingredients: {', '.join(self.parts)}"

# ==========================================
# 2. The Builder Interface
# ==========================================
class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts
    of the Product objects.
    """
    @property
    @abstractmethod
    def product(self) -> Pizza:
        pass

    @abstractmethod
    def produce_dough(self):
        pass

    @abstractmethod
    def produce_sauce(self):
        pass

    @abstractmethod
    def produce_topping(self):
        pass

# ==========================================
# 3. Concrete Builders
# ==========================================
class HawaiianPizzaBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Pizza()

    @property
    def product(self) -> Pizza:
        product = self._product
        self.reset()
        return product

    def produce_dough(self):
        self._product.add("Cross dough")

    def produce_sauce(self):
        self._product.add("Mild sauce")

    def produce_topping(self):
        self._product.add("Pineapple & Ham")

class SpicyPizzaBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Pizza()

    @property
    def product(self) -> Pizza:
        product = self._product
        self.reset()
        return product

    def produce_dough(self):
        self._product.add("Pan baked dough")

    def produce_sauce(self):
        self._product.add("Hot Chili sauce")

    def produce_topping(self):
        self._product.add("Pepperoni & Jalapenos")

# ==========================================
# 4. The Director
# ==========================================
class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration.
    """
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_minimal_viable_product(self):
        self.builder.produce_dough()

    def build_full_featured_product(self):
        self.builder.produce_dough()
        self.builder.produce_sauce()
        self.builder.produce_topping()

# ==========================================
# 5. Client Code
# ==========================================
if __name__ == "__main__":
    director = Director()
    
    # Building a Hawaiian Pizza
    print("Client: I want a standard Hawaiian pizza.")
    hawaiian_builder = HawaiianPizzaBuilder()
    director.builder = hawaiian_builder
    
    director.build_full_featured_product()
    print(hawaiian_builder.product.list_parts())

    print("\n")

    # Building a Spicy Pizza (Custom, without Director)
    print("Client: I want a custom Spicy pizza (no sauce).")
    spicy_builder = SpicyPizzaBuilder()
    # Client manually controlling the build steps
    spicy_builder.produce_dough()
    spicy_builder.produce_topping()
    print(spicy_builder.product.list_parts())
