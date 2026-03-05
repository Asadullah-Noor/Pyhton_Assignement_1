class Printer:

    def print(self, value):
        if isinstance(value, str):
            print("Printer printing text:", value)
        elif isinstance(value, int):
            print("Printer printing number:", value)
class AdvancedPrinter(Printer):
    # overriding
    def print(self, value, copies=None):

        if isinstance(value, str) and copies is None:
            print("AdvancedPrinter printing text:", value)

        elif isinstance(value, str) and copies is not None:
            for i in range(copies):
                print(f"Copy {i+1}: {value}")

        elif isinstance(value, int):
            super().print(value)


# reference
p = AdvancedPrinter()

p.print("Hello")
p.print(10)
p.print("Hello", 3)