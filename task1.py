import json
import csv
import io
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

# --- Adaptees (Legacy/External Modules) ---
# accepts the adaptee through the constructor
# conversts the format properly
# returns a json like dict
class TaxCalculator:
    #retunrs raw csv text
    def get_tax_history(self):
        return "id,amount,status\n1,1000,paid\n2,500,pending"

class AccountingModule:
    #returns an xml string
    def get_balance_sheet(self):
        return "<balances><entry><id>1</id><amount>5000</amount></entry></balances>"

class CreditAuthService:
    #retuns json , but as a string not a dict
    def get_credit_score(self):
        return json.dumps({"id": 1, "score": 750, "history": "clean"})

# --- Target Interface ---
# all adapters share the same interface
class FinancialDataProvider(ABC):
    @abstractmethod
    def get_data(self) -> dict:
        pass

# --- Adapters ---
class TaxCSVAdapter(FinancialDataProvider):
    def __init__(self, adaptee: TaxCalculator):
        self.adaptee = adaptee

    def get_data(self) -> dict:
        csv_data = self.adaptee.get_tax_history()
        # Convert CSV string to List of Dictionaries (JSON-serializable)
        reader = csv.DictReader(io.StringIO(csv_data))
        return {"source": "Tax", "data": [row for row in reader]}

class AccountingXMLAdapter(FinancialDataProvider):
    def __init__(self, adaptee: AccountingModule):
        self.adaptee = adaptee
```
    def get_data(self) -> dict:
        xml_data = self.adaptee.get_balance_sheet()
        # Simple XML parsing
        # extracts <entry> blocks
        # turns them into dictionaries
        root = ET.fromstring(xml_data)
        entries = []
        for entry in root.findall('entry'):
            entries.append({
                "id": entry.find('id').text,
                "amount": entry.find('amount').text
            })
        return {"source": "Accounting", "data": entries}
# loads the json string into a python dict
# wraps it in the unified structure
class CreditJSONAdapter(FinancialDataProvider):
    def __init__(self, adaptee: CreditAuthService):
        self.adaptee = adaptee

    def get_data(self) -> dict:
        # Ensure structure matches client expectations
        raw_json = self.adaptee.get_credit_score()
        return {"source": "Credit", "data": json.loads(raw_json)}

# --- Client --- return a dict
# expects all providers to have .get_data()
class ForecastingModule:
    def analyze(self, providers: list[FinancialDataProvider]):
        print("Starting Analysis...")
        for provider in providers:
            data = provider.get_data()
            print(f"Processing JSON data from {data['source']}: {data['data']}")

# --- Usage ---
if __name__ == "__main__":
    # Initialize Adaptees
    tax_calc = TaxCalculator()
    acc_mod = AccountingModule()
    credit_serv = CreditAuthService()

    # Wrap in Adapters
    adapters = [
        TaxCSVAdapter(tax_calc),
        AccountingXMLAdapter(acc_mod),
        CreditJSONAdapter(credit_serv)
    ]

    # Client works with common interface
    app = ForecastingModule()
    app.analyze(adapters)
