from person import Person
from package import Package
from overweigthpackage import OverWeigthPackage
from standardPackage import StandardPackage
from address import Address
from deliver import Deliver

"""from bill import Bill"""


Individual = Person(1001979606,"Juan","Moreno Santos")
Box = Package(123456, 5.6, "Pista de carreras", 500000)
Weigth = OverWeigthPackage(5.3, "Pista de carreras", 500000, 10.5)
Standard = StandardPackage("","","","",5.3)
Addres3 = Address("","","","","","","","","PradoVerde", "Carrera32", "Cartagena", "Ruta95", "130010")
Delivery = Deliver("22/03/2023", "9:49 Am", "Juan Moreno Santos", "David Arrieta", "recibir", "+573004689813", "Pista de carrera", "")

"""bil4 = Bill(Box,Addres3,Individual,500000 ,"Credito" ,"38 Cuotas")"""

print("Individuo")
print(Individual)
print("Paquete")
print(Box)
print("Peso De paquete")
print(Weigth)
print("Paquete estandar")
print(Standard)
print("Direccion")
print(Addres3)
print("Entrega")
print(Delivery)

"""print(bil4)"""


"""
if __name__ == '__main__':

    edwin = Person(id_person=73577376, name="Edwin", last_name="Puertas")
    edwin.name = "Edwin. A"
    print(edwin)

    juan = Person()
    print(juan)
"""