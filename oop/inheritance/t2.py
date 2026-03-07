class Vehicle:
      def __init__(self,name,year):
        self.brand_name=name
        self.brand_year=year
class Car(Vehicle):
    def __init__(self,model,name,year):
        super().__init__(name,year)
        self.model=model
    def display(self):
        print(f"The name of the brand model is {self.model} and {self.brand_name},  {self.brand_year}")


grandy=Car("Grandy","Honda",2024)

grandy.display()
