class Producto:
    def _init_(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def _str_(self):
        return f"Producto(id={self.id_producto}, nombre={self.nombre}, precio={self.precio}, stock={self.stock})"

    def actualizar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            print(f"Stock insuficiente para {self.nombre}")
            return False


class Cliente:
    def _init_(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre

    def _str_(self):
        return f"Cliente(id={self.id_cliente}, nombre={self.nombre})"


class Pedido:
    def _init_(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        if producto.actualizar_stock(cantidad):
            self.productos.append((producto, cantidad))
            self.total += producto.precio * cantidad

    def _str_(self):
        productos_str = ', '.join([f"{prod.nombre} x{cant}" for prod, cant in self.productos])
        return f"Pedido(cliente={self.cliente.nombre}, productos=[{productos_str}], total={self.total})"


class Tienda:
    def _init_(self):
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def _str_(self):
        productos_str = ', '.join([str(prod) for prod in self.productos])
        clientes_str = ', '.join([str(cli) for cli in self.clientes])
        return f"Tienda(productos=[{productos_str}], clientes=[{clientes_str}])"


# Ejemplo de uso
if __name__ == "_main_":
    # Crear tienda
    tienda = Tienda()

    # Agregar productos
    producto1 = Producto(1, "Laptop", 1500, 10)
    producto2 = Producto(2, "Smartphone", 800, 20)
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)

    # Agregar clientes
    cliente1 = Cliente(1, "Luis Daniel Neajic Arregui")
    tienda.agregar_cliente(cliente1)

    # Crear pedido
    pedido1 = Pedido(cliente1)
    pedido1.agregar_producto(producto1, 2)
    pedido1.agregar_producto(producto2, 1)

    print(tienda)
    print(pedido1)