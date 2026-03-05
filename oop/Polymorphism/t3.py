from typing_extensions import override
class Printer:
    def print(self,value):
        if isinstance(value, str):
            print("Printer printing the text ",value)
        elif isinstance(value, int):
            print("Printer printing the number", value)
class AdvancePrinter(Printer):
    @override
    def print(self, value, copies=None):
        if isinstance(value,str) and copies is None:
            print("Advance printer printing the text",value)
        elif isinstance(value,str) and copies is not None:
            print("Advance Printer printing the text and its copies ", value)
            for i in range(copies):
                print(f"Copy {i+1} and {value}")
        elif isinstance(value,int):
            super().print(value)
    
p=AdvancePrinter()
p.print(10)
p.print("Hello I m Assadullah")
p.print("Ali adv",0)




