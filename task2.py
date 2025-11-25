from abc import ABC, abstractmethod

# ==========================================
# 1. Abstract Products
# ==========================================
class Button(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass

# ==========================================
# 2. Concrete Products (Family A: Windows)
# ==========================================
class WinButton(Button):
    def paint(self) -> str:
        return "Rendering a button in Windows style."

class WinCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering a checkbox in Windows style."

# ==========================================
# 3. Concrete Products (Family B: Mac)
# ==========================================
class MacButton(Button):
    def paint(self) -> str:
        return "Rendering a button in MacOS style."

class MacCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering a checkbox in MacOS style."

# ==========================================
# 4. The Abstract Factory Interface
# ==========================================
class GUIFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family.
    """
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# ==========================================
# 5. Concrete Factories
# ==========================================
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# ==========================================
# 6. Client Code
# ==========================================
def client_code(factory: GUIFactory):
    """
    The client code works with factories and products only through abstract
    types: GUIFactory and AbstractProduct.
    """
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(f"Client: {button.paint()}")
    print(f"Client: {checkbox.paint()}")

if __name__ == "__main__":
    print("App: Launched with Windows configuration.")
    client_code(WindowsFactory())

    print("\nApp: Launched with Mac configuration.")
    client_code(MacFactory())
