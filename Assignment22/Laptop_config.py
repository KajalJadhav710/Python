class Laptop():
    def __init__(self):
        self.name = "acer"
        self.RAM = "4 GB"
        self.ROM = "64 GB"
        self.processor = "core i7"
        self.display = "15.60-inch"

    def config(self):
        print("Name is ",self.name)
        print("Ram is ", self.RAM)
        print("Rom is ",self.ROM)
        print("processor is ",self.processor)
        print("display is ", self.display)

a = Laptop()
b = Laptop()
a.config()
print("name ",a.RAM)
print()

b.processor = b. processor + " processor"
print("Laptop  is ", b.processor)
print()

b.display = "14 inch"
print("display is ", b.display)
print()

print("name is ", b.name,b.processor)

