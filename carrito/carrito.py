class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def Agregar(self, producto):
        if str(producto.id) not in self.carrito.keys():
            self.carrito[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "cantidad": 1,
                "precio": str(producto.precio_venta),
                "imagen": producto.img
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.save()

    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def Eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.save()

    def Decrementar(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.Eliminar(producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")

    def Limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True