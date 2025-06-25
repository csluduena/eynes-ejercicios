import math


class Circle:
    def __init__(self, radius):
        """
        Inicializa un círculo con el radio dado.
        Lanza ValueError si el radio es <= 0.
        """
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius

    def get_radius(self):
        """
        Retorna el radio del círculo.
        """
        return self.radius

    def set_radius(self, radius):
        """
        Establece un nuevo radio para el círculo.
        Lanza ValueError si el radio es <= 0.
        """
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius

    def get_area(self):
        """
        Retorna el área del círculo basada en su radio.
        Área = π * r²
        """
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        """
        Retorna el perímetro del círculo basado en su radio.
        Perímetro = 2 * π * r
        """
        return 2 * math.pi * self.radius

    def __mul__(self, n):
        """
        Multiplica el círculo por un número n, retornando un nuevo Circle
        con radio multiplicado por n.
        Lanza ValueError si n <= 0.
        """
        if n <= 0:
            raise ValueError("El multiplicador debe ser mayor que 0")
        return Circle(self.radius * n)

    def __str__(self):
        """
        Representación amigable del círculo.
        """
        return f"Circle(radius={self.radius})"
