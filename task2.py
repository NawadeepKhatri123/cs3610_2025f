from abc import ABC, abstractmethod

# --- 2. Implementation Interface ---
# every payment method must be able to process a payment
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

# --- 3. Concrete Implementations ---
class DirectDeposit(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing Direct Deposit of ${amount}")

class PaperCheck(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Printing Paper Check for ${amount}")

class CryptoTransfer(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Transferring ${amount} via Crypto Wallet")

# --- 4. Factory Method ---
class PaymentFactory:
    @staticmethod
    def get_payment_method(method_type: str) -> PaymentProcessor:
        methods = {
            "deposit": DirectDeposit(),
            "check": PaperCheck(),
            "crypto": CryptoTransfer()
        }
        return methods.get(method_type.lower(), DirectDeposit())

# --- 1. Abstraction ---
# front end visible to the system
class Employee(ABC):
    def __init__(self, name: str, payment_processor: PaymentProcessor):
        self.name = name
        self.payment_processor = payment_processor

    @abstractmethod
    def pay(self):
        pass

# --- 5. Refined Abstractions ---
class FullTimeEmployee(Employee):
    def __init__(self, name: str, payment_processor: PaymentProcessor, salary: float):
        super().__init__(name, payment_processor)
        self.salary = salary

    def pay(self):
        print(f"Paying Full-Time Employee: {self.name}")
        # Maybe add bonus or tax logic here
        self.payment_processor.process_payment(self.salary)

class Contractor(Employee):
    def __init__(self, name: str, payment_processor: PaymentProcessor, hourly_rate: float, hours: int):
        super().__init__(name, payment_processor)
        self.total_pay = hourly_rate * hours

    def pay(self):
        print(f"Paying Contractor: {self.name}")
        self.payment_processor.process_payment(self.total_pay)

# --- Usage ---
if __name__ == "__main__":
    # Use Factory to get implementations
    bank_method = PaymentFactory.get_payment_method("deposit")
    check_method = PaymentFactory.get_payment_method("check")

    # Bridge implementations with abstractions
    alice = FullTimeEmployee("Alice", bank_method, 5000)
    bob = Contractor("Bob", check_method, 50, 20)

    alice.pay()
    bob.pay()
