from abc import ABC, abstractmethod

# ==========================================
# 1. The Product Interface (Document)
# ==========================================
class Document(ABC):
    @abstractmethod
    def open(self) -> str:
        """
        Abstract method that all concrete documents must implement.
        """
        pass

    @abstractmethod
    def close(self) -> str:
        pass

# ==========================================
# 2. Concrete Products (Specific Documents)
# ==========================================
class WordDocument(Document):
    def open(self) -> str:
        return "Opening Word Document... Loaded MS Word tools."

    def close(self) -> str:
        return "Closing Word Document."

class PDFDocument(Document):
    def open(self) -> str:
        return "Opening PDF Document... Loaded Adobe tools."

    def close(self) -> str:
        return "Closing PDF Document."

# ==========================================
# 3. The Creator Class (Abstract Factory)
# ==========================================
class Application(ABC):
    """
    The Creator class declares the factory method that is supposed to return
    an object of a Product class. The Creator's subclasses usually provide
    the implementation of this method.
    """

    @abstractmethod
    def create_document(self) -> Document:
        """
        The FACTORY METHOD.
        """
        pass

    def new_document(self):
        """
        The core business logic that relies on the Factory Method.
        It creates a document and then uses it.
        """
        doc = self.create_document()
        print(f"App: {doc.open()}")
        print(f"App: {doc.close()}")

# ==========================================
# 4. Concrete Creators (Specific Applications)
# ==========================================
class WordApplication(Application):
    def create_document(self) -> Document:
        return WordDocument()

class PDFApplication(Application):
    def create_document(self) -> Document:
        return PDFDocument()

# ==========================================
# 5. Client Code / Driver
# ==========================================
if __name__ == "__main__":
    print("--- Client: I want a Word Document ---")
    app_word = WordApplication()
    app_word.new_document()

    print("\n--- Client: I want a PDF Document ---")
    app_pdf = PDFApplication()
    app_pdf.new_document()
