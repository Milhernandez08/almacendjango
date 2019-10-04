
# Sales = Sal
# Inventory = Inv
class Operaciones ():
    def __init__(self, Inventory, Sale):
        self.Inv = Inventory
        self.Sal = Sale

    def residuo (self):
        if int(self.Sal['status']) != 0:
            return int(self.Inv['quantity']) - int(self.Sal['quantity'])
        else:
            return int(self.Inv['quantity']) + int(self.Sal['quantity'])

    def subtotal (self):
        if int(self.Sal['status']) != 0:
            total = int(self.Sal['quantity']) * float(self.Inv['price'])
            descuento = (total * float(self.Sal['discount']))/100
            return total - descuento

    def total (self):
        if int(self.Sal['status']) != 0:
            iva = (self.subtotal() * float(self.Inv['tax']))/100
            return self.subtotal() + iva

    def res (self):
        resultado = []
        resultado.append(self.residuo())
        resultado.append(self.subtotal())
        resultado.append(self.total())
        return resultado