# Definición de la clase base Empleado
class Empleado:
    def _init_(self, nombre, salario):
        self.__nombre = nombre  # Encapsulación del atributo nombre
        self.__salario = salario  # Encapsulación del atributo salario

    def obtener_nombre(self):
        return self.__nombre

    def obtener_salario(self):
        return self.__salario

    def descripcion(self):
        return f"Soy un empleado llamado {self._nombre} y mi salario es ${self._salario:.2f}"


# Definición de la clase derivada Gerente
class Gerente(Empleado):
    def _init_(self, nombre, salario, departamento):
        super()._init_(nombre, salario)
        self.__departamento = departamento

    def obtener_departamento(self):
        return self.__departamento

    def descripcion(self):  # Polimorfismo: método sobrescrito
        return f"Soy un gerente llamado {self.obtener_nombre()}, trabajo en el departamento {self.__departamento} y mi salario es ${self.obtener_salario():.2f}"


# Creación de objetos y prueba del programa
if __name__ == "_main_":
    # Crear un objeto Empleado
    empleado1 = Empleado("Byro", 2100)
    print(empleado1.descripcion())

    # Crear un objeto Gerente
    gerente1 = Gerente("Karla", 3400, "Ventas")
    print(gerente1.descripcion())