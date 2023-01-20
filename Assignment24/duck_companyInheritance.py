class capgemini():
    def details(self):
        print("cagemini is multinational information tech.")
        print("CEO of capgemini company is Ashvini Yardi")
        print("company founded 1 oct 1967")
        print("company founder is Serge Kampf ")

class cognizant():
    def details(self):
        print("cognizant is American multinational information tech.")
        print("CEO of cognizant company is Ravi Kumar Singisetti")
        print("company founded 26 January 1994 ")
        print("company founder is Kumar Mahadeva")

class domain():
    def data(self, x):
        x.details()

d = domain()
c = cognizant()
d.data(c)
print("......")
b = capgemini()
d.data(b)
        
